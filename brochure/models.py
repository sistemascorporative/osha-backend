from django.db import models
from aula.models import Programa


# Create your models here.


class Brochure(models.Model):
    broprocod = models.OneToOneField(Programa, models.PROTECT, verbose_name="Código Curso", db_column='BroProCod', primary_key=True)
    bronummod = models.IntegerField( verbose_name="Número de módulos", db_column='BroNumMod', default=0)
    
    class Meta:
        db_table = 'brochure'
        managed = True
        verbose_name = 'Brochure'
        verbose_name_plural = 'Brochures'
    
    def __str__(self):
        return self.broprocod


class BModulo(models.Model):
    bmodcod = models.AutoField(verbose_name="Codigo", db_column='BModCod', primary_key=True)
    bmodnomes = models.CharField(verbose_name="Nombre en español", db_column='BModNomEs', max_length=100, blank=False)
    bmodnomen = models.CharField(verbose_name="Nombre en Ingles", db_column='BModNomEn', max_length=100, blank=False)
    bmodbrocod = models.ForeignKey(Brochure, models.PROTECT, verbose_name="Codigo Curso", db_column='ModCurCod')
    
    class Meta:
        db_table = 'bmodulo'
        managed = True
        verbose_name = 'BModulo'
        verbose_name_plural = 'BModulos'
    
    def __str__(self):
        return self.bmodnomes
