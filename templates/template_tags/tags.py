from docs.models import Folder
from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def current_time(format_string):
    now = datetime.now()
    current_time = now.strftime(format_string)
    return current_time
