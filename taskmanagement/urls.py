from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', include('main.urls'), name='main'),
    path('task/', include('task.urls')),
    path('admin/', admin.site.urls),
]

