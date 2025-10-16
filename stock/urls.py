from django import path
from stock.views import SaleRequestListCreate , SaleRequestRetrieveUpdateDestroy

urlpatterns = [
    path('sale-request-list-create' , SaleRequestListCreate.as_view()),
    path('sale-request-retrieve-destroy-update/<str:pk>' , SaleRequestRetrieveUpdateDestroy.as_view())
]