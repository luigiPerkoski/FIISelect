from django.db import models

class Save(models.Model):
    cotacao = models.FloatField()
    ffo_yield = models.FloatField()
    dividend_yield = models.FloatField()
    p_vp = models.FloatField()
    valor_mercado = models.FloatField()
    liquidez = models.FloatField()
    cap_rate = models.FloatField()
    vacancia = models.FloatField()