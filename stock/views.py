from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView , RetrieveUpdateDestroyAPIView
from stock.models import Company , SaleRequest , BuyRequest
from stock.serializers import CompanySerializers , SaleRequestSerializers , BuyRequestSerializers

def check():
   SaleRequest_sorted = SaleRequest.objects.all().order_by("-price") 
   BuyRequest_sorted = BuyRequest.objects.all().order_by("price")
   for i in SaleRequest_sorted:
       for j in BuyRequest_sorted:
           if i <= j:
               BuyRequest.amount - SaleRequest.amount
               


class SaleRequestListCreate(ListAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializers
    
class SaleRequestRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializers
    
class BuyRequestCreate(CreateAPIView):
    queryset = BuyRequest.objects.all()
    serializer_class = BuyRequestSerializers
    
    