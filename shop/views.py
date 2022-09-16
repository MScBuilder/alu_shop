from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages

from shop.models import Construction, Project
from shop.forms import ConstructionForm

class HomeView(TemplateView):
    template_name = 'home_page.html'

class ProjectsView(ListView):
    model = Project
    template_name = 'projects_page.html'
    paginate_by = 8

class CreateProjectView(CreateView):
    model = Project
    template_name = 'create_project.html'
    fields = ['user', 'name']

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The project has been created'
        )
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    

class ConstructionDetailView(DetailView):
    model = Construction
    template_name = 'construction_detail_view.html'

     
class ConstructionsView(ListView):
    model = Construction
    template_name = 'constructions_page.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        query_set = Construction.objects.filter(project_name__name__icontains = self.kwargs.get('slug'))
        return query_set


class ConstructionsCategoryView(ListView):
    model = Construction
    template_name = 'constructions_page.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        query_set = Construction.objects.filter(project_name__name__icontains = self.kwargs.get('slug')).filter(category__icontains = self.kwargs.get('category'))
        return query_set

class ConstructionFormView(FormView):
    model = Construction
    template_name = 'update_construction.html'
    form_class = ConstructionForm
    success_url = '/constructions_page/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def construction_create(request):
    submitted = False
    if request.method == "POST":
        form = ConstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_construction?submitted=True')
    else:
        form = ConstructionForm
        if 'submitted' in request.GET:
            submitted = True

    context = {"form" : form, 'submitted':submitted}     
    return render (request, 'create_construction.html', context=context, )

def checkout_page(request):
    return render (request, 'checkout_page.html', {})
