from django import forms

class BanterEntry(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    story = forms.CharField(label='Story',widget=forms.Textarea)
    author = forms.CharField(label='Author', max_length=100)

    def is_valid(self):
        #TODO: proper is valid check
        return True