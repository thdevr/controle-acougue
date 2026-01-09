from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=10, unique=True, editable=False)
    nome = models.CharField(max_length=120, null=False, blank=False)
    quantidade_kg = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    preco_por_kg = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    custo_por_kg = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    data_validade = models.DateField(null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.codigo:
            ultimo = Produto.objects.all().order_by('id').last()
            if ultimo:
                novo_id = ultimo.id + 1
            else:
                novo_id = 1

            self.codigo = f"P{novo_id:03d}"  # Ex: P001, P045, P120
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nome
    

class Venda(models.Model):
    cod = models.CharField(max_length=10, unique=True, editable=False)
    