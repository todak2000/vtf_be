from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("auth", views.test_auth),
    path("isaca-events", views.isaca_events),
    path("vtf-speaker-signup", views.speaker_signup),
]
