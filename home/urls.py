from django.urls import path

from .views import homepage, dashboard


urlpatterns = [
    path('', homepage, name='home'),
    path('dashboard/', dashboard, name='dashboard')
]
