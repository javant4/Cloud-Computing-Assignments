from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    a = models.FloatField(
        verbose_name='coefficient of x^2 term', default=1)
    b = models.FloatField(
        verbose_name='coefficient of x term', default=2)
    c = models.FloatField(
        verbose_name='constant term', default=4)

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = "__all__"
    

    
