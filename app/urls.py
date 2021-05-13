from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"root", views.RootAPI, 'root')
router.register(r"sub-group", views.SubGroupAPI, 'sub-group')
router.register(r"child", views.ChildAPI, 'child')
router.register(r"journal", views.JournalAPI, 'journal')
router.register(r"normally-journal", views.Normally_JournalAPI, 'normally-journal')

router.register(r"nested-root", views.RootNestedAPI, 'nested-root')
router.register(r"nested-sub", views.SubNestedAPI, 'nested-sub')
router.register(r"nested-child", views.ChildNestedAPI, 'nested-child')
router.register(r"nested-journal", views.JournalNestedAPI, 'nested-journal')
router.register(r"nested-normally-journal", views.Normally_JournalAPI, 'nested-normally-journal')





urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.test, name='test')
]
