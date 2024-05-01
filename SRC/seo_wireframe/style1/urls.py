from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('landing1/', TemplateView.as_view(template_name='style1/landing.html'), name='landing1'),
]