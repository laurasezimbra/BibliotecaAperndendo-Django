from django.db import models


class Cliente(models.Model):
    Nome = models.CharField('Nome', max_length=100)
    Sobrenome = models.CharField('Sobrenome', max_length=100)
    Email = models.EmailField('E-mail', max_length=100)
    Cpf = models.IntegerField('CPF')
    Numero = models.IntegerField('Número')

    def __str__(self):
        return f'{self.Nome} {self.Sobrenome}'


class Livro(models.Model):
    Livro = models.CharField('Livro', max_length=50)
    Autor = models.CharField('Autor', max_length=50)
    Editora = models.CharField('Editora', max_length=30)
    Preco = models.DecimalField('Preço', decimal_places=2, max_digits=4)
    Estoque = models.IntegerField('Quantidade em Estoque')
    Sinopse = models.TextField()
    Ano = models.IntegerField('Ano de lançamento')

    def __str__(self):
        return self.Livro
