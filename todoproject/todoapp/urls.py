from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    #path('delete/<int:taskid>/',views.delete,name='delete'),
    #path('update/<int:taskid>/',views.update_task,name='update_task'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskdeleteView.as_view(),name='cbvdelete'),

]
