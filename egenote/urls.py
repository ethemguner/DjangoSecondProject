"""egenote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import users.urls
import notification.urls
import note.urls
from users.views import homepage, who_we_are
from note.views import list_notes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auths/', include(users.urls)),
    path('selling/', include(notification.urls)),
    path('note/', include(note.urls)),
    path('', list_notes , name= 'list-notes'),
    path('aboutus', who_we_are, name='who-we-are'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
