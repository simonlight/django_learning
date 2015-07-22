from django.conf.urls import * 
from HelloWorld.view import current_datetime 
urlpatterns = patterns("",
        ('^time/$', current_datetime),
)