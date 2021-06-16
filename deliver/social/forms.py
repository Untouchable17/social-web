from django import forms
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

from social.models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Write a new blog..'
        }))

    class Meta:
        model = Post
        fields = ['title', 'body', 'photo']

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) > 200:
            raise ValidationError("The length mustn't exceed 200 characters")
        return title

    def clean_slug(self):
        self.slug = slugify(self.name)
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create" ')
        return new_slug


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Write a new comment..'
        }))

    class Meta:
        model = Comment
        fields = ['comment']


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=800)