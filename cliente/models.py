from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey 

class Departamento(models.Model):
    departamento=models.CharField(_("Departamento"), max_length=50)
    codDepartamento=models.CharField(max_length=2)
    def __str__(self):
        return self.departamento

class Provincia(models.Model):
    provincia=models.CharField(max_length=50)
    departamento=models.ForeignKey(Departamento,verbose_name="Provincia", on_delete=models.CASCADE)
    codProvincia=models.CharField(max_length=2)
    def __str__(self):
        return self.provincia

class Distrito(models.Model):
    distrito=models.CharField(max_length=50)
    provincia=models.ForeignKey(Provincia,verbose_name="Distrito", on_delete=models.CASCADE)
    codDistrito=models.CharField(max_length=2)

    def __str__(self):
        return self.distrito

class CustomClienteManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('El email es requerido!')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('dni', "12345678")
        # extra_fields.setdefault('celular', "123456789")
        # extra_fields.setdefault('fechanac', "19-06-97")

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomCliente(AbstractUser):
    username=None
    email=models.EmailField(_("Email"),unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomClienteManager()
    dni=models.CharField(verbose_name="DNI",max_length=8,blank=False)
    celular=models.CharField(verbose_name="Celular",max_length=9,blank=False)
    fechanac=models.DateField(verbose_name="Fecha de nacimiento",null=True)
    def __str__(self):
        return self.email
class Domicilio(models.Model):
    cliente=models.ForeignKey(CustomCliente,verbose_name="Cliente", on_delete=models.CASCADE)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    celular=models.CharField(max_length=8)
    departamento=models.ForeignKey(Departamento,verbose_name="departamento", on_delete=models.CASCADE)
    provincia = ChainedForeignKey (
        Provincia,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=False,
        sort=True)
    distrito = ChainedForeignKey (
        Distrito,
        chained_field="provincia",
        chained_model_field="provincia",
        show_all=False,
        auto_choose=False,
        sort=True)
    # provincia=models.ForeignKey(Provincia,verbose_name="Provincia", on_delete=models.CASCADE)


    # distrito=models.ForeignKey(Distrito,verbose_name="Distrito", on_delete=models.CASCADE)
    direccion=models.CharField(max_length=120)
 
    referencia=models.CharField(max_length=90)


    def __str__(self):
        return self.direccion

