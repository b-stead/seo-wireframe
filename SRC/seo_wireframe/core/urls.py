from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
]