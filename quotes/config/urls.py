from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    path('youtube/', include('youtube.urls')),
    path('quotes/', include('quotes.urls')),
    path('', include('pages.urls')),


]
