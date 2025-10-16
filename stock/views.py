from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView , RetrieveUpdateDestroyAPIView
from stock.models import Company , SaleRequest , BuyRequest
from stock.serializers import CompanySerializers , SaleRequestSerializers , BuyRequestSerializers

class SaleRequestListCreate(ListAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializers
    
class SaleRequestRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializers