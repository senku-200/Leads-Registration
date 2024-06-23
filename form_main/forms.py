from django import forms
from .models import Lead
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget 
class LeadForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=50, widget=forms.TextInput(attrs={'pattern': '[A-Za-z\s]{1,50}', 'title': 'Full name should only contain letters and spaces, maximum 50 characters'}))
    contact_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN')
    )
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
