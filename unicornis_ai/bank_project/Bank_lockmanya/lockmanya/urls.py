from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.signup , name="signup"),
    path('dashboard' , views.Dashboard , name='dashboard') ,
    path('add_product', views.add_product, name='add_product'),
    path('Report', views.Report, name='Report'),
    path('Setting', views.Setting, name='Setting'),
    path('product_list', views.product_list, name='product_list'),
    path('signup', views.index, name='index'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('profile', views.profile, name='profile'),
    path('create_campaign', views.create_campaign, name='create_campaign'),
    path('view_campaigns', views.view_campaigns, name='view_campaigns'),
    path('report', views.report, name='report'),
    path('search', views.search_view, name='search'),
    path('setting', views.setting, name='setting'),
    path('notification', views.notification, name='notification'),


]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)