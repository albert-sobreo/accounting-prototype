from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"root", views.RootAPI, 'user')
router.register(r"sub-group", views.SubGroupAPI, 'work')
router.register(r"child", views.ChildAPI, 'bug')

router.register(r"nested-root", views.RootNestedAPI, 'nested-root')
router.register(r"nested-sub", views.SubNestedAPI, 'nested-work')
router.register(r"nested-child", views.ChildNestedAPI, 'nested-bug')



urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.test, name='test')
]
