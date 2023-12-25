from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class RegistrarUsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ["nombre","apellido","username", "fecha_nacimiento", "password1", "password2", "email", "imagen"]

    @transaction.atomic
    def save(self):
        user =super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user