from .models import About
from django.forms import ModelForm, TextInput, Textarea

# class ServicesForm(ModelForm):
#     class Meta:
#         model = Title_for_section
#         fields = ["titlePrice", "price"]
#         widgets = {
#             "titlePrice": TextInput(attrs={
#                 "class": "form-control",
#                 'placeholder': "Введите название"
#             }),
#             "price": Textarea(attrs={
#                 "class": "form-control",
#                 'placeholder': "Введите описание"
#             }),
            
#         }

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