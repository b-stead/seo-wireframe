from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('landing1/', TemplateView.as_view(template_name='style1/landing.html'), name='landing1'),
    path('profile1/', TemplateView.as_view(template_name='style1/profile.html'), name='profile1'),
    path('dash/', TemplateView.as_view(template_name='style1/dashboard.html'), name='dashboard'),
    path('alumni/', TemplateView.as_view(template_name='style1/alumni.html'), name='alumni1'),
]