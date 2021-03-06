from django.contrib import admin
from django import template
from django.utils.text import capfirst
from django.core.urlresolvers import NoReverseMatch, reverse
from django.apps import apps

register = template.Library()

@register.inclusion_tag('admin/top.html', takes_context=True)
def get_all_apps(context):
    app_dict = {}
    request = context['request']
    models = admin.site._registry
    for model, model_admin in models.items():
        app_label = model._meta.app_label

        has_module_perms = model_admin.has_module_permission(request)
        if not has_module_perms:
            continue

        perms = model_admin.get_model_perms(request)

        # Check whether user has any perm for this module.
        # If so, add the module to the model_list.
        if True not in perms.values():
            continue

        info = (app_label, model._meta.model_name)
        model_dict = {
            'name': capfirst(model._meta.verbose_name_plural),
            'object_name': model._meta.object_name,
            'perms': perms,
        }
        if perms.get('change'):
            try:
                model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app='admin')
            except NoReverseMatch:
                pass
        if perms.get('add'):
            try:
                model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app='admin')
            except NoReverseMatch:
                pass

        if app_label in app_dict:
            app_dict[app_label]['models'].append(model_dict)
        else:
            app_dict[app_label] = {
                'name': apps.get_app_config(app_label).verbose_name,
                'app_label': app_label,
                'app_url': reverse(
                    'admin:app_list',
                    kwargs={'app_label': app_label},
                    current_app='admin',
                ),
                'has_module_perms': has_module_perms,
                'models': [model_dict],
            }

    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    # Sort the models alphabetically within each app.
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])

    return {'all_apps_list': app_list}
