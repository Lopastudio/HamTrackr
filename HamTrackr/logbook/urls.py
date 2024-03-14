from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('log_contact/', views.log_contact, name='log_contact'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("register/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
