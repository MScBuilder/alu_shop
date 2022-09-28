from django.urls import path

from .views import (
    HomeView, 
    ProjectDetailView,
    EditProjectView,
    ConstructionFormView,
    ConstructionDetailView,
    ProjectsView,
    CreateProjectView,
    CreateConstructionView,
    construction_create,
    checkout_page,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_project/', CreateProjectView.as_view(), name='create_project'),
    path('projects_page/', ProjectsView.as_view(), name='projects_page'),
    path('project_detail/<int:pk>/<str:category>', ProjectDetailView.as_view(), name='project_detail'),
    path('update_project/<int:id>', EditProjectView.as_view(), name='update_project'),
    path('create_construction/<int:pk>', CreateConstructionView.as_view(), name='create_construction'),
    path('construction_detail_view/<int:pk>/<slug:slug>', ConstructionDetailView.as_view(), name='construction_detail_view'),
    path('update_construction/<int:pk>/<slug:slug>', ConstructionFormView.as_view(), name='update_construction'),
    path('checkout_page/', checkout_page)
    
]