"""bitpocket URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from bitpocket.views import PlayView

urlpatterns = [
    url(r'', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^secret/', login_required(TemplateView.as_view(template_name="secret.html")), name='secret'),
    url(r'^play/', login_required(PlayView.as_view()), name='play'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
