from django.urls import path
from contact import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contact'

urlpatterns = [
    path('', views.index, name = 'index' ),
    path('search/', views.search, name = 'search'),
    
    # CONTACT (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name = 'contact'),
    path('contact/create/', views.create, name = 'create'),
    path('contact/<int:contact_id>/update/', views.update, name = 'update'),
    path('contact/<int:contact_id>/delete/', views.delete, name = 'delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)