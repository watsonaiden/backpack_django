from docs.models import Folder
from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def current_time(format_string):
    now = datetime.now()
    current_time = now.strftime(format_string)
    return current_time

@register.inclusion_tag("top3.html", takes_context=True)
def get_top3_folders(context):
    request = context['request']
    user = request.user
    queryset = Folder.objects.filter(user_owner = user).order_by('last_access')[:5]
        
    return {"folder_queryset":queryset}
    
