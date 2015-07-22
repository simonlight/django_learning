from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Template
from django.template import  Context

def current_datetime(request):
    now = datetime.datetime.now()
    tpl = get_template("current_time.html")
#     tpl = Template("<html><body>It is now {{ current_date }}</body></html>")
    html = tpl.render(Context({'current_date': now}))
    return HttpResponse(html)
