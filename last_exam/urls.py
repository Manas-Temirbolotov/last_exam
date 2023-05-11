"""last_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

import account
import post
from account.views import AuthorRegisterView
from post import views as post_views
from account import views as account_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


account_router = DefaultRouter()
account_router.register('register', AuthorRegisterView)

post_router = DefaultRouter()
post_router.register('post', post_views.PostListCreateAPIView)
post_router.register('comment', post_views.CommentListCreateAPIView)

schema_view = get_schema_view(
    openapi.Info(
        title="exam API",
        default_version='v0.1',
        description="API для новостного сайта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),
    path('api/account/', include('account.urls')),
    path('api/post/', include('post.urls')),
    path('api/comment/', include('post.urls')),

    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
    path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),
]
