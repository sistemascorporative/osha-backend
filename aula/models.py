from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
#from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class EstadoRegistro(models.Model):
    estregcod = models.AutoField(verbose_name="Codigo", db_column='EstRegCod', primary_key=True)
    estregnom = models.CharField(verbose_name="Nombre", db_column='EstRegNom', max_length=40, blank=False)
    
    class Meta:
        db_table = 'estado_registro'
        managed = True
        verbose_name = 'EstadoRegistro'
        verbose_name_plural = 'EstadosRegistro'
    
    def __str__(self):
        return self.estregnom


#class UserAccountManager(BaseUserManager):
#    def create_user(self, email, password=None, **extra_fields):
#        if not email:
#            raise ValueError('Users must have an email address')

#        email = self.normalize_email(email)
#        user = self.model(email=email, **extra_fields)

#        user.set_password(password)
#        user.save()

#        return user
    
#    def create_superuser(self, email, password=None, **extra_fields):
#        if not email:
#            raise ValueError('Users must have an email address')

#        email = self.normalize_email(email)
#        user = self.model(email=email, **extra_fields)

#        user.set_password(password)
#        user.save()

#        return user

"""
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country', 'city', 'address']

    def __str__(self):
        return self.email"""

#class EstudianteUser(AbstractBaseUser, PermissionsMixin):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #estcod = models.AutoField(verbose_name="Codigo", db_column='EstCod', primary_key=True)
#    estnom = models.CharField(verbose_name="Nombre", db_column='EstNom', max_length=60, blank=False)
#    estape = models.CharField(verbose_name="Apellidos", db_column='EstApe', max_length=60, blank=False)
#    estdocide = models.CharField(verbose_name="Documento de identidad", db_column='EstDocIde', max_length=50, blank=False)
#    estema = models.EmailField(verbose_name="Email", db_column='EstEma', max_length=255, unique=True)
#    estpai = models.CharField(verbose_name="Pais", db_column='EstPai', max_length=50, blank=True)
#    estciu = models.CharField(verbose_name="Ciudad", db_column='EstCiu', max_length=50, blank=True)
#    estdir = models.CharField(verbose_name="Direccion", db_column='EstDir', max_length=100, blank=True)
    #estfeccre = models.DateTimeField(db_column='EstFecCre', default=timezone.now, editable=False)
    #estfecmod = models.DateTimeField(db_column='EstFecMod', default=timezone.now)
#    estestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstEstReg', default=1)
    #is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)
    
    #objects = EstudianteUserManager()
    
    #USERNAME_FIELD = 'estema'
    #REQUIRED_FIELDS = ['estnom', 'estape']

    #class Meta:
##        db_table = 'estudiante_user'
#        managed = True
#        verbose_name = 'EstudianteUser'
#        verbose_name_plural = 'EstudiantesUsers'
#    
#    def get_full_name(self):
#        return self.estnom + " " + self.estape

#    def get_short_name(self):
#        return self.estnom
    
#    def __str__(self):
#        return self.estnom + " " + self.estape + " - " + self.estdocide


class Estudiante(models.Model):
    estcod = models.AutoField(verbose_name="Codigo", db_column='EstCod', primary_key=True)
    estnom = models.CharField(verbose_name="Nombre", db_column='EstNom', max_length=60, blank=False)
    estape = models.CharField(verbose_name="Apellidos", db_column='EstApe', max_length=60, blank=False)
    estdocide = models.CharField(verbose_name="Documento de identidad", db_column='EstDocIde', max_length=50, blank=False)
    estema = models.EmailField(verbose_name="Email", db_column='EstEma', max_length=255, unique=True)
    estpai = models.CharField(verbose_name="Pais", db_column='EstPai', max_length=50, blank=True)
    estciu = models.CharField(verbose_name="Ciudad", db_column='EstCiu', max_length=50, blank=True)
    estdir = models.CharField(verbose_name="Direccion", db_column='EstDir', max_length=100, blank=True)
    #estfeccre = models.DateTimeField(db_column='EstFecCre', default=timezone.now, editable=False)
    #estfecmod = models.DateTimeField(db_column='EstFecMod', default=timezone.now)
    estestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstEstReg', default=1)

    class Meta:
        db_table = 'estudiante'
        managed = True
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def get_full_name(self):
        return self.estnom + " " + self.estape

    def get_short_name(self):
        return self.estnom
    
    def __str__(self):
        return self.estnom + " " + self.estape + " - " + self.estdocide


