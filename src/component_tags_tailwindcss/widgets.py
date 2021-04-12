from django.forms import widgets

__all__ = [
    'TailWindInputMixin',
    'TextInput',
    'NumberInput',
    'EmailInput',
    'PasswordInput',
    'CheckboxInput',
    'Select',
    'SelectMultiple',
    'TextArea'
]

WIDGET_ATTRS = {
    'class': 'my-2 px-2 py-2 placeholder-gray-400 text-gray-700 border-gray-400 text-sm border w-full'
}


class TailWindInputMixin:

    # noinspection PyUnresolvedReferences
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs'].update(WIDGET_ATTRS)
        return context


class TextInput(TailWindInputMixin, widgets.TextInput):
    pass


class NumberInput(TailWindInputMixin, widgets.NumberInput):
    pass


class EmailInput(TailWindInputMixin, widgets.EmailInput):
    pass


class PasswordInput(TailWindInputMixin, widgets.PasswordInput):
    pass


class CheckboxInput(widgets.CheckboxInput):

    def get_context(self, name, value, attrs):
        # noinspection PyUnresolvedReferences
        context = super().get_context(name, value, attrs)
        context['widget']['attrs'].update({
            'class': 'my-2 h-5 w-5 text-blue-600'
        })
        return context


class Select(TailWindInputMixin, widgets.Select):
    pass


class SelectMultiple(TailWindInputMixin, widgets.SelectMultiple):
    pass


class TextArea(TailWindInputMixin, widgets.Textarea):
    pass


# TODO: pending to solve
class SelectDateWidget(widgets.SelectDateWidget):
    pass
