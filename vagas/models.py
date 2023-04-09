from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    titulo = models.CharField(max_length=255)
    nome_empresa = models.CharField(max_length=255)
    descricao_simplificada = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    curtir = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

"""
user: administrador
password: 123456
"""
