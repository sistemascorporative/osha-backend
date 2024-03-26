from django.db import models

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


class Estudiante(models.Model):
    estcod = models.AutoField(db_column='EstCod', primary_key=True)
    estnom = models.CharField(db_column='EstNom', max_length=60, blank=False)
    estape = models.CharField(db_column='EstApe', max_length=60, blank=False)
    estdocide = models.CharField(db_column='EstDcIde', max_length=50, blank=False)
    estema = models.EmailField(db_column='EstEma', max_length=50, blank=False)
    estpai = models.CharField(db_column='EstPai', max_length=50, blank=True)
    estciu = models.CharField(db_column='EstCiu', max_length=50, blank=True)
    estdir = models.CharField(db_column='EstDir', max_length=100, blank=True)
    #estfeccre = models.DateTimeField(db_column='EstFecCre', default=timezone.now, editable=False)
    #estfecmod = models.DateTimeField(db_column='EstFecMod', default=timezone.now)
    estestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstEstReg')


class Programa(models.Model):
    procod = models.AutoField(verbose_name="Codigo", db_column='ProCod', primary_key=True)
    pronom = models.CharField(verbose_name="Nombre", db_column='ProNom', max_length=100, blank=False)
    proestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='ProEstRegCod')
    
    class Meta:
        db_table = 'programa'
        managed = True
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
    
    def __str__(self):
        return self.pronom


class Curso(models.Model):
    curcod = models.AutoField(verbose_name="Codigo", db_column='CurCod', primary_key=True)
    curnom = models.CharField(verbose_name="Nombre", db_column='CurNom', max_length=80, blank=False)
    curprocod = models.ForeignKey(Programa, models.DO_NOTHING, verbose_name="Codigo Programa", db_column='CurProCod')
    curestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EStReg", db_column='CurEstRegCod')
    
    class Meta:
        db_table = 'curso'
        managed = True
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return self.curnom


class Modulo(models.Model):
    modcod = models.AutoField(verbose_name="Codigo", db_column='ModCod', primary_key=True)
    modnom = models.CharField(verbose_name="Nombre", db_column='ModNom', max_length=100, blank=False)
    modcurcod = models.ForeignKey(Curso, models.DO_NOTHING, verbose_name="Codigo Curso", db_column='ModCurCod')
    modestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EStReg", db_column='ModEstRegCod')
    
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
    altCor = models.BooleanField(verbose_name="Correcto", db_column='AltCor')
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
    resestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='AltEstRegCod')
    
    class Meta:
        db_table = 'respuesta'
        managed = True
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        unique_together = ('resestcod','resexacod', 'resprecod')
    
    def __str__(self):
        return self.rese


class Matricula(models.Model):
    matcod = models.AutoField(verbose_name="Codigo", db_column='MatCod', primary_key=True)
    matestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codigo Estudiante", db_column='MatEstCod')
    matcurcod = models.ForeignKey(Curso, models.DO_NOTHING, verbose_name="Codigo Curso", db_column='MatCurCod')
    matestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='MatEstRegCod')
    
    class Meta:
        db_table = 'matricula'
        managed = True
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
    
    def __str__(self):
        return self.matcod


class NotaCurso(models.Model):
    notcurcod = models.AutoField(verbose_name="codigo", db_column='NotCurCod', primary_key=True)
    notcurpun = models.DecimalField(verbose_name="Puntuacion", db_column='NotCurPun', max_digits=5, decimal_places=2)
    notcurestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codio Estudiante", db_column='NotCurEstCod')
    notcurcurcod = models.ForeignKey(Curso, models.DO_NOTHING, verbose_name="Codigo Curso", db_column='NotCurCurCod')
    notcurestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='NotCurEstRegCod')
    
    class Meta:
        db_table = 'nota_curso'
        managed = True
        verbose_name = 'NotaCurso'
        verbose_name_plural = 'NOtaCursos'
    
    def __str__(self):
        return self.notcurcod


class NotaPrograma(models.Model):
    notprocod = models.AutoField(verbose_name="codigo", db_column='NotProCod', primary_key=True)
    notpropun = models.DecimalField(verbose_name="Puntuacion", db_column='NotProPun', max_digits=5, decimal_places=2)
    notproestcod = models.ForeignKey(Estudiante, models.DO_NOTHING, verbose_name="Codio Estudiante", db_column='NotProEstCod')
    notproprocod = models.ForeignKey(Programa, models.DO_NOTHING, verbose_name="Codigo Programa", db_column='NotProProCod')
    notproestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='NotProEstRegCod')
    
    class Meta:
        db_table = 'nota_programa'
        managed = True
        verbose_name = 'NotaPrograma'
        verbose_name_plural = 'NotaProgramas'
        unique_together = ('notproestcod','notproprocod')
    
    def __str__(self):
        return self.notprocod