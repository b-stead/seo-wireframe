from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('landing2/', TemplateView.as_view(template_name='style2/landing.html'), name='landing2'),
    path('profile2/', TemplateView.as_view(template_name='style2/profile.html'), name='profile2'),
    path('profile2-2/', TemplateView.as_view(template_name='style2/profile2-2.html'), name='profile2-2'),
    path('events2/', TemplateView.as_view(template_name='style2/events.html'), name='events2'),
    path('alumni2/', TemplateView.as_view(template_name='style2/alumni.html'), name='alumni2'),
    path('resources2/', TemplateView.as_view(template_name='style2/resources.html'), name='resources2'),
]