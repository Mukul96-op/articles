from django.urls import path
from authy.views import  Signup ,EditProfile , PasswordChange ,ChangePasswordDone
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    
    path('profile/edit', EditProfile ,name= 'edit-profile'),
    path('signup/' ,Signup ,name = 'signup'),
    path('login/',LoginView.as_view(template_name="login.html") , name= 'login'),
    path('logout/',LogoutView.as_view(),{'next_page':'home'} , name= 'logout'),

    path('changepassword/',PasswordChange , name = 'changepassword'),
    path('changepassword/done/',ChangePasswordDone , name= 'change_password_done'),
]
