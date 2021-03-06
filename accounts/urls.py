from django.urls import path
from .views import CustomAuthToken
from . import views


app_name = "account"

urlpatterns = [
    path('signup/', views.sign_up, name="register"),
    path('signin/', CustomAuthToken.as_view(), name="login"),
    path('logout/', views.sign_out, name="logout"),
    path('get-user/<int:id>', views.get_user, name="get_user"),
    path('update-user/<int:id>', views.update_user, name="update_user"),
    path('delete-user/<int:id>', views.delete_user, name="delete_user"),
    path('upload-image/<int:id>', views.upload_image, name="upload_image"),
    path('favourite-restaurant/<int:user_id>/<int:restaurant_id>', views.favourite_restaurant, name="favourite_restaurant"),
    path('unfavourite-restaurant/<int:user_id>/<int:restaurant_id>', views.unfavourite_restaurant, name="unfavourite_restaurant"),
    path('request-ownership/<int:user_id>/<int:restaurant_id>', views.request_ownership, name="request_ownership"),
    path('get-request/', views.get_request, name="get_request"),
    path('accept-request/<int:user_id>/<int:restaurant_id>', views.accept_request, name="accept_request"),
    path('delete-request/<int:id>', views.delete_request, name="delete_request")

]


