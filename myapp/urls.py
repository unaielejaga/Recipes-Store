from django.urls import path
from . import views
from .views import IngredientesDetailView, IngredientesListView, RecetasDetailView, RecetasListView, TiposListView

urlpatterns = [
    # Lista ingredientes
    path('ingredientes/', IngredientesListView.as_view()),

    # Detalle de los ingredientes
    path('ingredientes/<int:pk>', IngredientesDetailView.as_view(), name='id'),
    
    path('tipos/', TiposListView.as_view()),

    path('recetas/', RecetasListView.as_view()),
    path('recetas/<int:pk>', RecetasDetailView.as_view(), name = 'id'),
]
