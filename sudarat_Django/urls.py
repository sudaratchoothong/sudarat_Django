from django.contrib import admin
from django.urls import path,include
from sudarat_app import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sudarat_app.urls')),
   
]

handler404 = 'sudarat_app.views.handler404'
# handler500 = 'sudarat_app.views.handler500'