from django import forms
from .models import CategoryModel,SubcategoryModel,ItemModel,StatusModel

class categoryform(forms.ModelForm):
    category_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    category_description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'cols':'4',
        'rows':'8'
    }))
    choices=(('Active','Active'),('Inactive','Inactive'))
    category_status = forms.CharField(max_length=30,widget=forms.Select(choices=choices,attrs={
        'class':'form-control'
    }))

    class Meta:
        model = CategoryModel
        fields = "__all__"

class SubCategoryForm(forms.ModelForm):

    class Meta:
          model =SubcategoryModel
          fields ="__all__"
          data=CategoryModel.objects.all()
          choices=(('Active','Active'),('Inactive','Inactive'))
          widgets={
              'subcategory_name':forms.TextInput(attrs={'class':'form-control'}),
              'category_name':forms.Select(choices=data,attrs={'class':'form-control'}),
              'sub_category_description':forms.Textarea(attrs={'class':'form-control','rows':8,'cols':100}),
              'sub_category_status':forms.Select(choices=choices,attrs={'class':'form-control','style':'width: 405%;'})
          }


class ItemForm(forms.ModelForm):


    class Meta:
        model =ItemModel
        fields ="__all__"
        value=SubcategoryModel.objects.all()
        widgets={
            'itemcategory_name':forms.Select(attrs={'class':'category form-control'}),
            'itemsubcategory_name':forms.Select(choices=value,attrs={'class':'sub_category form-control'}),
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class StatusForm(forms.ModelForm):

    class Meta:
        model=StatusModel
        fields="__all__"
        widgets={
            'quantity_on_hand':forms.NumberInput(attrs={'class':'form-control'}),
            'purchase_price':forms.NumberInput(attrs={'class':'form-control'}),
            'sales_price':forms.NumberInput(attrs={'class':'form-control'})
        }

 
