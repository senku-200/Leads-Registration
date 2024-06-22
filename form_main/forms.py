from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name', 'company_name', 'email', 'contact_number', 'service_description', 'category', 'custom_category']
        widgets = {
            'custom_category': forms.TextInput(attrs={'style': 'display:block;', 'id': 'custom-category-input'})
        }
        help_texts = {
            'custom_category': 'Please specify your category if you selected "Others".',
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        custom_category = cleaned_data.get("custom_category")

        if category == 'Others' and not custom_category:
            self.add_error('custom_category', "This field is required when 'Others' is selected.")
        return cleaned_data
