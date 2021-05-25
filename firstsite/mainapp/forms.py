from .models import About, Services
from django.forms import ModelForm, TextInput, Textarea

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ["titlePr", "price"]
        widgets = {
            "titlePr": TextInput(attrs={
                "class": "form-control",
                'placeholder': "Введите название"
            }),
            "price": Textarea(attrs={
                "class": "form-control",
                'placeholder': "Введите описание"
            }),
            
        }

# class AboutUsForm(ModelForm):
#     class Meta:
#         model = About
#         fields = ["noteAbout"]
#         widgets = {
#             "noteAbout": TextInput(attrs={
#                 "class": "form-control",
#                 'placeholder': "Начни писать"
#             })
#         }