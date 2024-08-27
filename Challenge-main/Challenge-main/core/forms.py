from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Clientes, Setores, AcervoVideos


class ClienteForm(UserCreationForm):
    nome = forms.CharField(max_length=255)
    setor = forms.ModelChoiceField(queryset=Setores.objects.all())
    data_de_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'format': '%Y-%m-%d'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        cliente, created = Clientes.objects.update_or_create(
            usuario=user,
            defaults={
                'nome': self.cleaned_data['nome'],
                'data_de_nascimento': self.cleaned_data['data_de_nascimento'],
                'setor': self.cleaned_data['setor']
            }
        )

        cliente.save()

        return user


class AcervoVideoForm(forms.ModelForm):
    class Meta:
        model = AcervoVideos
        exclude = ()

        widgets = {
            'nome_video': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'url_video': forms.URLInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
