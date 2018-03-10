from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^my/set/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
