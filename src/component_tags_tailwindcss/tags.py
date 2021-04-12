from component_tags import template


class BadgeColorChoices(template.AttributeChoices):
    primary = 'bg-blue-500 text-white'
    success = 'bg-green-500 text-white'
    warning = 'bg-yellow-500 text-white'
    error = 'bg-red-500 text-white'
    default = 'border'


def badge(value, color='primary', **attributes):
    color_choice = getattr(BadgeColorChoices, color, BadgeColorChoices.default)
    context = template.TagContext(attributes)
    context['value'] = value
    context.add_class('w-auto inline-block align-middle px-1 rounded-full', color_choice.value)
    return context.flatten()


def breadcrumb_item(title, href='#', active=False, **attributes):
    context = template.TagContext(attributes)
    context.add_class('px-2')

    if not active:
        context.add_class('text-blue-500 hover:text-blue-700')

    context['title'] = title
    context['href'] = href
    context['active'] = active
    return context.flatten()


def dropdown_item(title, href='#', **attributes):
    context = template.TagContext(attributes)
    context['title'] = title
    context['href'] = href
    return context.flatten()


def dropdown_item_divider(**attributes):
    context = template.TagContext(attributes)
    return context.flatten()
