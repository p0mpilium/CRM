from django.urls import path
from myproject.views import UserRegistrationView
from django.urls import path, include

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/accounts/', include('accounts.urls')),
]