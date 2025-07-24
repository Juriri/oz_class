from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmarks/', include('bookmark.urls')),  # bookmark 앱 url 연결
]
