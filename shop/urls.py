from django.urls import path

from .views import (
    HomeView, 
    ProjectDetailView,
    ConstructionsView,
    ConstructionsCategoryView, 
    ConstructionFormView,
    ConstructionDetailView,
    ProjectsView,
    CreateProjectView,
    construction_create,
    checkout_page,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_project/', CreateProjectView.as_view(), name='create_project'),
    path('projects_page/', ProjectsView.as_view(), name='projects_page'),
    path('project_detail/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('create_construction/', construction_create),
    path('constructions_page/<slug>/<str:category>', ConstructionsCategoryView.as_view(), name='category_page'),
    path('construction_detail_view.html/<str:slug>', ConstructionDetailView.as_view(), name='construction_detail_view'),
    path('update_construction/<int:id>', ConstructionFormView.as_view(), name='update_construction'),
    path('update_project/<int:id>', ConstructionFormView.as_view(), name='update_project'),
    path('checkout_page/', checkout_page)
]