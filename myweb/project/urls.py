from django.urls import path
from project import views

# TEMPLATE TAGGING
app_name = 'project'

urlpatterns = [
    path('heart_disease', views.heart_disease, name="heart_disease")
]
