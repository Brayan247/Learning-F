from django.urls import path
from .views_admin import *

urlpatterns = [
    # admin views
    path('mensaje/', MensajeList.as_view()),
    path('mensajeerrores/', MensajesErroresList.as_view()),
]
