from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', include('webapp.urls')),
    path('', include('userapp.urls')),
    path('nzl/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('password/reset', auth_view.PasswordResetView.as_view(template_name= 'password/password_reset.html'), name='password_reset'),
    path('password/reset/done', auth_view.PasswordResetDoneView.as_view(template_name= 'password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name= 'password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password/reset/complete', auth_view.PasswordResetCompleteView.as_view(template_name= 'password/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)