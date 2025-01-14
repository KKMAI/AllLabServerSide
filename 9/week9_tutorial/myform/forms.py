from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    descriptions = forms.CharField(
        label="About yourself", 
        max_length=500, 
        widget=forms.Textarea(attrs={"cols": 20, "rows": 5})
        )
    your_age = forms.IntegerField(label="Your age", initial=0)
    your_email = forms.EmailField(label="Your email", required=False)
    your_birthdate = forms.DateField(label="Your birthdate", widget=forms.TextInput(attrs={"type": 'date'}))
