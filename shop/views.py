from django.http import Http404
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DetailView, UpdateView, DetailView, CreateView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages

from shop.models import Construction, Project
from shop.forms import ConstructionForm, ProjectForm

class HomeView(TemplateView):
    template_name = 'home_page.html'

class ProjectsView(ListView):
    model = Project
    template_name = 'projects_page.html'
    paginate_by = 8

class CreateProjectView(CreateView):
    model = Project
    template_name = 'create_project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The project has been created'
        )
        return super().form_valid(form)

class EditProjectView(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The project has been created'
        )
        return super().form_valid(form)


class ProjectDetailView(ListView):
    template_name = 'project_detail.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('category') == "all":
            queryset = Construction.objects.all().filter(project=self.kwargs.get('pk'))
        else:
            queryset = Construction.objects.all().filter(project=self.kwargs.get('pk'), category=self.kwargs.get('category'))
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        project= Project.objects.get(id=self.kwargs.get('pk'))
        context.update({'project_id':project.id, 'project_name':project.name})
        return context

class ConstructionDetailView(DetailView):
    model = Construction
    template_name = 'construction_detail_view.html'
    
    #Changing the get_object() method to first look by the "slug" and then by "pk"
    def get_object(self, queryset=None):
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None :
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # Next, try looking up by pk.
        if pk is not None and (slug is None or self.query_pk_and_slug):
            queryset = queryset.filter(pk=pk)
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj    

class ConstructionFormView(UpdateView):
    model = Construction
    template_name = 'update_construction.html'
    form_class = ConstructionForm
    success_url = '/project_detail/1/all/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    #Changing the get_object() method to first look by the "slug" and then by "pk"
    def get_object(self, queryset=None):
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None :
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # Next, try looking up by pk.
        if pk is not None and (slug is None or self.query_pk_and_slug):
            queryset = queryset.filter(pk=pk)
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj 



class CreateConstructionView(CreateView):
    model = Construction
    template_name = 'crate_construction.html'
    form_class = ConstructionForm
    success_url = '/project_detail/1/all/'
    print(success_url)
    
    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The construction has been created'
        )
        return super().form_valid(form)

    def get_success_url(self):
        if self.success_url:
            url = '/project_detail/1/all/'
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

def construction_create(request, **kwargs):
    submitted = False
    if request.method == "POST":
        form = ConstructionForm(request.POST)
        if form.is_valid():
            form.save()
            proj_id = form.cleaned_data['project'].id
            return HttpResponseRedirect(f'/project_detail/{proj_id}/all?submitted=True')  
    else:
        form = ConstructionForm
        if 'submitted' in request.GET:
            submitted = True

    context = {"form" : form, 'submitted':submitted}     
    return render (request, 'create_construction.html', context=context, )

def checkout_page(request):
    return render (request, 'checkout_page.html', {})