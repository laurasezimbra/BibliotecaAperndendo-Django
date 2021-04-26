from django.db import models


class Cliente(models.Model):
    Nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    Sobrenome = models.CharField('Sobrenome', max_length=100, blank=False, null=False)
    Email = models.EmailField('E-mail', max_length=100, blank=False, null=False)

    def __str__(self):
        return f'{self.Nome} {self.Sobrenome}'


class Livro(models.Model):
    Livro = models.CharField('Livro', max_length=50, blank=False, null=False)
    Autor = models.CharField('Autor', max_length=50, blank=False, null=False)
    Editora = models.CharField('Editora', max_length=30, blank=False, null=False)
    Preco = models.DecimalField('Preço', decimal_places=2, max_digits=4, blank=False, null=False)
    Estoque = models.IntegerField('Quantidade em Estoque', blank=False, null=False)

    def __str__(self):
        return self.Livro
    
   
class Venda(models.Model):
    Data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    Data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    Numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da Venda')
    Observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    Comprovante_venda = models.FileField(upload_to='Comprovante_venda/', verbose_name='Comprovante de Venda')
    Exemplo_upload = models.FileField(upload_to='outro_diretorio/', null=True, blank=True)
    Venda_concluida = models.BooleanField(blank=False, null=False)
