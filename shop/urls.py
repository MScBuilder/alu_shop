from django.urls import path

from .views import (
    HomeView, 
    ProjectDetailView,
    ProjectDeleteView,
    EditProjectView,
    ConstructionFormView,
    ConstructionDetailView,
    ProjectsView,
    CreateProjectView,
    CreateConstructionView,
    UserDetailView,
    construction_create,
    checkout_page,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_project/', CreateProjectView.as_view(), name='create_project'),
    path('projects_page/', ProjectsView.as_view(), name='projects_page'),
    path('project_detail/<int:pk>/<str:category>', ProjectDetailView.as_view(), name='project_detail'),
    path('project_delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('update_project/<int:pk>', EditProjectView.as_view(), name='update_project'),
    path('create_construction/<int:pk>', CreateConstructionView.as_view(), name='create_construction'),
    path('construction_detail_view/<int:pk>/<slug:slug>', ConstructionDetailView.as_view(), name='construction_detail_view'),
    path('update_construction/<int:pk>/<slug:slug>', ConstructionFormView.as_view(), name='update_construction'),
    path('profile_page/<int:pk>', UserDetailView.as_view(), name='profile_page'),
    path('checkout_page/', checkout_page)
    
]