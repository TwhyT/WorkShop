from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('productlist', views.productlist, name='productlist'),
    path('detail/<slug:slug>', views.detail, name='detail'), 
    path('contact', views.Contact, name = 'contact'),
    path('about', views.about, name='about'),

    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)