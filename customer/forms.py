from django import forms
from .models import CustomeragetModel,CustomerdetailsModel,BillingModel

class CustomeragentForm(forms.ModelForm):
    class Meta:
        model=CustomeragetModel
        fields="__all__"
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'company_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}),
            'sales_team':forms.TextInput(attrs={'class':'form-control','placeholder':'Sales Team'}),
            'Email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Address','rows':'4','cols':'60'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
            'sendemail':forms.EmailInput(attrs={'class':'form-control','placeholder':'Send Email'}),

        }

class CustomerdetailsForm(forms.ModelForm):
    class Meta:
        model=CustomerdetailsModel
        fields="__all__"
        widgets={
            'company_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'website':forms.TextInput(attrs={'class':'form-control','placeholder':'Web site'}),
            'vat_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Vat Number'}),
            'address':forms.Textarea(attrs={'class':'form-control','style':'height:150px;'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'Country'})
        }

class BillingFrom(forms.ModelForm):
    class Meta:
        model=BillingModel
        fields="__all__"
        widgets={
            'street_billing':forms.TextInput(attrs={'class':'form-control','placeholder':'Street'}),
            'city_billing':forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'state_billing':forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
            'zip_code_billing':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip'}),
            'country_billing':forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),
        }