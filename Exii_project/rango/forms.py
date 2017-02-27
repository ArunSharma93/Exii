from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter a Category, bro")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)

    class Meta:
        model = Category
        fields = '__all__'


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(help_text="Please enter the URL of the page.", initial = 'http://www.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        fields = ('title', 'url', 'views')
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is non-empty and does not starts with http://, append one.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
