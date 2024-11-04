from django.db import models
from aula.models import EstadoRegistro, EstudianteUser, Programa

# Create your models here.



class Credencial(models.Model):
    crecod = models.AutoField(verbose_name="Codigo osha", db_column='CreCod', primary_key=True)
    creestcod = models.OneToOneField(EstudianteUser, models.PROTECT, verbose_name="Código Estudiante", db_column='CreEstCod', blank=True, null=True)
    creprocod = models.ForeignKey(Programa, models.PROTECT, verbose_name="Código del programa", db_column='CreProCod', blank=True, null=True)
    
    class Meta:
        db_table = 'credencial'
        managed = True
        verbose_name = 'Credencial'
        verbose_name_plural = 'Credenciales'


class Certificado(models.Model):
    cercod = models.AutoField(verbose_name="Codigo", db_column='CerCod', primary_key=True)
    cerfecemi = models.DateField(verbose_name="Fecha de emisión", db_column='CerFecEmi', blank=True, null=True)
    cerfeccad = models.DateField(verbose_name="Fecha de caducidad", db_column='CerFecCad', blank=True, null=True)
    cersrc = models.FileField(verbose_name="Archivo", db_column="CerSrc", upload_to='credenciales/certificados/', blank=True, null=True)
    cercrecod = models.ForeignKey(Credencial, models.PROTECT, verbose_name="Código de credencial", db_column='CerCreCod', blank=True, null=True)
    cerestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg", db_column='CerEstRegCod', blank=True, null=True)
    
    class Meta:
        db_table = 'certificado'
        managed = True
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'


class Diploma(models.Model):
    dipcod = models.AutoField(verbose_name="", db_column='DipCod', primary_key=True)
    dipfecemi = models.DateField(verbose_name="Fecha de emisión", db_column='CerDipEmi', blank=True, null=True)
    dipfeccad = models.DateField(verbose_name="Fecha de caducidad", db_column='CerDipCad', blank=True, null=True)
    dipsrc = models.FileField(verbose_name="Archivo", db_column="DipSrc", upload_to='credenciales/diplomas/', blank=True, null=True)
    dipcrecod = models.ForeignKey(Credencial, models.PROTECT, verbose_name="Código de credencial", db_column='DipCreCod', blank=True, null=True)
    dipestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg", db_column='DipEstRegCod', blank=True, null=True)
    
    class Meta:
        db_table = 'diploma'
        managed = True
        verbose_name = 'Diploma'
        verbose_name_plural = 'Diplomas'


class Carnet(models.Model):
    carcod = models.AutoField(verbose_name="", db_column='CarCod', primary_key=True)
    carsrc = models.FileField(verbose_name="Archivo", db_column="CarSrc", upload_to='credenciales/carnets/', blank=True, null=True)
    carcrecod = models.ForeignKey(Credencial, models.PROTECT, verbose_name="Código de credencial", db_column='CarCreCod', blank=True, null=True)
    carestregcod = models.ForeignKey(EstadoRegistro, models.PROTECT, verbose_name="Codigo EstReg")
    
    class Meta:
        db_table = 'carnet'
        managed = True
        verbose_name = 'Carnet'
        verbose_name_plural = 'Carnets'