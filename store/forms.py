from django import forms
from .models.customer import Customer
from .models.profile import Profile
from .models.feedback import Feedback

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['product_name', 'problem_issue']