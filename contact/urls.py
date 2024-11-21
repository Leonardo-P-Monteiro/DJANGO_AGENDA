from django.urls import path
from contact import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name = 'contact'),
    path('search/', views.search, name = 'search'),
    path('', views.index, name = 'index' ),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)