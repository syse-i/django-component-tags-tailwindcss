from component_tags import template

from ..components import (
    Alert,
    Breadcrumb,
    Button,
    Card,
    Dropdown,
    Label,
    Modal,
    Link,
)

from ..tags import badge, breadcrumb_item, dropdown_item, dropdown_item_divider

register = template.Library()

# Components
register.tag('alert', Alert)
register.tag('link', Link)
register.tag('button', Button)
register.tag('breadcrumb', Breadcrumb)
register.tag('card', Card)
register.tag('dropdown', Dropdown)
register.tag('label', Label)
register.tag('modal', Modal)

# Inclusion Tags
register.inclusion_tag('component_tags_tailwindcss/tags/badge.html')(badge)
register.inclusion_tag('component_tags_tailwindcss/tags/breadcrumb_item.html')(breadcrumb_item)
register.inclusion_tag('component_tags_tailwindcss/tags/dropdown_item.html')(dropdown_item)
register.inclusion_tag('component_tags_tailwindcss/tags/dropdown_item_divider.html')(dropdown_item_divider)
