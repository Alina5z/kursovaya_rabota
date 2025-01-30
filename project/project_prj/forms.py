from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "manufacturer", "price", "square"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "manufacturer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производитель'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "square": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
        }