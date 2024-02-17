from django.contrib import admin
from django.urls import path,include
from advapp import views

app_name ='advapp'

urlpatterns = [
  path('',views.SchoolListView.as_view(),name='list'),
  path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),  
] 