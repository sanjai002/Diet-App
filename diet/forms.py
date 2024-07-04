from django import forms
from .models import *
from django.contrib.auth.models import User

from django import forms

class HeartDiseasePredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[('male', 'Male'), ('female', 'Female')])
    cp = forms.ChoiceField(label='Chest Pain Type', choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Anginal Pain'), (4, 'Asymptomatic')])
    trestbps = forms.IntegerField(label='Resting Blood Pressure')
    chol = forms.IntegerField(label='Cholesterol')
    fbs = forms.ChoiceField(label='Fasting Blood Sugar', choices=[(0, '< 120 mg/dl'), (1, '> 120 mg/dl')])
    restecg = forms.ChoiceField(label='Resting Electrocardiographic Results', choices=[(0, 'Normal'), (1, 'ST-T wave abnormality'), (2, 'Left ventricular hypertrophy')])
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved')
    exang = forms.ChoiceField(label='Exercise Induced Angina', choices=[(0, 'No'), (1, 'Yes')])
    oldpeak = forms.FloatField(label='ST Depression Induced by Exercise Relative to Rest')
    slope = forms.ChoiceField(label='Slope of the Peak Exercise ST Segment', choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Downsloping')])
    ca = forms.IntegerField(label='Number of Major Vessels Colored by Flourosopy')
    thal = forms.ChoiceField(label='Thalassemia', choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')])
