from django.conf.urls import * 
from HelloWorld.view import * 
urlpatterns = patterns("",
        ('^time/$', current_datetime),
        ('^time/(\d{1,2})$', hours_head),
)