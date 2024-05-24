from django.urls import path
from admin.views import admin_landing, content_management, user_management, edit_data

app_name = 'admin'

urlpatterns = [
    path('admin_landing/', admin_landing, name='admin_landing'),
    path('content_management/', content_management, name='content_management'),
    path('user_management/', user_management, name='user_management'),
    path('edit_data/<int:pk>/', edit_data, name='edit_data'),

]

urlpatterns = [
    path('suspend_user/<int:user_id>/', views.suspend_user, name='suspend_user'),
    path('unsuspend_user/<int=user_id>/', views.unsuspend_user, name='unsuspend_user'),
]
