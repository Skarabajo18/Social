from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('feed/', views.feed, name = 'feed'),
    # path('profile/<str:username>/', views.profile, name='profile'),
    # path('product/<int:id_product>/', views.view_product_post, name='view_product_post'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
