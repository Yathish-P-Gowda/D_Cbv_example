from typing import Any
from. import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# from django.http import HttpResponse
# # Create your views here.

# class CBview(View):
#     def get(self,request):
#         return HttpResponse("This is a class based view cool bro")

# # def get(request):
# #     return render(request,'index.html')

class Index_View(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection...!'
        return context

class SchoolListView(ListView):
    context_object_name='schools'
    model = models.School  #it returns a list with name school_list
    template_name = 'advapp/school_list.html' 
    
class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model = models.School  # it returns just model lower case (school)
    template_name = 'advapp/schoold_details.html'
    
class SchoolCreateView(CreateView):
    fields = '__all__'
    model=models.School
    template_name = 'advapp/school_form.html'


class SchollUpdateView(UpdateView):
    fields=('name','principal')
    model = models.School
    template_name = 'advapp/school_update.html'
    
class SchoolDelete_view(DeleteView):
    model = models.School
    success_url = reverse_lazy("advapp:list")
    template_name = 'advapp/school_delete.html'
    
