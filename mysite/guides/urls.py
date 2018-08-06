from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Contributors Page ex: /contribute/
    path('contributor', views.contributor, name='contributor'),
    # Funders Page ex: /fund/
    path('funder', views.funder, name='funder'),
]