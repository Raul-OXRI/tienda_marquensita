from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar contraseña')
    
    class Meta:
        model = Cliente
        fields = [
            'nombre_client', 
            'apellido_client', 
            'correo_client', 
            'telefono_client', 
            'direccion_client', 
            'password', 
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', 'Las contraseñas no coinciden')
        
        return cleaned_data
