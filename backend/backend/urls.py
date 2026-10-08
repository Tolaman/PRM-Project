from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
# This view are provided by the Simple JWT package and are used to obtain and refresh JSON Web Tokens (JWTs) 
# for user authentication.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('admin/', admin.site.urls),
  # When we go to this URL, it will call the CreateUserView class and handle the request to create a new user. 
  # The 'as_view()' method is used to convert the class-based view into a view function that can be called by 
  # Django's URL dispatcher.
  path("api/user/register/", CreateUserView.as_view(), name="register"),
  path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
  path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
  # this is used to provide a login and logout view for the browsable API. It allows users to authenticate 
  # themselves when using the API through a web browser.
  path("api-auth/", include("rest_framework.urls")), 
]
