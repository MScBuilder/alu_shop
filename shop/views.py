from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView, DetailView

from django.http import HttpResponseRedirect
from shop.models import Construction, Project
from shop.forms import ConstructionForm, ProjectForm

class HomeView(TemplateView):
    template_name = 'home_page.html'


class ConstructionDetailView(DetailView):
    model = Construction
    template_name = 'construction_detail_view.html'

     
class ConstructionsView(ListView):
    model = Construction
    template_name = 'constructions_page.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return Construction.objects.filter(project_name__name__icontains = self.kwargs.get('slug'))
    

class ConstructionsCategoryView(ListView):
    model = Construction
    template_name = 'constructions_page.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return Construction.objects.filter(category__icontains = self.kwargs.get('category'))

class ProjectsView(ListView):
    model = Project
    template_name = 'projects_page.html'
    paginate_by = 8

class ConstructionFormView(FormView):
    model = Construction
    template_name = 'update_construction.html'
    form_class = ConstructionForm
    success_url = '/constructions_page/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def project_create(request):
    submitted = False
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_project?submitted=True')
    else:
        form = ProjectForm
        if 'submitted' in request.GET:
            submitted = True

    context = {"form" : form, 'submitted':submitted}     
    return render (request, 'create_project.html', context=context, )


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
