from django import template
from ..models import MenuItem, Menu 

register = template.Library()



@register.simple_tag()
#@register.assignment_tag
def get_menu(slug):
    return Menu.objects.get(slug=slug)
