from django.db import models
from aula.models import EstudianteUser, Programa, Curso, MatriculaPrograma, MatriculaCurso


# Create your models here.


class CredencialProgramaMatriculado(models.Model):
    TIPO_CHOICES = [
        ('CERT', 'Certificado'),
        ('DIPLO', 'Diploma')
    ]
    creprocod = models.AutoField(verbose_name="Código", db_column='CreProCod', primary_key=True)
    creprofecemi = models.DateField(verbose_name="Fecha de emisión", db_column='CreProFecEmi', blank=True, null=True)
    creprofeccad = models.DateField(verbose_name="Fecha de caducidad", db_column='CreProFecCad', blank=True, null=True)
    creprotipo = models.CharField(verbose_name="Tipo credencial", db_column='CreProTipo', blank=False, null=False, max_length=20, choices=TIPO_CHOICES)
    creprocarnet = models.BooleanField(verbose_name="Con carnet", db_column='CreProCarnet', blank=False, null=False, default=True)
    crepromatprocod = models.ForeignKey(MatriculaPrograma, models.PROTECT, verbose_name="Código Matrícula Programa", db_column='CreProMatProCod', blank=True, null=True)
    class Meta:
        db_table = 'Credencial_programa_matriculado'
        managed = True
        verbose_name = 'Credencial para Programa Matriculado'
        verbose_name_plural = 'Credenciales para Programa Matriculado'


class CredencialPrograma(models.Model):
    TIPO_CHOICES = [
        ('CERT', 'Certificado'),
        ('DIPLO', 'Diploma')
    ]
    creprocod = models.AutoField(verbose_name="Código", db_column='CreProCod', primary_key=True)
    creprofecemi = models.DateField(verbose_name="Fecha de emisión", db_column='CreProFecEmi', blank=True, null=True)
    creprofeccad = models.DateField(verbose_name="Fecha de caducidad", db_column='CreProFecCad', blank=True, null=True)
    creprotipo = models.CharField(verbose_name="Tipo credencial", db_column='CreProTipo', blank=False, null=False, max_length=20, choices=TIPO_CHOICES)
    creprocarnet = models.BooleanField(verbose_name="Con carnet", db_column='CreProCarnet', blank=False, null=False, default=True)
    creproestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Código Estudiante", db_column='CreProEstCod', blank=True, null=True)
    creproprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Código Programa", db_column='CreProProCod', blank=True, null=True)
    class Meta:
        db_table = 'Credencial_programa'
        managed = True
        verbose_name = 'Credencial para Programa'
        verbose_name_plural = 'Credenciales para Programa'


class CertificadoCursoMatriculado(models.Model):
    cercurcod = models.AutoField(verbose_name="Código", db_column='CerCurCod', primary_key=True)
    cercurfecemi = models.DateField(verbose_name="Fecha de emisión", db_column='CerCurFecEmi', blank=True, null=True)
    cercurfeccad = models.DateField(verbose_name="Fecha de caducidad", db_column='CerCurFecCad', blank=True, null=True)
    cercurcarnet = models.BooleanField(verbose_name="Con carnet", db_column='CerCurCarnet', blank=False, null=False, default=False)
    cercurmatcurcod = models.ForeignKey(MatriculaCurso, models.PROTECT, verbose_name="Código Matrícula Curso", db_column='CerCurMatCurCod', blank=True, null=True)
    class Meta:
        db_table = 'certificado_curso_matriculado'
        managed = True
        verbose_name = 'Certificado para Curso Matriculado'
        verbose_name_plural = 'Certificados para Curso Matriculado'


class CertificadoCurso(models.Model):
    cercurcod = models.AutoField(verbose_name="Código", db_column='CerCurCod', primary_key=True)
    cercurfecemi = models.DateField(verbose_name="Fecha de emisión", db_column='CerCurFecEmi', blank=True, null=True)
    cercurfeccad = models.DateField(verbose_name="Fecha de caducidad", db_column='CerCurFecCad', blank=True, null=True)
    cercurcarnet = models.BooleanField(verbose_name="Con carnet", db_column='CerCurCarnet', blank=False, null=False, default=False)
    cercurestcod = models.ForeignKey(EstudianteUser, models.PROTECT, verbose_name="Código Estudiante", db_column='CerCurEstCod', blank=True, null=True)
    cercurcurcod = models.ForeignKey(Curso, models.PROTECT, verbose_name="Código Programa", db_column='CerCurCurCod', blank=True, null=True)
    class Meta:
        db_table = 'certificado_curso'
        managed = True
        verbose_name = 'Certificado para Curso'
        verbose_name_plural = 'Certificados para Curso'