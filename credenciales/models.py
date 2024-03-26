from django.db import models
from  aula.models import EstadoRegistro

# Create your models here.

class Certificado(models.Model):
    cercod = models.AutoField(verbose_name="Codigo", db_column='CerCod', primary_key=True)
    cerestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='CerEstRegCod')
    
    class Meta:
        db_table = 'certificado'
        managed = True
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'


class Diploma(models.Model):
    dipcod = models.AutoField(verbose_name="", db_column='DipCod', primary_key=True)
    dipestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='DipEstRegCod')
    
    class Meta:
        db_table = 'diploma'
        managed = True
        verbose_name = 'Diploma'
        verbose_name_plural = 'Diplomas'


class Carnet(models.Model):
    carcod = models.AutoField(verbose_name="", db_column='CarCod', primary_key=True)
    carestregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, verbose_name="Codigo EstReg", db_column='CarEstRegCod')
    
    class Meta:
        db_table = 'carnet'
        managed = True
        verbose_name = 'Carnet'
        verbose_name_plural = 'Carnets'