from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo