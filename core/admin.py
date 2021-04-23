from django.contrib import admin

from .models import Cliente, Livro


class LivroAdmin(admin.ModelAdmin):
    list_display = ('Livro', 'Preco', 'Estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Sobrenome', 'Email')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Livro, LivroAdmin)
