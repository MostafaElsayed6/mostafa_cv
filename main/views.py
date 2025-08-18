# from django.shortcuts import renderظ

# Create your views here.
# main/views.py
# from django.shortcuts import render
# from .models import *

# def home_view(request):
#     # الحصول على المحتوى النشط فقط
#     content = HomeContent.objects.filter(is_active=True).first()
    
#     # إذا لم يوجد محتوى، ننشئ واحدًا افتراضيًا
#     if not content:
#         content = HomeContent.objects.create(
#             greeting="مرحبا أنا",
#             name="اسمك هنا",
#             job_title="المسمى الوظيفي هنا",
#             email="example@example.com",
#             phone="+1234567890",
#             address="العنوان هنا",
#             is_active=True
#         )
    
#     return render(request, 'home.html', {'content': content})

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *

def home_view(request):
    context = {
        'content': HomeContent.objects.filter(is_active=True).first(),
        'about': AboutSection.objects.filter(is_active=True).first(),
        'services': Service.objects.filter(is_active=True),
        'tech_skills': Skill.objects.filter(skill_type='tech', is_active=True),
        'pro_skills': Skill.objects.filter(skill_type='pro', is_active=True),
        'education': Education.objects.filter(is_active=True),
        'experience': Experience.objects.filter(is_active=True),
        # ... بقية الأقسام ...
        'educations': Education.objects.filter(is_active=True).order_by('order'),
        'experiences': Experience.objects.filter(is_active=True).order_by('order'),
        'pricing_plans': PricingPlan.objects.filter(is_active=True).order_by('order'),
        #المدونة 
        'featured_posts': BlogPost.objects.filter(
            is_active=True, 
            is_featured=True
        ).order_by('-publish_date')[:3],
    
    }
    return render(request, 'home.html', context)

def blog_post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_active=True)
    return render(request, 'blog/post_detail1.html', {'post': post})