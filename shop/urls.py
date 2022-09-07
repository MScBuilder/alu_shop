from django.contrib import admin
from django.urls import path

from .views import (
    HomeView, 
    checkout_page,
    construction_create,
    project_create,
    ConstructionsView,
    ConstructionsCategoryView, 
    ConstructionFormView,
    ConstructionDetailView,
    ProjectsView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view()),
    path('create_project/', project_create),
    path('projects_page/', ProjectsView.as_view(), name='projects_page'),
    path('create_construction/', construction_create),
    path('constructions_page/<slug>', ConstructionsView.as_view(), name='constructions_page'),
    path('constructions_page/<slug>/<str:category>', ConstructionsCategoryView.as_view()),
    path('construction_detail_view.html/<slug>', ConstructionDetailView.as_view(), name='construction_detail_view'),
    path('update_construction/<id>', ConstructionFormView.as_view(), name='update_construction'),
    path('update_project/<id>', ConstructionFormView.as_view(), name='update_project'),
    path('checkout_page/', checkout_page)
]