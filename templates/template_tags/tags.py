from docs.models import Folder, Document
from reminders.models import Reminder
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
    queryset = Folder.objects.filter(user_owner = user).order_by('-last_access')[:3]
        
    return {"folder_queryset":queryset}


@register.inclusion_tag("reminders_upcoming.html", takes_context=True)
def get_upcoming_reminders(context):
    request = context['request']
    user = request.user
    queryset = Reminder.objects.filter(user_owner = user, deadline__gte=datetime.now()).order_by('deadline')[:5]
    days_til = []
    for items in queryset:
       days_til.append(items.days_to_complete())
    queryset = zip(queryset, days_til)
    return {"reminders_queryset": queryset}
    
@register.inclusion_tag("recent_docs.html", takes_context=True)
def get_recent_docs(context):
    request = context['request']
    user = request.user
    queryset = Document.objects.filter(folder_parent__user_owner=user).order_by('-last_access')[:5]
    return {"doc_queryset":queryset}

@register.simple_tag
def get_url_self(obj):
    return obj.get_absolute_url()
