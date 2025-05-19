from django.db import models
from users.models import EstudianteUser


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


class Curso(models.Model):
    curcod = models.IntegerField(verbose_name="Código", db_column='CurCod', primary_key=True)
    curnom = models.CharField(verbose_name="Nombre", db_column='CurNom', max_length=80, blank=False)
    curnomeng = models.CharField(verbose_name="Nombre en Inglés", db_column='CurNomEng', max_length=80, blank=False, default="")
    curfre = models.BooleanField(verbose_name="Gratuitos", db_column='CurFre', default=False)
    curnummod = models.IntegerField( verbose_name="Número de módulos", db_column='CurNumMod', default=0)
    cursrcpdf = models.FileField(verbose_name="Archivo PDF", db_column='CurSrcPdf', upload_to='cursos_pdf/', blank=True, null=True)
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
    pronom = models.CharField(verbose_name="Nombre de Grado", db_column='ProNom',max_length=200, blank=False)
    pronomeng = models.CharField(verbose_name="Nombre de Grado en inglés", db_column='ProNomEng',max_length=200, blank=True, default='')
    prodip = models.CharField(verbose_name="Nombre de Diploma", db_column='ProDip',max_length=200, blank=True, default='')
    prodipeng = models.CharField(verbose_name="Nombre de Diploma en inglés", db_column='ProDipEng',max_length=200, blank=True, default='')
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
    modsrctxt = models.FileField(verbose_name="Archivo TXT", db_column='ModSrcTxt', upload_to='modulo_pdf/', blank=True, null=True)
    modcurcod = models.ForeignKey(Curso, models.PROTECT, verbose_name="Codigo Curso", db_column='ModCurCod')
    modestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg", db_column='ModEstRegCod')
    
    class Meta:
        db_table = 'modulo'
        managed = True
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'
    
    def __str__(self):
        return f"{self.modcurcod} - {self.modnom}"


class Examen(models.Model):
    exacurcod = models.OneToOneField(Curso, models.PROTECT, verbose_name="Codigo Curso", db_column='ExaCurCod', primary_key=True)
    exanumpre = models.IntegerField( verbose_name="Número de preguntas", db_column='ExaNumPre', default=0)
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
    pretex = models.CharField(verbose_name="Texto",db_column="PreTex", max_length=500)
    preexp = models.CharField(verbose_name="Explicación",db_column="PreExp", max_length=1000, default='')
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
        return f"{self.matproestcod.usuario.usernom} - {self.matproprocod.pronom}"


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
        return f"{self.matcurestcod.usuario.usernom} - {self.matcurcurcod.curnom}"


class RespuestaExamenPrograma(models.Model):
    resprocod = models.AutoField(verbose_name="Código", db_column='ResProCod', primary_key=True)
    respropun = models.DecimalField(verbose_name="Puntuacion", db_column='ResProPun', max_digits=5, decimal_places=2)
    resproestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Codigo Estudiante", db_column='ResProEstCod')
    resproprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Codigo Programa", db_column='ResProProCod')
    resproexacod = models.ForeignKey(Examen, on_delete=models.PROTECT, verbose_name="Codigo Examen", db_column='ResProExaCod')
    resproprecod = models.ForeignKey(Pregunta, on_delete=models.PROTECT, verbose_name="Pregunta", db_column='ReaProPreCod')
    resproaltcod = models.ForeignKey(Alternativa, on_delete=models.PROTECT, verbose_name="Alternativa seleccionada", db_column='ResProAltCod')
    resprofec = models.DateTimeField(verbose_name="Fecha de respuesta", db_column='ResProFec', auto_now_add=True)

    class Meta:
        db_table = 'respuesta_examen_programa'
        managed = True
        verbose_name = 'Respuesta de Examen por Programa'
        verbose_name_plural = 'Respuestas de Exámenes por Programa'
        unique_together = ('resproestcod', 'resproprocod', 'resproexacod', 'resproprecod')

    def __str__(self):
        return f"{self.resproestcod.usuario.usernom} - {self.resproprecod} - {self.resproaltcod}"


