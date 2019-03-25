from django.conf.urls import url
from . import views

#TEMPATE URLS!

app_name = 'pass_app'

urlpatterns= [
    url(r'^register/$',views.register,name='register'),
    url(r'^userlogin/$',views.user_login,name='user_login'),
]
