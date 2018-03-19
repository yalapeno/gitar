"""gitar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
#  from rest_framework import routers
from rest_framework_nested import routers
from chords import views
from gitar import login_views


router = routers.DefaultRouter()
router.register(r"artist", views.ArtistViewSet)


artists_router = routers.NestedDefaultRouter(router, r"artist", lookup="artist")
artists_router.register(r"chord", views.ChordWithDataViewSet)
router.register(r"genre", views.GenreViewSet)


router.register(r"user", login_views.UserViewSet)
router.register(r"groups", login_views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include(router.urls)),
    url(r"^", include(artists_router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^o/", include("oauth2_provider.urls", namespace="oauth2_provider"))
]
