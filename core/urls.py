from django.urls import path,include
from . import views


from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'
urlpatterns = [
    path('', views.core_home , name = "core_home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)