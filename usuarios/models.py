from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    def create_user(self, carnet, nombre, apellidos, contraseña=None, **extra_fields):
        if not carnet:
            raise ValueError('El usuario debe tener un carnet')
        if not extra_fields.get('username'):
            raise ValueError('El usuario debe tener un nombre de usuario')

        user = self.model(
            carnet=carnet,
            nombre=nombre,
            apellidos=apellidos,
            **extra_fields
        )
        user.set_password(contraseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, carnet, nombre, apellidos, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(carnet, nombre, apellidos, contraseña, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, help_text="Nombre de usuario único")
    carnet = models.CharField(max_length=50, unique=True, default='SIN_CARNET')
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)

    direccion = models.TextField(default='Dirección por defecto')
    telefono = models.CharField(max_length=15, default='0000000000')
    fecha_nacimiento = models.DateField(default=timezone.now)
    fecha_registro = models.DateField(default=timezone.now)

    tutor = models.JSONField(null=True, blank=True, default=dict)
    domicilio = models.CharField(max_length=255, default='Domicilio por defecto')
    rol = models.CharField(max_length=100, default='Rol por defecto')
    ocupacion = models.TextField(null=True, blank=True)
    parentesco = models.CharField(max_length=100, null=True, blank=True)

    # Requeridos por Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['carnet', 'nombre', 'apellidos']

    class Meta:
        db_table = "usuario"

    def __str__(self):
        return f"{self.username} - {self.nombre} {self.apellidos}"
