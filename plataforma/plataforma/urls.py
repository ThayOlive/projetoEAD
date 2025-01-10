
from django.contrib import admin
from django.urls import include, path
from cursos import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from plataforma import settings
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('main/', views.main, name="main"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login, name='login'),
    path('acessar/<int:curso_id>/', views.acessar, name="acessar"),
    path('visualizar-pdf/<int:material_id>/', views.visualizar_pdf, name='visualizar_pdf'),
    path('marcar-assistido/<int:video_id>/', views.marcar_assistido, name='marcar_assistido'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('login/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header= "Painel Administrativo"
admin.AdminSite.site_title = "Painel Administrativo"
admin.AdminSite.index_title = "Administração"