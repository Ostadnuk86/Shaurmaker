from django.urls import path

from Bot import views

urlpatterns = [
    path('fgfhgfjhghsagfdhgfjfgsdfhghsdf', views.webhoock, name='webhoock'),
    path('setwebhoock', views.setwebhoock, name='setwebhoock')
]