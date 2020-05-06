from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('location', 'image', 'caption')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = 'Upload image'
        self.fields['image'].widget.attrs['class'] = 'img'
        self.fields['location'].widget.attrs['class'] = 'img'
        self.fields['caption'].widget.attrs['class'] = 'img'