class Curso(models.Model):
    curcod = models.IntegerField(verbose_name="Código", db_column='CurCod', primary_key=True)
    curnom = models.CharField(verbose_name="Nombre", db_column='CurNom', max_length=80, blank=False)
    curnummod = models.IntegerField( verbose_name="Numero de módulos", db_column='CurNumMod', default=0)
    curestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EStReg", db_column='CurEstRegCod')
    
    class Meta:
        db_table = 'curso'
        managed = True
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return self.curnom


class Programa(models.Model):
    procod = models.IntegerField(verbose_name="Codigo", db_column='ProCod', primary_key=True)
    pronom = models.CharField(verbose_name="Nombre", db_column='ProNom', max_length=100, blank=False)
    procodosh = models.CharField(verbose_name="Codigo osha", db_column='ProCodOsh', max_length=30)
    pronumcur = models.IntegerField( verbose_name="Numero de cursos", db_column='ProNumCur', default=0)
    proestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='ProEstRegCod')
    cursos = models.ManyToManyField(Curso, related_name='programas', verbose_name="Cursos", blank=True)
    
    class Meta:
        db_table = 'programa'
        managed = True
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
    
    def __str__(self):
        return self.pronom


class Modulo(models.Model):
    modcod = models.AutoField(verbose_name="Codigo", db_column='ModCod', primary_key=True)
    modnom = models.CharField(verbose_name="Nombre", db_column='ModNom', max_length=100, blank=False)
    modcurcod = models.ForeignKey(Curso, models.DO_NOTHING, verbose_name="Codigo Curso", db_column='ModCurCod')
    modestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='ModEstRegCod')
    
    class Meta:
        db_table = 'modulo'
        managed = True
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'
    
    def __str__(self):
        return self.modnom


class Examen(models.Model):
    exacod = models.AutoField(verbose_name="Codigo", db_column='ExaCod', primary_key=True)
    exacurcod = models.ForeignKey(Curso, models.DO_NOTHING, verbose_name="Codigo Curso", db_column='ExaCurCod')
    exaestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EStReg", db_column='ExaEstRegCod')
    
    class Meta:
        db_table = 'examen'
        managed = True
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'
    
    def __str__(self):
        return self.exacurcod.curnom


class Pregunta(models.Model):
    precod = models.AutoField(verbose_name="Codigo", db_column='preCod', primary_key=True)
    pretex = models.CharField(verbose_name="Texto",db_column="PreTex", max_length=300)
    preexacod = models.ForeignKey(Examen, models.DO_NOTHING, verbose_name="Codigo EXamen", db_column='PreExaCod')
    preestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EStReg", db_column='PreEstRegCod')
    
    class Meta:
        db_table = 'Pregunta'
        managed = True
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Pregunta'
    
    def __str__(self):
        return self.pretex
    


class Alternativa(models.Model):
    altcod = models.AutoField(verbose_name="Codigo", db_column='AltCod', primary_key=True)
    alttex = models.CharField(verbose_name="Texto", db_column='AltTex', max_length=500)
    altcor = models.BooleanField(verbose_name="Correcto", db_column='AltCor')
    altprecod = models.ForeignKey(Pregunta, models.DO_NOTHING, verbose_name="Codigo Pregunta", db_column='AltPreCod')
    altestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='AltEstRegCod')
    
    class Meta:
        db_table = 'alternativa'
        managed = True
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'
    
    def __str__(self):
        return self.alttex


