from django.contrib import admin
from stock.models import Company , BuyRequest , SaleRequest

admin.site.register(Company)
admin.site.register(BuyRequest)
admin.site.register(SaleRequest)
