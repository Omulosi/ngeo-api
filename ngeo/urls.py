"""ngeo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include, re_path
from ngeo.apps.libs.exception_handler import not_found

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
handler404 = not_found

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"api/v1/", include("ngeo.apps.account.urls")),
    re_path(r"api/v1/", include("ngeo.apps.agents.rest_api.urls")),
    re_path(r"api/v1/", include("ngeo.apps.projects.rest_api.urls")),
    re_path(r"api/v1/", include("ngeo.apps.field_officer.rest_api.urls")),
    re_path(r"api/v1/", include("ngeo.apps.shapefiles.rest_api.urls")),
    re_path(r"api/v1/", include("ngeo.apps.incidence.rest_api.urls")),
]


# enable serve static by django for local development
if settings.DEBUG:  # noqa
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# enable debug_toolbar for local development (if installed)
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

