from django import forms
from .models import CustomeragetModel

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