from django.urls import path, include, re_path
from django.views.generic import TemplateView
from notes.views import NoteList
from .views import ClientList, ClientDetail, DealList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/', include('api.urls')),
    path('notes/', NoteList.as_view(), name='note-list'),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('deals/', DealList.as_view(), name='deal-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='home'),
]
