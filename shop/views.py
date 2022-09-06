from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView, DetailView

from django.http import HttpResponseRedirect
from shop.models import Construction
from shop.forms import ConstructionForm

class HomeView(TemplateView):
    template_name = 'home_page.html'


class ConstructionDetailView(DetailView):
    model = Construction
    template_name = 'construction_detail_view.html'

     
class QuotationView(ListView):
    model = Construction
    template_name = 'quotation_page.html'
    paginate_by = 8

class QuotationCategoryView(ListView):
    model = Construction
    template_name = 'quotation_page.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return Construction.objects.filter(category__icontains = self.kwargs.get('category'))

#Function type View insted of ListView
#def quotation_page(request):
#    construction_list = Construction.objects.all()
#    context = {"construction_list": construction_list}
#    return render (request, 'quotation_page.html', context)

class ConstructionFormView(FormView):
    model = Construction
    template_name = 'update_construction.html'
    form_class = ConstructionForm
    success_url = '/quotation_page/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def construction_create(request):
    submitted = False
    if request.method == "POST":
        form = ConstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create?submitted=True')
    else:
        form = ConstructionForm
        if 'submitted' in request.GET:
            submitted = True

    context = {"form" : form, 'submitted':submitted}     
    return render (request, 'create.html', context=context, )

def checkout_page(request):
    return render (request, 'checkout_page.html', {})
