from django.conf.urls import url
from . import views

app_name='console'

urlpatterns = [
    url(r'^logout/', views.signout,name='signout'),
    url(r'^register/',views.register,name='registration'),

]