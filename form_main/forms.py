from django.forms import ModelForm
from . import models

class LeadForm(ModelForm):
    class Meta:
        model = models.Lead
        fields = '__all__'
        exclude = ['created_at','updated_at']
        