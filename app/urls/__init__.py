from django.urls import path, include

urlpatterns = [
    path('', include('app.urls.auth')),
    path('', include('app.urls.admin')),
    path('', include('app.urls.teacher')),
    path('', include('app.urls.student')),
]
