from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index" ),
    path("search/", views.search, name="search"),
    path("post/<str:slug>", views.detail, name="detail"),
    path('contact/', views.contact_view, name='contact'),
    path("about", views.about_view, name="about" ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

