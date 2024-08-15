from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hexlet_django_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.about),
    path('articles/', include('hexlet_django_blog.article.urls'), name='articles'),
] #+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
