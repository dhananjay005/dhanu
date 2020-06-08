from django.contrib import admin

from supple.models import Registration,supplementsOrdered,Ask,Contact,Shipping
admin.site.register(Registration)
admin.site.register(supplementsOrdered)
admin.site.register(Ask)
admin.site.register(Contact)
admin.site.register(Shipping)