class Respuesta(models.Model):
    rescod = models.AutoField(verbose_name="Codigo", db_column='ResCod', primary_key=True)
    respun = models.DecimalField(verbose_name="Puntuacion", db_column='ResPun', max_digits=5, decimal_places=2)
    resestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codigo Estudiante", db_column='ResEstCod')
    resexacod = models.ForeignKey(Examen, models.DO_NOTHING, verbose_name="Codigo Examen", db_column='ResExaCod')
    resprecod = models.ForeignKey(Pregunta, models.DO_NOTHING, verbose_name="Codigo Pregunta", db_column='ResPreCod')
    resaltcod = models.ForeignKey(Alternativa, models.DO_NOTHING, verbose_name="Codigo Alternativa", db_column='ResAltCod')
    resprocod = models.ForeignKey(Programa, models.DO_NOTHING, verbose_name="Codigo Programa", db_column='ResProCod')
    resestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='AltEstRegCod')
    
    class Meta:
        db_table = 'respuesta'
        managed = True
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        unique_together = ('resestcod','resprocod', 'resexacod', 'resprecod')
    
    def __str__(self):
        return self.rescod


class Matricula(models.Model):
    matcod = models.AutoField(verbose_name="Codigo", db_column='MatCod', primary_key=True)
    matestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codigo Estudiante", db_column='MatEstCod')
    matprocod = models.ForeignKey(Programa, models.DO_NOTHING, verbose_name="Codigo Programa", db_column='MatProCod')
    matestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='MatEstRegCod')
    
    class Meta:
        db_table = 'matricula'
        managed = True
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        unique_together = ('matestcod','matprocod')
    
    def __str__(self):
        return self.matcod


class RegistroExamen(models.Model):
    regexacod = models.AutoField(verbose_name="Codigo", db_column='RegExaCod', primary_key=True)
    regexapun = models.DecimalField(verbose_name="Puntuacion", db_column='RegExaPun', max_digits=5, decimal_places=2)
    regexaint = models.IntegerField( verbose_name="Número de intentos", db_column='RegExaInt', default=0)
    regexaest = models.CharField(verbose_name="Estado", db_column='RegExaEst', max_length=100)
    regexaestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codio Estudiante", db_column='RegExaEstCod')
    regexaexacod = models.ForeignKey(Examen, models.DO_NOTHING, verbose_name="Codigo Examen", db_column='RegExaExaCod')
    
    class Meta:
        db_table = 'registro_examen'
        managed = True
        verbose_name = 'RegistroExamen'
        verbose_name_plural = 'RegistroExamenes'
        unique_together = ('regexaestcod','regexaexacod')
    
    def __str__(self):
        return self.regexaest


class RegistroCurso(models.Model):
    regcurcod = models.AutoField(verbose_name="Codigo", db_column='RegCurCod', primary_key=True)
    regcurest = models.CharField(verbose_name="Estado", db_column='RegCurEst', max_length=50)
    regcurpro = models.DecimalField(verbose_name="Progeso", db_column='RegCurPro', max_digits=5, decimal_places=2)
    regcurprocod = models.ForeignKey(Programa, models.DO_NOTHING, verbose_name="Codiogo Programa", db_column='RegCurProCod')
    regcurestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codigo Estudiante", db_column='RegCurEstCod')
    regcurcurcod = models.ForeignKey(Curso, models.DO_NOTHING, verbose_name="Codigo Curso", db_column='RegCurCurCod')
    
    class Meta:
        db_table = 'registro_curso'
        managed = True
        verbose_name = 'RegistroCurso'
        verbose_name_plural = 'RegistroCursos'
        unique_together = ('regcurprocod','regcurestcod','regcurcurcod')
    
    def __str__(self):
        return self.regcurest


class NotaPrograma(models.Model):
    notprocod = models.AutoField(verbose_name="codigo", db_column='NotProCod', primary_key=True)
    notpropun = models.DecimalField(verbose_name="Puntuacion", db_column='NotProPun', max_digits=5, decimal_places=2)
    notproestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codio Estudiante", db_column='NotProEstCod')
    notproprocod = models.ForeignKey(Programa, models.DO_NOTHING, verbose_name="Codigo Programa", db_column='NotProProCod')
    
    class Meta:
        db_table = 'nota_programa'
        managed = True
        verbose_name = 'NotaPrograma'
        verbose_name_plural = 'NotaProgramas'
        unique_together = ('notproestcod','notproprocod')
    
    def __str__(self):
        return self.notprocod