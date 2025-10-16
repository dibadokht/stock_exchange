from django import path
from stock.views import SaleRequestListCreate , SaleRequestRetrieveUpdateDestroy , BuyRequestCreate

urlpatterns = [
    path('sale-request-list-create' , SaleRequestListCreate.as_view()),
    path('sale-request-retrieve-destroy-update/<str:pk>' , SaleRequestRetrieveUpdateDestroy.as_view()),
    path('buy-request-create' , BuyRequestCreate.as_view())
]