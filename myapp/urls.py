from django.urls import path
from . import views
from .views import IngredientesDetailView, IngredientesListView

urlpatterns = [
    # Lista ingredientes
    path('ingredientes/', IngredientesListView.as_view()),

    # Detalle de los ingredientes
    path('ingredientes/<int:pk>', IngredientesDetailView.as_view(), name='id'),
]