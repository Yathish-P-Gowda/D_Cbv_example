from django.contrib import admin
from django.urls import path,include
from advapp import views

app_name ='advapp'

urlpatterns = [
  path('',views.SchoolListView.as_view(),name='list'),
  path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),  #int pk automatically takes a primary key 
  path('create',views.SchoolCreateView.as_view(),name='create'),
  path('<int:pk>/update/', views.SchollUpdateView.as_view(), name='update'),
  path('<int:pk>/delete/', views.SchoolDelete_view.as_view(), name='delete'),
] 
