"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label = 'Ваш город', min_length=2, max_length=100)    
    mark = forms.ChoiceField(label = 'Оцените качество услуг', choices=[('1', 'Плохое'), ('2', 'Среднее'), ('3', 'Хорошее')], widget=forms.RadioSelect, initial=1)
    message = forms.CharField(label = 'Ваше впечатление от использования сервиса', widget=forms.Textarea(attrs={'rows':12, 'cols':40}))


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text


class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog # используемая модель
        fields = ('title', 'description', 'content', 'image',) # заполняемые поля
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"} # метки к полям
