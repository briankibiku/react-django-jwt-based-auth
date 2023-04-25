from django.contrib import admin
from django.urls import path, include
# import views from todo
from .views import TodoView

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers

# create a router object
router = routers.DefaultRouter()
router.register(r'tasks',TodoView, 'task')

urlpatterns = [
    path("", include(router.urls)),
]
