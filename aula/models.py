from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError

# Create your models here.

class EstadoRegistro(models.Model):
    estregcod = models.AutoField(verbose_name="Codigo", db_column='EstRegCod', primary_key=True)
    estregnom = models.CharField(verbose_name="Nombre", db_column='EstRegNom', max_length=40, blank=False, unique=True)
    
    class Meta:
        db_table = 'estado_registro'
        managed = True
        verbose_name = 'EstadoRegistro'
        verbose_name_plural = 'EstadosRegistro'
    
    def __str__(self):
        return self.estregnom


class EstadoExamen(models.Model):
    estexacod = models.AutoField(verbose_name="Código", db_column='EstExaCod', primary_key=True)
    estexanom = models.CharField(verbose_name="Nombre de Estado", db_column='EstExaNom', max_length=40, blank=False, unique=True)

    class Meta:
        db_table = 'estado_examen'
        managed = True
        verbose_name = 'EstadoExamen'
        verbose_name_plural = 'EstadosExamenes'

    def __str__(self):
        return self.estexanom


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class EstudianteUser(AbstractBaseUser, PermissionsMixin): #UserAccount
    USER_TYPES = [
        ('ADMIN', 'Administrador'),
        ('PROF', 'Profesor'),
        ('STUD', 'Estudiante'),
    ]
    email = models.EmailField(verbose_name="Email", unique=True)
    
    estusernom = models.CharField(verbose_name="Nombre", db_column='EstUserNom', max_length=60, blank=False)
    estuserape = models.CharField(verbose_name="Apellidos", db_column='EstUserApe', max_length=60, blank=False)
    estuserdocide = models.CharField(verbose_name="Documento de identidad", db_column='EstUserDocIde', max_length=50, blank=False, unique=True)
    estuserpai = models.CharField(verbose_name="Pais", db_column='EstUserPai', max_length=50, blank=True, null=True)
    estuserciu = models.CharField(verbose_name="Ciudad", db_column='EstUserCiu', max_length=50, blank=True, null=True)
    estuserdir = models.CharField(verbose_name="Dirección", db_column='EstUserDir', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserAccountManager()
    
    def __str__(self):
        return self.estusernom + " " + self.estuserape + " - " + self.estuserdocide


class Curso(models.Model):
    curcod = models.IntegerField(verbose_name="Código", db_column='CurCod', primary_key=True)
    curnom = models.CharField(verbose_name="Nombre", db_column='CurNom', max_length=80, blank=False)
    curnummod = models.IntegerField( verbose_name="Número de módulos", db_column='CurNumMod', default=0)
    curfre = models.BooleanField(verbose_name="Gratuitos", db_column='CurFre', default=False)
    curestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Código EstReg", db_column='CurEstRegCod')
    
    class Meta:
        db_table = 'curso'
        managed = True
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return self.curnom


class Programa(models.Model):
    procod = models.IntegerField(verbose_name="Código", db_column='ProCod', primary_key=True)
    pronom = models.CharField(verbose_name="Nombre", db_column='ProNom', max_length=100, blank=False)
    pronomeng = models.CharField(verbose_name="Nombre en inglés", db_column='ProNomEng', max_length=100, blank=True, default='')
    pronomdip = models.CharField(verbose_name="Nombre de diploma", db_column='ProNomDip', max_length=100, blank=True, default='')
    procodosh = models.CharField(verbose_name="Codigo osha", db_column='ProCodOsh', max_length=30)
    pronumhor = models.IntegerField( verbose_name="Número de horas", db_column='ProNumHor', default=0)
    pronumcur = models.IntegerField( verbose_name="Número de cursos", db_column='ProNumCur', default=0)
    proestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Código EstReg", db_column='ProEstRegCod')
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
    modcurcod = models.ForeignKey(Curso, models.PROTECT, verbose_name="Codigo Curso", db_column='ModCurCod')
    modestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg", db_column='ModEstRegCod')
    
    class Meta:
        db_table = 'modulo'
        managed = True
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'
    
    def __str__(self):
        return self.modnom


class Examen(models.Model):
    exacurcod = models.OneToOneField(Curso, models.PROTECT, verbose_name="Codigo Curso", db_column='ExaCurCod', primary_key=True)
    exanumpre = models.IntegerField( verbose_name="Numero de preguntas", db_column='ExaNumPre', default=0)
    exaestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg", db_column='ExaEstRegCod', default=1)
    
    class Meta:
        db_table = 'examen'
        managed = True
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'
    
    def __str__(self):
        return f"{self.exacurcod.curnom}"


class Pregunta(models.Model):
    precod = models.AutoField(verbose_name="Codigo", db_column='preCod', primary_key=True)
    pretex = models.CharField(verbose_name="Texto",db_column="PreTex", max_length=300)
    prenummod = models.IntegerField(verbose_name="Número de modulo al que pertenece", db_column="PreNumMod", default=0)
    preexacod = models.ForeignKey(Examen, models.PROTECT, verbose_name="Codigo EXamen", db_column='PreExaCod')
    preestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EStReg", db_column='PreEstRegCod')
    
    class Meta:
        db_table = 'Pregunta'
        managed = True
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Pregunta'
    
    def __str__(self):
        return f"{self.precod} - {self.pretex}"


class Alternativa(models.Model):
    altcod = models.AutoField(verbose_name="Codigo", db_column='AltCod', primary_key=True)
    alttex = models.CharField(verbose_name="Texto", db_column='AltTex', max_length=500)
    altcor = models.BooleanField(verbose_name="Correcto", db_column='AltCor')
    altprecod = models.ForeignKey(Pregunta, models.PROTECT, verbose_name="Código Pregunta", db_column='AltPreCod')
    altestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Código EstReg", db_column='AltEstRegCod')
    
    class Meta:
        db_table = 'alternativa'
        managed = True
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'
    
    def __str__(self):
        return self.alttex


class MatriculaPrograma(models.Model):
    matprocod = models.AutoField(verbose_name="Codigo", db_column='MatProCod', primary_key=True)
    matprofecini = models.DateField(verbose_name="Fecha de inicio", db_column='MatProFecIni', blank=True, null=True)
    matprofecfin = models.DateField(verbose_name="Fecha de finalización", db_column='MatProFecFin', blank=True, null=True)
    matproter = models.BooleanField(verbose_name="Programa terminado", db_column='MatProTer', blank=False, null=False, default=False)
    matpropun = models.DecimalField(verbose_name="Puntuación", db_column='MatProPun', max_digits=5, decimal_places=2, default=0.00)
    matpropor = models.DecimalField(verbose_name="Porcentaje de avance", db_column='MatProPor', max_digits=5, decimal_places=2, default=0.00)
    matproestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Codigo Estudiante", db_column='MatProEstCod')
    matproprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Codigo Programa", db_column='MatProProCod')
    matproestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg", db_column='MatProEstRegCod')
    
    class Meta:
        db_table = 'matricula_programa'
        managed = True
        verbose_name = 'Matricula para Programa'
        verbose_name_plural = 'Matricula para Programas'
        unique_together = ('matproestcod','matproprocod')
    
    def __str__(self):
        return f"{self.matproestcod.estusernom} - {self.matproprocod.pronom}"


class MatriculaCurso(models.Model):
    matcurcod = models.AutoField(verbose_name="Código", db_column='MatCurCod', primary_key=True)
    matcurfecini = models.DateField(verbose_name="Fecha de inicio", db_column='MatCurFecIni', blank=True, null=True)
    matcurfecfin = models.DateField(verbose_name="Fecha de finalización", db_column='MatCurFecFin', blank=True, null=True)
    matcurter = models.BooleanField(verbose_name="Curso terminado", db_column='MatCurTer', blank=False, null=False, default=False)
    matcurestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Código Estudiante", db_column='MatCurEstCod')
    matcurcurcod = models.ForeignKey(Curso, models.PROTECT, verbose_name="Código Curso", db_column='MatCurCurCod')
    matcurestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Código EstReg", db_column='MatCurEstRegCod')
    
    class Meta:
        db_table = 'matricula_curso'
        managed = True
        verbose_name = 'Matricula para Curso'
        verbose_name_plural = 'Matricula para Cursos'
        unique_together = ('matcurestcod','matcurcurcod')
    
    def __str__(self):
        return f"{self.matcurestcod.estusernom} - {self.matcurcurcod.curnom}"


#class Respuesta(models.Model):
#    rescod = models.AutoField(verbose_name="Codigo", db_column='ResCod', primary_key=True)
#    respun = models.DecimalField(verbose_name="Puntuacion", db_column='ResPun', max_digits=5, decimal_places=2)
#    resestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Codigo Estudiante", db_column='ResEstCod')
#    resprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Codigo Programa", db_column='ResProCod')
#    resexacod = models.ForeignKey(Examen, on_delete=models.PROTECT, verbose_name="Codigo Examen", db_column='ResExaCod')
#    resprecod = models.ForeignKey(Pregunta, models.PROTECT, verbose_name="Codigo Pregunta", db_column='ResPreCod')
#    resaltcod = models.ForeignKey(Alternativa, models.PROTECT, verbose_name="Codigo Alternativa", db_column='ResAltCod')
#    
#    class Meta:
#        db_table = 'respuesta'
#        managed = True
#        verbose_name = 'Respuesta'
#        verbose_name_plural = 'Respuestas'
#        unique_together = ('resestcod','resprocod', 'resexacod', 'resprecod')
#    
#    def __str__(self):
#        return f"{self.rescod}"



class Respuesta(models.Model):
    rescod = models.AutoField(verbose_name="Código", db_column='ResCod', primary_key=True)
    resfec = models.DateTimeField( verbose_name="Fecha de Respuesta", db_column='ResFec', auto_now_add=True)
    resexacod = models.ForeignKey(Examen, on_delete=models.PROTECT, verbose_name="Codigo Examen", db_column='ResExaCod')
    resprecod = models.ForeignKey(Pregunta, models.PROTECT, verbose_name="Codigo Pregunta", db_column='ResPreCod')
    resaltcod = models.ForeignKey(Alternativa, models.PROTECT, verbose_name="Codigo Alternativa", db_column='ResAltCod')
    resmatcurcod = models.ForeignKey('MatriculaCurso', models.PROTECT, verbose_name="Matrícula del Curso", db_column='ResMatCur', blank=True, null=True)
    resmatprocod = models.ForeignKey('MatriculaPrograma', models.PROTECT, verbose_name="Matrícula del Programa", db_column='ResMatPro', blank=True, null=True)

    class Meta:
        db_table = 'respuesta'
        managed = True
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return f"Respuesta {self.rescod} - Pregunta {self.resprecod}"
    
    def clean(self):
        super().clean()
        # Validación: Solo uno de los dos campos debe estar lleno
        if self.resmatcurcod and self.resmatprocod:
            raise ValidationError(
                "La respuesta no puede estar asociada a una matrícula de curso y a una matrícula de programa al mismo tiempo."
            )
        if not self.resmatcurcod and not self.resmatprocod:
            raise ValidationError(
                "La respuesta debe estar asociada a una matrícula de curso o a una matrícula de programa."
            )


class RegistroExamen(models.Model):
    regexacod = models.AutoField(verbose_name="Codigo", db_column='RegExaCod', primary_key=True)
    regexapun = models.DecimalField(verbose_name="Puntuacion", db_column='RegExaPun', max_digits=5, decimal_places=2)
    regexaint = models.IntegerField( verbose_name="Número de intentos", db_column='RegExaInt', default=0)
    regexaestexacod = models.ForeignKey(EstadoExamen, models.PROTECT, verbose_name="Codigo Examen", db_column='RegExaEstExaCod')
    regexaestprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Codigo Programa", db_column='RegExaEstProCod')
    regexaestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Codigo Estudiante", db_column='RegExaEstCod')
    regexaexacod = models.ForeignKey(Examen, models.PROTECT, verbose_name="Codigo Examen", db_column='RegExaExaCod')
    
    class Meta:
        db_table = 'registro_examen'
        managed = True
        verbose_name = 'RegistroExamen'
        verbose_name_plural = 'RegistroExamenes'
        unique_together = ('regexaestprocod','regexaestcod','regexaexacod') #Estudiante-Programa-Examen
    
    def __str__(self):
        return f"{self.regexaestcod} - {self.regexaexacod} - {self.regexaestexacod.estexanom}"


class RegistroExamenPrograma(models.Model):
    regexaprocod = models.AutoField(verbose_name="Código", db_column='RegExProCod', primary_key=True)
    regexapropun = models.DecimalField(verbose_name="Puntuación", db_column='RegExProPun', max_digits=5, decimal_places=2, default=0.00)
    regexaproint = models.IntegerField(verbose_name="Número de intentos", db_column='RegExProInt', default=0)
    regexaproestexacod = models.ForeignKey(EstadoExamen, models.PROTECT, verbose_name="Estado del Examen", db_column='RegExProEstExaCod')
    regexapromatprocod = models.ForeignKey(MatriculaPrograma, models.PROTECT, verbose_name="Matrícula del Programa", db_column='RegExProMatProCod')
    regexaproexacod = models.ForeignKey(Examen, models.PROTECT, verbose_name="Código del Examen", db_column='RegExProExaCod')

    class Meta:
        db_table = 'registro_examen_programa'
        managed = True
        verbose_name = 'Registro de Examen por Programa'
        verbose_name_plural = 'Registros de Exámenes por Programa'
        unique_together = ('regexapromatprocod', 'regexaproexacod')  # Una matrícula solo puede tener un registro por examen.

    def __str__(self):
        return f"{self.regexapromatprocod.matproestcod.estusernom} - {self.regexaproexacod} - {self.regexaproestexacod.estexanom}"


class RegistroExamenCurso(models.Model):
    regexacurcod = models.AutoField(verbose_name="Código", db_column='RegExCurCod', primary_key=True)
    regexacurpun = models.DecimalField(verbose_name="Puntuación", db_column='RegExCurPun', max_digits=5, decimal_places=2, default=0.00)
    regexacurint = models.IntegerField(verbose_name="Número de intentos", db_column='RegExCurInt', default=0)
    regexacurestexacod = models.ForeignKey(EstadoExamen, models.PROTECT, verbose_name="Estado del Examen", db_column='RegExCurEstExaCod')
    regexacurmatcurcod = models.ForeignKey(MatriculaCurso, models.PROTECT, verbose_name="Matrícula del Curso", db_column='RegExCurMatCurCod')
    regexacurexacod = models.ForeignKey(Examen, models.PROTECT, verbose_name="Código del Examen", db_column='RegExCurExaCod')

    class Meta:
        db_table = 'registro_examen_curso'
        managed = True
        verbose_name = 'Registro de Examen por Curso'
        verbose_name_plural = 'Registros de Exámenes por Curso'
        unique_together = ('regexacurmatcurcod', 'regexacurexacod')

    def __str__(self):
        return f"{self.regexacurmatcurcod.matcurestcod.estusernom} - {self.regexacurexacod} - {self.regexacurestexacod.estexanom}"