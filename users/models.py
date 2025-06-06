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
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields["is_staff"] = True  # Forzar que is_staff sea True
        extra_fields["is_superuser"] = True  # Forzar que is_superuser sea True
        return self.create_user(email, password, **extra_fields)


class UserSimple(models.Model):
    """Usuarios básicos sin necesidad de email ni contraseña."""
    
    usernom = models.CharField(verbose_name="Nombre", db_column='UserNom', max_length=60, blank=False)
    userape = models.CharField(verbose_name="Apellidos", db_column='UserApe', max_length=60, blank=False)
    userdocide = models.CharField(verbose_name="Documento de identidad", db_column='UserDocIde', max_length=50, blank=False, unique=True)
    usercodosh = models.CharField(verbose_name="Código Osha Institute", db_column='UserCodOsh', max_length=9, blank=True, null=True, unique=True)
    userpai = models.CharField(verbose_name="Pais", db_column='UserPai', max_length=50, blank=True, null=True, default='')
    userciu = models.CharField(verbose_name="Ciudad", db_column='UserCiu', max_length=50, blank=True, null=True, default='')
    userdir = models.CharField(verbose_name="Dirección", db_column='UserDir', max_length=100, blank=True, null=True, default='')
    
    def convertir_a_usuario(self, email, password):
        """Convierte esta instancia de UserSimple en un usuario que puede iniciar sesión."""
        if hasattr(self, 'estudianteuser'):
            raise ValueError("Este usuario ya tiene una cuenta de acceso.")
        # Crear el usuario con acceso a la plataforma
        usuario = EstudianteUser.objects.create_user(
            usuario=self,  # Usa el UserSimple como PK
            email=email,
            password=password
        )
        return usuario
    
    def __str__(self):
        return f"{self.userdocide} - {self.usernom} {self.userape}"


class EstudianteUser(AbstractBaseUser, PermissionsMixin):
    """Usuarios que pueden iniciar sesión en la plataforma."""

    usuario = models.OneToOneField(
        UserSimple, on_delete=models.CASCADE, verbose_name="Usuario", db_column='User', unique=True, null=False
    )
    email = models.EmailField(verbose_name="Email", unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario']
    
    def get_full_name(self):
        return self.usuario.usernom + "" + self.usuario.userape
    
    def get_name(self):
        return self.usuario.usernom
    
    def __str__(self):
        return f"{self.email}"