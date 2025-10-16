from rest_framework.serializers import ModelSerializer
from stock.models import Company , SaleRequest , BuyRequest

class CompanySerializers(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
    
class SaleRequestSerializers(ModelSerializer):
    class Meta:
        model = SaleRequest
        fields = '__all__'
        
        
class BuyRequestSerializers(ModelSerializer):
    class Meta:
        model = BuyRequest
        fields = ['amount' , 'price']
        