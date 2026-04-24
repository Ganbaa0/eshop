from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Имэйл'}))
    first_name = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Нэр'}))
    last_name = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Овог'}))
 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
 
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Нэвтрэх нэр'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Нэвтрэх нэр 50 тэмдэгтээс бага байх ёстой. Үсэг, цифр болон @/./+/-/_ тэмдэгтүүдийг ашиглаж болно.</small></span>'
 
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Нууц үг'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Нууц үг 8 тэмдэгтээс багагүй байх ёстой. Нууц үг нь цифр, жижиг болон том үсэг, болон тусгай тэмдэгтүүдийг агуулсан байх ёстой.</small></span>'
 
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Нууц үг давтах'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Нууц үгийг дахин оруулна уу.</small></span>'
 