class RespuestaExamenCurso(models.Model):
    rescurcod = models.AutoField(verbose_name="Código", db_column='RepCurCod', primary_key=True)
    rescurpun = models.DecimalField(verbose_name="Puntuacion", db_column='ResCurPun', max_digits=5, decimal_places=2)
    rescurestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Codigo Estudiante", db_column='ResCurEstCod')
    rescurexacod = models.ForeignKey(Examen, on_delete=models.PROTECT, verbose_name="Codigo Examen", db_column='ResCurExaCod')
    rescurprecod = models.ForeignKey(Pregunta, on_delete=models.PROTECT, verbose_name="Pregunta", db_column='ResCurPreCod')
    rescuraltcod = models.ForeignKey(Alternativa, on_delete=models.PROTECT, verbose_name="Alternativa seleccionada", db_column='ResCurAltCod')
    rescurfec = models.DateTimeField(verbose_name="Fecha de respuesta", db_column='ResCurFec', auto_now_add=True)

    class Meta:
        db_table = 'respuesta_examen_curso'
        managed = True
        verbose_name = 'Respuesta de Examen por Curso'
        verbose_name_plural = 'Respuestas de Exámenes por Curso'
        unique_together = ('rescurestcod', 'rescurexacod', 'rescurprecod')  # Una respuesta por pregunta en un intento.

    def __str__(self):
        return f"{self.rescurestcod.usuario.usernom} - {self.rescurprecod} - {self.rescuraltcod}"



class RegistroExamenPrograma(models.Model):
    regexaprocod = models.AutoField(verbose_name="Código", db_column='RegExaProCod', primary_key=True)
    regexapropun = models.DecimalField(verbose_name="Puntuación", db_column='RegExaProPun', max_digits=5, decimal_places=2, default=0.00)
    regexaproint = models.IntegerField(verbose_name="Número de intentos", db_column='RegExaProInt', default=0)
    regexaproprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Matrícula del Programa", db_column='RegExProProCod')
    regexaproestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Matrícula del Programa", db_column='RegExProEstCod')
    regexaproexacod = models.ForeignKey(Examen, models.PROTECT, verbose_name="Código del Examen", db_column='RegExProExaCod')
    regexaproestexacod = models.ForeignKey(EstadoExamen, models.PROTECT, verbose_name="Estado del Examen", db_column='RegExProEstExaCod')

    class Meta:
        db_table = 'registro_examen_programa'
        managed = True
        verbose_name = 'Registro de Examen por Programa'
        verbose_name_plural = 'Registros de Exámenes por Programa'
        unique_together = ('regexaproestcod', 'regexaproprocod', 'regexaproexacod')  # Una matrícula solo puede tener un registro por examen.

    def __str__(self):
        return f"{self.regexaproestcod.usuario.usernom} - {self.regexaproexacod} - {self.regexaproestexacod.estexanom}"


class RegistroExamenCurso(models.Model):
    regexacurcod = models.AutoField(verbose_name="Código", db_column='RegExaCurCod', primary_key=True)
    regexacurpun = models.DecimalField(verbose_name="Puntuación", db_column='RegExaCurPun', max_digits=5, decimal_places=2, default=0.00)
    regexacurint = models.IntegerField(verbose_name="Número de intentos", db_column='RegExaCurInt', default=0)
    regexacurcurcod = models.ForeignKey(Curso, models.PROTECT, verbose_name="Matrícula del Curso", db_column='RegExaCurCurCod')
    regexacurestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Matrícula del Programa", db_column='RegExaProEstCod')
    regexacurexacod = models.ForeignKey(Examen, models.PROTECT, verbose_name="Código del Examen", db_column='RegExaCurExaCod')
    regexacurestexacod = models.ForeignKey(EstadoExamen, models.PROTECT, verbose_name="Estado del Examen", db_column='RegExaCurEstExaCod')

    class Meta:
        db_table = 'registro_examen_curso'
        managed = True
        verbose_name = 'Registro de Examen por Curso'
        verbose_name_plural = 'Registros de Exámenes por Curso'
        unique_together = ('regexacurestcod', 'regexacurcurcod', 'regexacurexacod')

    def __str__(self):
        return f"{self.regexacurestcod.usuario.usernom} - {self.regexacurexacod} - {self.regexacurestexacod.estexanom}"