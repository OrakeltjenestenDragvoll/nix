from django import forms

class PostForm(forms.Form):
    content = forms.CharField(label='content', max_length=500)
    category = forms.CharField(label='category')