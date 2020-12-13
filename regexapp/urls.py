"""bigbasket2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import  path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from items import views as item_views
# from items import urls

urlpatterns = [
    path(r'admin/', admin.site.urls),

    path(r'items/', include('items.urls')),
    path(r'signup/', item_views.sign_up, name='sign_up'),
    path(r'^$',RedirectView.as_view(url='/items/', permanent=True)),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)