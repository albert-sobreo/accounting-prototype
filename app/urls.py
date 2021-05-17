from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r"root", views.RootAPI, 'root')
router.register(r"sub-group", views.SubGroupAPI, 'sub-group')
router.register(r"child", views.ChildAPI, 'child')
router.register(r"journal", views.JournalAPI, 'journal')
router.register(r"journal-entries", views.JournalEntriesAPI, 'normally-journal')

router.register(r"nested-root", views.RootNestedAPI, 'nested-root')
router.register(r"nested-sub", views.SubNestedAPI, 'nested-sub')
router.register(r"nested-child", views.ChildNestedAPI, 'nested-child')
router.register(r"nested-journal", views.JournalNestedAPI, 'nested-journal')
router.register(r"nested-journal-entries", views.JournalEntriesNestedAPI, 'nested-journal-entries')
router.register(r"nested-journal-entries-child", views.JournalEntriesNestedChildAccountAPI, 'nested-journal-entries-child')
router.register(r"ledger", views.LedgerAPI, 'ledger-api')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.chartOfAccounts, name='chartOfAccounts'),
    path('journal/', views.journalView, name='journalView'),
    path('save-journal/', views.SaveJournalAPI.as_view()), 
    path('ledger/', views.ledgerView, name="ledger"),
    path('test/', views.testView, name='test')
]
