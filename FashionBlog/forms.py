from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list =[]

for item in choices:
    choice_list.append(item)
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}), 
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'author', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }