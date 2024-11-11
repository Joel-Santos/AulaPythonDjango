from django.urls import path
from .views import ProdutoListCreateView, ProdutoRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProdutoListCreateView.as_view(), name='produto-list-create'),
    path('<int:pk>/', ProdutoRetrieveUpdateDestroyView.as_view(), name='produto-detail'),
]
