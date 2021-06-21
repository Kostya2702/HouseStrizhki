from django.db.models.fields import CharField
from django.db.models.query import QuerySet
from django.forms import fields, MultiValueField
from django.forms.widgets import MultiWidget, TextInput
from .models import *
from django import forms
from django.contrib.admin import widgets
from attr import attrs

# class PhoneWidget(MultiWidget):
#     def __init__(self, code_length=3, num_length=7, attrs=None):
#         widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length}),
#                     TextInput(attrs={'size': num_length, 'maxlength': num_length})]
#         super(PhoneWidget, self).__init__(widgets, attrs)

#     def decompress(self, value):
#         if value:
#             return [value.code, value.number]
#         else:
#             return ['', '']

#     def format_output(self, rendered_widgets):
#         return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]


# class PhoneField(MultiValueField):
#     def __init__(self, code_length, num_length, *args, **kwargs):
#         list_fields = [CharField(),
#                        CharField()]
#         super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

#     def compress(self, values):
#         return '+7' + values[0] + values[1]


class NoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choiceServ'].empty_label = 'Услуга не выбрана'
        self.fields['choiceMaster'].empty_label = 'Мастер не выбран'

    nameUser = forms.CharField(label='Имя', max_length=30)
    phoneNumber = forms.CharField(label='Номер телефона',min_length=10 , max_length=11)
    calendar = forms.SplitDateTimeField(label='Календарь',
                                          input_date_formats=['%d.%m.%Y'],
                                          input_time_formats=['%H:%M:%S'],
                                          widget=widgets.AdminSplitDateTime())
                                       
    class Meta:
        model = ChooceServ
        fields = '__all__'
        # widgets = {
        #     'choiceServ': fields.MultipleChoiceField(attrs={'class': 'formitem'})
        # }


    