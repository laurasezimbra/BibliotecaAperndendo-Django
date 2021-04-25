from django.db import models


class Cliente(models.Model):
    Nome = models.CharField('Nome', max_length=100)
    Sobrenome = models.CharField('Sobrenome', max_length=100)
    Email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.Nome} {self.Sobrenome}'


class Livro(models.Model):
    Livro = models.CharField('Livro', max_length=50)
    Autor = models.CharField('Autor', max_length=50)
    Editora = models.CharField('Editora', max_length=30)
    Preco = models.DecimalField('Preço', decimal_places=2, max_digits=4)
    Estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.Livro
    
   
class Venda(models.Model):
    Data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
        Hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
        Data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    Numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da Venda')
        Observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
        Comprovante_venda = models.FileField(upload_to='Comprovante_venda/', verbose_name='Comprovante de Venda')
        Exemplo_upload = models.FileField(upload_to='outro_diretorio/', null=True, blank=True)
        Venda_concluida = models.BooleanField(blank=False, null=False)
