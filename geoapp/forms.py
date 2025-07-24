from django import forms
 
class ContinentForm(forms.Form):
    CONTINENTS = [
        ('Africa', 'Africa'),
        ('Americas', 'Americas'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('Oceania', 'Oceania'),
    ]
    continent = forms.ChoiceField(choices=CONTINENTS)