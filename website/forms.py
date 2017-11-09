from django import forms

areas = forms.ChoiceField(max_length=50)

class AreaForm(ModelForm):
    allCars = forms.ModelChoiceField(queryset=areas.objects.all())