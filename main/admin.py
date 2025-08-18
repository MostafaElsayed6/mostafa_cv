from django.contrib import admin
from .models import *

# Register your models here.
# main/admin.py
# from django.contrib import admin
from .models import HomeContent
from django.utils.html import format_html

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'email', 'is_active', 'preview_image')
    list_editable = ('is_active',)
    search_fields = ('name', 'email', 'job_title')
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': (
                'is_active',
                'greeting',
                'name',
                'job_title',
                'email',
                'phone',
                'address',
            )
        }),
        ('الصورة الشخصية', {
            'fields': ('profile_image', 'image_preview'),
            'classes': ('collapse',)
        }),
        ('وسائل التواصل الاجتماعي', {
            'fields': (
                'facebook_url',
                'twitter_url',
                'github_url',
                'dribbble_url',
            ),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="150" height="150" style="border-radius:50%;object-fit:cover;" />',
                obj.profile_image.url
            )
        return "لا توجد صورة"
    image_preview.short_description = "معاينة الصورة"
    
    def preview_image(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;object-fit:cover;" />',
                obj.profile_image.url
            )
        return "لا توجد صورة"
    preview_image.short_description = "الصورة"
    ##################################################
    from django.contrib import admin





@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'percentage', 'is_active')
    list_filter = ('skill_type', 'is_active')
    list_editable = ('percentage', 'is_active')

# ... تسجيل بقية النماذج بنفس الطريقة ...


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institute', 'degree', 'period', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('institute', 'degree')
    fieldsets = (
        (None, {
            'fields': ('institute', 'degree', 'period', 'description')
        }),
        ('الإعدادات', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'period', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('company', 'position')
    fieldsets = (
        (None, {
            'fields': ('company', 'position', 'period', 'responsibilities')
        }),
        ('الإعدادات', {
            'fields': ('is_active', 'order')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 5})}
    }
    ##################################################
@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan_type', 'price', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'plan_type')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': (
                'plan_type', 
                'title', 
                'description', 
                'price',
                'features',
                'button_text',
                'button_url',
                'icon'
            )
        }),
        ('الإعدادات', {
            'fields': ('is_active', 'order')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 4})}
    }
#######################################

from django.utils.html import format_html

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'is_featured', 'is_active', 'cover_image_preview')
    list_editable = ('is_featured', 'is_active')
    list_filter = ('is_featured', 'is_active', 'publish_date')
    search_fields = ('title', 'content', 'excerpt')
    date_hierarchy = 'publish_date'
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('محتوى المنشور', {
            'fields': (
                'title', 
                'slug', 
                'content', 
                'excerpt',
                'cover_image',
                'cover_image_preview'
            )
        }),
        ('الإعدادات', {
            'fields': (
                'author',
                'publish_date',
                'is_featured',
                'is_active'
            )
        }),
    )
    
    readonly_fields = ('cover_image_preview',)
    
    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="150" />', obj.cover_image.url)
        return "لا توجد صورة"
    cover_image_preview.short_description = "معاينة الصورة"