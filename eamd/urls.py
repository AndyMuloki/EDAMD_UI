from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room),
    path('cnn/', include('cnn.urls'))
]
