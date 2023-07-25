"""
URL configuration for superEcommerceDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from. import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='homepage'),
    path('addproduct/', user_views.addproduct, name='addproduct'),
    path('products/', user_views.all_products, name='proddisplay'),
    path('del-prod/<id>', user_views.delete_product, name='delete-prod'),
    path('update-product/<id>', user_views.update_product, name='upd-prod'),
    path('register/', user_views.register, name='reg-user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='user-logout')
]