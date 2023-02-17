
from django import forms
from django.forms import CharField, EmailField

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError('Invalid Last Name')
    return value


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # fields=['first_name', 'last_name', 'email']
        fields = '__all__'
        labels = {
            'first_name':_('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email')
        }
        help_texts={'first_name':_('Enter characters only')}
        error_messages={
            'first_name':{
                'required':_('You cannot move forward without first name.')
            }
        }




# class SubscribeForm(forms.Form):
#     first_name = CharField(max_length=100, label="Enter First Name")
#     last_name = CharField(max_length=100, validators=[validate_comma], label="Enter Last Name")
#     email = EmailField(max_length=100, validators=[validate_comma], label="Enter Email")
#
#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError('Invalid first name')
#         return data

