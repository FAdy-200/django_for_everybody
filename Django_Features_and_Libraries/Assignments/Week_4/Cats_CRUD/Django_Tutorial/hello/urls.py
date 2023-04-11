from django.urls import path

from . import views
app_name = 'hello'
urlpatterns = [
    # ex: /hello/
    path('', views.IndexView.as_view(), name='index'),
]