from django.contrib import admin

from .models import Cliente, Livro, Genero, Hq, Mangas, Record, Intrinseca, Darkside, Rocco, Fundamento


class LivroAdmin(admin.ModelAdmin):
    list_display = ('Livro', 'Preco', 'Estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Sobrenome', 'Email')
    
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')
    
class HqAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')
    
class MangasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')
 
class IntrinsecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')

class DarksideAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')
    
class RoccoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')
    
class FundamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'sinopse', 'ano', 'editora', 'edicao', 'preco')    
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Hq, HqAdmin)
admin.site.register(Mangas, MangasAdmin)
admin.site.register(Intrinseca, IntrinsecaAdmin)
admin.site.register(Darkside, DarksideAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Rocco, RoccoAdmin)
admin.site.register(Fundamento, FundamentoAdmin)
