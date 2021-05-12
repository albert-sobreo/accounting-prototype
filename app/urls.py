from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"root", views.UserAPI, 'user')
router.register(r"sub-group", views.WorkAPI, 'work')
router.register(r"child", views.BugAPI, 'bug')

router.register(r"nested-sub", views.WorkNestedAPI, 'nested-work')
router.register(r"nested-child", views.BugNestedAPI, 'nested-bug')



urlpatterns = [
    path('', views.test, name='test')
]
