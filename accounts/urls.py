from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('signup/', views.StudentsSignupView.as_view(), name='signup'),
    path('staff/signup/staff/', views.StaffSignupView.as_view(), name='staff_signup'),
    path('nonstaff/signup/', views.NonStaffSignupView.as_view(), name='non_staff_signup'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_user'),
]