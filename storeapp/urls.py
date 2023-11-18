from django.urls import path
from . import views

app_name = 'storeapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('userpage/',views.userpage,name='userpage'),
    path('form/',views.form,name='form'),
    path('logout/',views.logout,name='logout')


]