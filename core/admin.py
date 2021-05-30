from django.contrib import admin

from .models import Cliente, Livro, Genero


class LivroAdmin(admin.ModelAdmin):
    list_display = ('Livro', 'Preco', 'Estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Sobrenome', 'Email')
    
class GeneroAdmin(admin.ModelAdmin):]
    list_display = ('Nome', 'Autor', 'Sinopse', 'Ano', 'Editora', 'Edição', 'Preço')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Genero, GeneroAdmin)
