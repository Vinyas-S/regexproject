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
from django.urls import  url,include,re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from items import views as item_views
# from items import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path(r'^accounts/login/$', auth_views.LoginView,{'template_name': 'login.html'}, name="login"),
    url(r'^accounts/logout/$', auth_views.LogoutView, name='logout'),
    url(r'^items/', include('items.urls')),
    url(r'^signup/$', item_views.sign_up, name='sign_up'),
    url(r'^$', RedirectView.as_view(url='/items/', permanent=True)),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
