from django import forms
from .models import Task

class TaskForm(forms.ModelForm ):
    class Meta:
        model = Task
        fields= ['title','description','inportant']   
        widgets ={
                'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'write a Title'}),
                'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'write a description'}),
                'inportant': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'})
        }     