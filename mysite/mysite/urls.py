from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

def redirect_root(request):
    return HttpResponseRedirect("/polls/")  # Redirects to polls app

urlpatterns = [
    path("", include("polls.urls")),  # Main app
    path("admin/", admin.site.urls),  # Admin panel
    path("accounts/", include("django.contrib.auth.urls")),  # Login/logout views
    
    
]

