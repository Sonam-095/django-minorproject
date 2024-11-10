from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('moodinput/',views.moodinput,name='moodinput'),
    path('recommendation/',views.recommendation,name='recommendation')
]