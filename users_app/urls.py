from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . views import custom_logout_view
from django.contrib.auth.views import LogoutView

class LogoutAllowGet(LoginView):
    http_method_names=['get','post']
urlpatterns = [
    path('register',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', custom_logout_view, name='logout'),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')  
    # path('logout/',LoginView.as_view(template_name='logout.html'),name='logout') 
    
]
