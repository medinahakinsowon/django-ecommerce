from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.dashboard, name="dashboard"),
    
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('forgotPassword/', views.forgotPassword, name="forgotPassword"),
    path('passwordreset_validate/<uidb64>/<token>/', views.passwordreset_validate, name="passwordreset_validate"),
    path('resetPassword/', views.resetPassword, name="resetPassword"),
    
    #dashboard pages
    path('my_orders/', views.my_orders , name="my_orders"),
    path('edit_profile/', views.edit_profile , name="edit_profile"),
    path('change_password/', views.change_password , name="change_password"),
    path('order_detail/<int:order_id>/', views.order_detail, name="order_detail"),
]


# //the empty dashboard is to set the dashboard as the default page when a user loogged in//