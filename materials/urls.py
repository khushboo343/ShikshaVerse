# materials/urls.py

from django.urls import path
from .views import IndexView, MaterialListView, MaterialSubmissionView, material_submission, material_search

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('material_list/', MaterialListView.as_view(), name='material_list'),
    path('material_submission/', MaterialSubmissionView.as_view(), name='material_submission'),
    path('material_submission_submit/', material_submission, name='material_submission_submit'),
    path('material_search/', material_search, name='material_search'),
]
