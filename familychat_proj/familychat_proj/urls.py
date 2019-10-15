
from django.contrib import admin

from django.urls import path,re_path,include
from familychat_proj.settings import DEBUG 

from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from django.contrib.auth.decorators import login_required

# admin_url = include('settings.urls')

# if DEBUG == False:
#     admin_url = admin.site.urls
    

urlpatterns = [
    # re_path(r'^',include('api.urls')),
    path("",
        TemplateView.as_view(template_name="application.html"),
        name="app",
    ),    

    path('admin/', admin.site.urls),
    re_path(r'^auth/obtain_token/', obtain_jwt_token),
    re_path(r'^auth/refresh_token/', refresh_jwt_token),
    re_path(r'^api/',include('api.urls')),
    
     
]