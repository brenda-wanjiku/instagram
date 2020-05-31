from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('search/', views.search_results, name='search_results'),
    path('profile/',views.profile, name = "profile"),
    path('update_profile/',views.update_profile, name = "update_profile"),
    path('upload_image/',views.upload_image, name = "update_image")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)