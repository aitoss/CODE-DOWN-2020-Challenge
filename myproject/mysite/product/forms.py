from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title of product'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Enter the price'}))
    summary = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the summary'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter the Email'}))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
            # 'password'
        ]

        # widgets = {
        #    'password': forms.PasswordInput()
        # }

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'The Power of your Subconscious Mind' not in title:
            raise forms.ValidationError('This is not a valid title')
        if 'Think and Grow Rich' not in title:
            raise forms.ValidationError('This is not a valid title')
        if 'Word Power Made Easy' not in title:
            raise forms.ValidationError('This is not valid title')
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('com'):
            raise forms.ValidationError('This is an Invalid Email address')
        return email


class RawProductForm(forms.Form):
    # It is optional->attrs help us to perform the task of html such as adding class name or id or placeholder and
    # many more
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title of product'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Enter the price'}))
    summary = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the summary'}))
