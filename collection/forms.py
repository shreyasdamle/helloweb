from django.forms import ModelForm

from collection.models import Cryptocurrency

class CryptocurrencyForm(ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ('name', 'description',)
