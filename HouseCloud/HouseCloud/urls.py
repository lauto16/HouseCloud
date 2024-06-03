from Cloud.views import *
from Sign.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view')
]
