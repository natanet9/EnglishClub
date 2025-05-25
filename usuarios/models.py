from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, carnet, nombre, apellidos, contrseña=None, **extra_fields):
        if not carnet:
            raise ValueError('El usuario debe tener un carnet')
        user = self.model(
            carnet=carnet,
            nombre=nombre,
            apellidos=apellidos,
            **extra_fields
        )
        user.set_password(contrseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, carnet, nombre, apellidos, contrseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(carnet, nombre, apellidos, contrseña, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    carnet = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.BigIntegerField()
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(default=timezone.now)
    hijo = models.JSONField(null=True, blank=True)
    domicilio = models.CharField(max_length=255)
    rol = models.CharField(max_length=100)
    ocupacion = models.TextField(null=True, blank=True)
    parentesco = models.CharField(max_length=100, null=True, blank=True)

    # Requeridos por Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'carnet'
    REQUIRED_FIELDS = ['nombre', 'apellidos']

    class Meta:
        db_table = "usuario"

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.carnet})"
