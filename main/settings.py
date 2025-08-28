# إعدادات البريد الإلكتروني
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # أو مزود البريد الإلكتروني الخاص بك
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # بريدك الإلكتروني
EMAIL_HOST_PASSWORD = 'your-app-password'  # كلمة المرور أو كلمة مرور التطبيق
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'  # بريدك الإلكتروني

# إدارة الموقع للإشعارات
ADMINS = [
    ('Your Name', 'your-email@gmail.com'),
]