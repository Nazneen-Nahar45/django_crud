"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from newapp import views as s_view
urlpatterns = [
path('admin/', admin.site.urls),
path('', s_view.index,name='index'),
path('add/', s_view.add,name='add'),
path('addrec/',s_view.addrec,name='addrec'),
path('delete/<int:id>/', s_view.delete, name='delete'),
path('update/<int:id>/', s_view.update, name='update'),
path('update/uprec/<int:id>/', s_view.uprec, name='uprec'),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)