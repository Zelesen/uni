# products/forms.py
from django import forms
from .models import Product
from .models import Campaign

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        
        fields = ['name', 'price', 'description', 'city', 'state', 'country']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'description-textarea',
                'placeholder': 'Enter product description here...'
            }),
        }



class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['campaign_name', 'audience', 'campaign_type', 'campaign_goal', 'advertisement_type', 'advertisement_text', 'ad_file']

                                                                         