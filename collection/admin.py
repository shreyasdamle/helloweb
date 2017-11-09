from django.contrib import admin

# Register your models here.

# import your model
from collection.models import Cryptocurrency

# set up automated slug creation
class CryptocurrencyAdmin(admin.ModelAdmin):
    model = Cryptocurrency
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Cryptocurrency, CryptocurrencyAdmin)
