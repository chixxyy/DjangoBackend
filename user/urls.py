from django.urls import path
from .views import register_user, login_user, get_data

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('get-data/', get_data, name='get_data'),
]
