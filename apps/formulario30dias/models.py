from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

class Formulario(models.Model):
    # Estados de recuperação do paciente pós 30 dias
    class EstadoDeRecuperacao(models.IntegerChoices):
        EXCELENTE = 4, _("Excelente - me sinto muito bem")
        BOA = 3,  _("Boa - estou melhorando")
        REGULAR = 2, _("Regular - ainda tenho dificuldades")
        RUIM = 1, _("Ruim - não estou melhorando")

    class RetornoAtividades(models.IntegerChoices):
        COMPLETAMENTE = 4, _("Sim, completamente")
        PARCIALMENTE = 3, _("Parcialmente")
        AINDA_NAO_CONSIGO = 2, _("Ainda não consigo")
        NAO_SE_APLICA = 1, _("Não se aplica")


        
    estado_de_recuperacao = models.IntegerField(choices=EstadoDeRecuperacao, max_length= 1, default= 1)
    nivel_de_dor = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default= 0)
    retorno_atividades =  models.IntegerField(choices=RetornoAtividades, default= 1)
    satisfacao_resultado = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default= 0)