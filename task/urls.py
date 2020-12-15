from . import views
from django.urls import path,re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('all-tasks/', views.TaskIndexView.as_view(), name='allTasks'),
    path('my-tasks/', views.MyTaskView.as_view(), name='myTasks'),
    path('new-task/', views.CreateTaskView.as_view(), name='newTask'),
    path('taskDetail/<int:taskid>/detail/', views.taskDetail, name='taskDetail'),
    path('update/<int:taskid>/edit/', views.UpdateTaskView.as_view(), name='editTask'),
    path('delete/<int:taskid>/delete/', views.DeleteTaskView.as_view(), name='deleteTask'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),
]
