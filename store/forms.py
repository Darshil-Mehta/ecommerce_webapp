from django import forms
from .models.customer import Customer
from .models.profile import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']