from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProfilArty.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name = 'logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
