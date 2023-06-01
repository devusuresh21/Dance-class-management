from atexit import register
from django.contrib import admin
from django.urls import path
from danceapp import views
from danceapp.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
urlpatterns = [
    
    path('', index, name='index'),  
    
    path('sign_up/', sign_up, name='sign_up'),
    path('user_login/', user_login, name='user_login'),
    path('sign_up/user_login/', sign_up, name='sign_up_user_login'),
    path('sign_up/user_login/', user_login, name='sign_up_user_login'),
    path('user_login/sign_up.html', sign_up, name='user_login_sign_up'),
    path('user_login/index.html', sign_up, name='user_login_index'),
   
    path('user_login/user_home', user_login, name='user_login_user_home'),
    path('user_login/register/', views.register_user, name='user_login_register'),
    path('user_login/index/', views.index, name='user_login_index'),
    path('user_home/', views.user_home, name='user_home'),
    path('usercategories/',views.usercategories),

  
    
    path('events/', views.event_list, name='events'),
    path('events/', views.event_list, name='events_list'),
    path('confirm_event/<int:event_id>/', views.confirm_event, name='confirm_event'),



    path('changepassword/', views.changepassword, name='changepassword'),
    path('user_home/changepassword/', views.changepassword, name='user_home_changepassword'),
    path('video/', views.video),
    path('viewdetails/', viewdetails, name='viewdetails'),
    path('viewdetails/', views.viewdetails, name='viewdetails'),
    path('my_Profile', views.my_Profile, name='my_Profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_Profile/edit_profile', views.edit_profile, name='my_Profile_edit_profile'),
    path('videos/', views.video, name='video'),
    path('register/', views.register_user, name='register'),
    path('register/register/user_home.html', views.register_user, name='register_user_home'),
    path('category/',views.category),
    path('stream/',views.stream),
    path('changepassword', changepassword, name='changepassword'),
    path('user_login/register', Register, name='user_login_register'),
    path('logout', Logout, name='logout'),
    path('confirm/<int:pk>',views.confirm_event)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
