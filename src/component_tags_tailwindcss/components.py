from django.utils.translation import ugettext as _

from component_tags import template


class Link(template.Component):
    class ColorChoices(template.AttributeChoices):
        primary = 'text-blue-500 hover:text-blue-700 hover:underline'
        secondary = 'text-gray-700 hover:text-gray-800 hover:underline'
        text = secondary
        default = primary

    color = template.Attribute(choices=ColorChoices, default=ColorChoices.default, as_class=True)
    href = template.Attribute(default='#', as_context=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/link.html'


class Alert(template.Component):
    class ColorChoices(template.AttributeChoices):
        primary = 'border-blue-500 bg-blue-200 text-blue-700'
        success = 'border-green-500 bg-green-200 text-green-700'
        warning = 'border-yellow-500 bg-yellow-200 text-yellow-700'
        error = 'border-red-500 bg-red-200 text-red-700'
        default = 'border'
        info = primary

    color = template.Attribute(choices=ColorChoices, default=ColorChoices.default, as_class=True)
    close = template.Attribute(default=True, as_context=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/alert.html'
        js = [
            'component_tags_tailwindcss/js/js.js'
        ]

    def get_context_data(self, context):
        context = super().get_context_data(context)
        context.add_class('px-6 py-4')
        return context


class Breadcrumb(template.Component):

    def get_context_data(self, context):
        context = super().get_context_data(context)
        context.add_class('flex items-center justify-start leading-none divide-x divide-gray-500')
        return context

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/breadcrumb.html'


class Button(template.Component):
    class ColorChoices(template.AttributeChoices):
        primary = 'py-2 px-4 bg-blue-500 hover:bg-blue-700 text-white rounded border-blue-700'
        success = 'py-2 px-4 bg-green-500 hover:bg-green-700 text-white rounded border-green-700'
        warning = 'py-2 px-4 bg-yellow-500 hover:bg-yellow-700 text-white rounded border-yellow-700'
        error = 'py-2 px-4 bg-red-500 hover:bg-red-700 text-white rounded border-red-700'
        default = 'py-2 px-4 rounded border'
        link = 'py-2 px-4 text-blue-500 hover:text-blue-700'

    color = template.Attribute(choices=ColorChoices, default=ColorChoices.default, as_class=True)
    click = template.Attribute(context_name='@click')

    class TypeChoices(template.AttributeChoices):
        button = 'button'
        reset = 'reset'
        submit = 'submit'

    type = template.Attribute(choices=TypeChoices, default=TypeChoices.submit)
    disabled = template.Attribute(default=None)

    href = template.Attribute(default=None, as_context=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/button.html'

    def get_context_data(self, context):
        context = super().get_context_data(context)
        return context


class Card(template.Component):
    title = template.Attribute(required=False, as_context=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/card.html'


class Dropdown(template.Component):
    title = template.Attribute(required=False, as_context=True)

    class PositionChoices(template.AttributeChoices):
        left = 'origin-top-left left-0'
        right = 'origin-top-right right-0'

    position = template.Attribute(choices=PositionChoices, default=PositionChoices.left, as_context=True)

    class TextPositionChoices(template.AttributeChoices):
        left = 'text-left'
        right = 'text-right'

    text_position = template.Attribute(choices=TextPositionChoices, default=TextPositionChoices.left, as_context=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/dropdown.html'
        js = [
            'component_tags_tailwindcss/js/js.js'
        ]


class Label(template.Component):

    class ColorChoices(template.AttributeChoices):
        primary = 'bg-blue-500 text-white'
        success = 'bg-green-500 text-white'
        warning = 'bg-yellow-500 text-white'
        error = 'bg-red-500 text-white'

    color = template.Attribute(choices=ColorChoices, default=ColorChoices.primary, as_class=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/label.html'

    def get_context_data(self, context):
        context = super().get_context_data(context)
        context.add_class('text-xs inline-block py-1 px-2 rounded uppercase last:mr-0 mr-1')
        return context


class Modal(template.Component):
    title = template.Attribute(default=_('Modal Title'), as_context=True)
    close = template.Attribute(default=True, as_context=True)

    class Meta:
        template_name = 'component_tags_tailwindcss/tags/modal.html'
        js = [
            'component_tags_tailwindcss/js/js.js'
        ]
