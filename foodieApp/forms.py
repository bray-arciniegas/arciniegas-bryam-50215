from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones', 'imagen']

class CoctelForm(forms.ModelForm):
    class Meta:
        model = Coctel
        fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones', 'imagen']

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['titulo', 'contenido']

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen']

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['username'].help_text = ''
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class CustomUserChangeForm(UserChangeForm):
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')

    def save(self, commit=True):
        user = super().save(commit=False)
        avatar = self.cleaned_data.get('avatar')

        if avatar:
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user, avatar=avatar)
            else:
                user.userprofile.avatar = avatar
                user.userprofile.save()

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']