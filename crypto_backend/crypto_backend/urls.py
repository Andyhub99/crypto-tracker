from django.contrib import admin
from django.urls import path, include
from tracker.views import api_home   # <-- ADD THIS
from tracker.views import coin_ui  # <-- import your view here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')),
    path('', coin_ui, name="coin_ui"), 

    # HOME API at /
    path('', api_home),      # <-- ADD THIS
]
