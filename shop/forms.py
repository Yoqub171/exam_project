from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'main_image', 'discount', 'category', 'quantity']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'email', 'rating', 'content']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your review'}),
        }
