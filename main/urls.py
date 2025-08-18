# main/urls.py
from django.urls import path
from . import views

from .views import home_view  # استيراد الدالة مباشرة

urlpatterns = [
    path('', home_view, name='home'),  # المسار الرئيسي
    path('blog/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
]