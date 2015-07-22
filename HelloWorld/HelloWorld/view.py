from django.shortcuts import render_to_response
import datetime

def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_head.html', {'hour_offset':offset, 'next_time':dt}) 

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_time.html', {'current_date': now})
