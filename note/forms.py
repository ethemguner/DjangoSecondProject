from django import forms

class NoteQueryForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control',
                                                                           'placeholder':'search a note'}), required=False)