from django.forms import ModelForm, TextInput, Textarea
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model=News
        fields=['titel_text','text_news']

        widgets={
            "titel_text": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Заголовок новости'
            }),
            "text_news": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'
            })
        }