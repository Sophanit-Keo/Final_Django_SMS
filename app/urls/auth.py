from django.urls import path
from app.view import login, logout

urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
]
