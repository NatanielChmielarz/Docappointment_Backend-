

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('user_app.api.urls')),
    path('specialization/',include('specialization.api.urls')),
    
]