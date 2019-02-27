from django import forms


class UserTextForm(forms.Form):
    Input_text = forms.CharField(label='',
                                 widget=forms.Textarea(attrs={
                                     'rows': 3,
                                     'style': "background-color:#BAB0B0",
                                     'class': "form-control",
                                     'id': "Text",
                                     }))








