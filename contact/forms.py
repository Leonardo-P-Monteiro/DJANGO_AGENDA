from django import forms
from . import models
from django.core.exceptions import ValidationError




class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'class-a class-b',
                'placeholder': 'Text of orientation.'
                  }
        ),
        label= 'Primeiro Nome',
        help_text= 'Text of orientation.'
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class-a class-b',
        #             'placeholder': 'Text of orientation.',
        #             }
        #         )
        # }
    
    
    
    
    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError('Mensagem de erro 1')
        )

        self.add_error(
            'last_name',
            ValidationError('Mensagem de erro 2')
        )

        return super().clean()