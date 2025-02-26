from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()#user.save(using=self._db)
        return user
    
    #def create_superuser(self, email, password=None, **extra_fields):
    #    extra_fields["is_staff"] = True  # Forzar que is_staff sea True
    #    extra_fields["is_superuser"] = True  # Forzar que is_superuser sea True
    #    return self.create_user(email, password, **extra_fields)


class EstudianteUser(AbstractBaseUser, PermissionsMixin): #UserAccount
    USER_TYPES = [
        ('ADMIN', 'Administrador'),
        ('PROF', 'Profesor'),
        ('STUD', 'Estudiante'),
    ]
    email = models.EmailField(verbose_name="Email", unique=True)
    
    usernom = models.CharField(verbose_name="Nombre", db_column='EstUserNom', max_length=60, blank=False)
    userape = models.CharField(verbose_name="Apellidos", db_column='EstUserApe', max_length=60, blank=False)
    userdocide = models.CharField(verbose_name="Documento de identidad", db_column='EstUserDocIde', max_length=50, blank=False, unique=True)
    usercodosh = models.CharField(verbose_name="Código Osha Institute", db_column='EstUserCodOsh', max_length=9, blank=True, null=True, unique=True)
    userpai = models.CharField(verbose_name="Pais", db_column='EstUserPai', max_length=50, blank=True, null=True)
    userciu = models.CharField(verbose_name="Ciudad", db_column='EstUserCiu', max_length=50, blank=True, null=True)
    userdir = models.CharField(verbose_name="Dirección", db_column='EstUserDir', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usernom']
    
    def get_full_name(self):
        return self.usernom + "" + self.userape
    
    def get_name(self):
        return self.usernom
    
    def __str__(self):
        return self.usernom + " " + self.userape + " - " + self.userdocide
