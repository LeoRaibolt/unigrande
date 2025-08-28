from tortoise import fields, models
from datetime import datetime
class periodoLetivo(models.Model):
    id: int = fields.IntField(pk=True)
    ano: int = fields.IntField() #ano que pode ser 2020, 2025
    semestre: int = fields.IntField() #semestre que pode ser 1 ou 2
    data_inicio: datetime = fields.DatetimeField()
    data_fim: datetime = fields.DatetimeField()

    class Meta:
        table = "periodo_letivo"
        unique_together = (("ano", "semestre"),)
        indexes = (("ano", "semestre"),)

    class professor(models.Model):
        pass

    class curso(models.Model):
        pass

    class Disciplina(models.Model):
        pass

    class Matriz(models.Model):
        pass

    class Turma(models.Model):
        pass

    class Aluno(models.Model):
        pass

    class Matricula(models.Model):
        pass

    class Historico(models.Model):
        pass
