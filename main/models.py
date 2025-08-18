from django.db import models

# Create your models here.
# main/models.py
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

from django.db import models
from django_resized import ResizedImageField
from django.utils.safestring import mark_safe

class HomeContent(models.Model):
    greeting = models.CharField(max_length=50, default="مرحبا أنا", verbose_name="التحية")
    name = models.CharField(max_length=100, verbose_name="الاسم")
    job_title = models.CharField(max_length=100, verbose_name="المسمى الوظيفي")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, verbose_name="الهاتف")
    address = models.TextField(verbose_name="العنوان")
    profile_image = ResizedImageField(
        size=[500, 500],
        quality=85,
        upload_to='profile_images/',
        verbose_name="الصورة الشخصية",
        blank=True,
        null=True
    )
    
    # وسائط التواصل الاجتماعي
    facebook_url = models.URLField(blank=True, null=True, verbose_name="فيسبوك")
    twitter_url = models.URLField(blank=True, null=True, verbose_name="تويتر")
    github_url = models.URLField(blank=True, null=True, verbose_name="جيت هاب")
    dribbble_url = models.URLField(blank=True, null=True, verbose_name="دریبل")
    
    # إعدادات إضافية
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "محتوى الصفحة الرئيسية"
        verbose_name_plural = "محتوى الصفحة الرئيسية"

    def __str__(self):
        return f"محتوى الصفحة الرئيسية - {self.name}"



###############################################################

    # ... النموذج الحالي كما هو ...

class AboutSection(models.Model):
    title = models.CharField(max_length=100, default="عني", verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    cv_url = models.URLField(verbose_name="رابط السيرة الذاتية")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    
    class Meta:
        verbose_name = "قسم عني"
        verbose_name_plural = "قسم عني"

    def __str__(self):
        return self.title

class Skill(models.Model):
    SKILL_TYPES = (
        ('tech', 'مهارات تقنية'),
        ('pro', 'مهارات احترافية'),
    )
    
    name = models.CharField(max_length=100, verbose_name="اسم المهارة")
    percentage = models.IntegerField(verbose_name="النسبة المئوية")
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPES, verbose_name="نوع المهارة")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    
    class Meta:
        verbose_name = "مهارة"
        verbose_name_plural = "المهارات"

    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"

class Service(models.Model):
    icon = models.CharField(max_length=50, verbose_name="الأيقونة")
    title = models.CharField(max_length=100, verbose_name="عنوان الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    
    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        ordering = ['id']

    def __str__(self):
        return self.title

class Education(models.Model):
    institute = models.CharField(max_length=200, verbose_name="المعهد/الجامعة")
    degree = models.CharField(max_length=200, verbose_name="الدرجة العلمية")
    period = models.CharField(max_length=50, verbose_name="الفترة الزمنية")
    description = models.TextField(verbose_name="الوصف")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    
    class Meta:
        verbose_name = "تعليم"
        verbose_name_plural = "التعليم"

    def __str__(self):
        return f"{self.degree} - {self.institute}"

class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="الشركة")
    position = models.CharField(max_length=200, verbose_name="المنصب")
    period = models.CharField(max_length=50, verbose_name="الفترة الزمنية")
    responsibilities = models.TextField(verbose_name="المسؤوليات")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    
    class Meta:
        verbose_name = "خبرة عمل"
        verbose_name_plural = "خبرات العمل"

    def __str__(self):
        return f"{self.position} - {self.company}"

# ... نماذج مشابهة للأقسام الأخرى (Portfolio, Pricing, Blog, Testimonial, ContactInfo) ...

class Education(models.Model):
    institute = models.CharField(max_length=200, verbose_name="المعهد/الجامعة")
    degree = models.CharField(max_length=200, verbose_name="الدرجة العلمية")
    period = models.CharField(max_length=50, verbose_name="الفترة الزمنية")
    description = models.TextField(verbose_name="الوصف")
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    
    class Meta:
        verbose_name = "تعليم"
        verbose_name_plural = "التعليم"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.degree} - {self.institute}"

class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="الشركة")
    position = models.CharField(max_length=200, verbose_name="المنصب")
    period = models.CharField(max_length=50, verbose_name="الفترة الزمنية")
    responsibilities = models.TextField(
        verbose_name="المسؤوليات",
        help_text="أدخل كل مسؤولية في سطر جديد"
    )
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    
    class Meta:
        verbose_name = "خبرة عمل"
        verbose_name_plural = "خبرات العمل"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.position} - {self.company}"
    
    def get_responsibilities_list(self):
        return self.responsibilities.split('\n') if self.responsibilities else []


 # ################################################################3
class PricingPlan(models.Model):
    PLAN_TYPES = (
        ('full_time', 'العمل بدوام كامل'),
        ('fixed', 'مشروع سعر ثابت'),
        ('hourly', 'العمل كل ساعة'),
    )
    
    plan_type = models.CharField(
        max_length=20, 
        choices=PLAN_TYPES, 
        verbose_name="نوع الخطة"
    )
    title = models.CharField(max_length=100, verbose_name="عنوان الخطة")
    description = models.TextField(verbose_name="وصف الخطة")
    price = models.CharField(max_length=50, verbose_name="السعر")
    features = models.TextField(
        verbose_name="الميزات",
        help_text="أدخل كل ميزة في سطر جديد"
    )
    button_text = models.CharField(
        max_length=50, 
        default="وظفني", 
        verbose_name="نص الزر"
    )
    button_url = models.URLField(
        default="#", 
        verbose_name="رابط الزر"
    )
    icon = models.CharField(
        max_length=50, 
        verbose_name="الأيقونة",
        help_text="استخدم أسماء أيقونات FontAwesome مثل: fa-calendar"
    )
    is_active = models.BooleanField(default=True, verbose_name="مفعل")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    
    class Meta:
        verbose_name = "خطة تسعير"
        verbose_name_plural = "خطط التسعير"
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def get_features_list(self):
        return self.features.split('\n') if self.features else []
    
    def get_icon_class(self):
        return f"fa {self.icon}"



#########################################################################


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المنشور")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="رابط المنشور")
    content = models.TextField(verbose_name="محتوى المنشور")
    excerpt = models.TextField(max_length=300, verbose_name="ملخص المنشور")
    cover_image = models.ImageField(
        upload_to='blog/covers/',
        verbose_name="صورة الغلاف",
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="المؤلف"
    )
    publish_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاريخ النشر"
    )
    is_featured = models.BooleanField(default=False, verbose_name="مميز")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "منشور المدونة"
        verbose_name_plural = "منشورات المدونة"
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f"/blog/{self.slug}/"