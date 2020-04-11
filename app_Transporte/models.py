from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length = 50, blank = True, null = True)
    sigla =models.CharField(max_length = 10,  blank = True, null = True)

    def __str__(self):
        return self.nome

class Departamento (models.Model):
    nome = models.CharField(max_length=150,  blank = True, null = True)

    def __str__(self):
        return self.nome

class Funcionario (models.Model):
    nome = models.CharField(max_length = 150,  blank = True, null = True)
    matricula = models.CharField(max_length = 50, blank = True, null = True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.nome, self.cargo)

class Veiculo(models.Model):
    descricao = models.CharField(max_length = 50, blank = True, null = True)
    modelo = models.CharField(max_length = 30, blank = True, null = True)
    placa = models.CharField(max_length = 10, blank = True, null = True)

    def __str__(self):
        return "{} - {}".format(self.modelo,self.placa)

class Solicitacao (models.Model):
    data_hora = models.DateTimeField()
    origem = models.CharField(max_length = 50, blank = True, null = True)
    destino = models.CharField(max_length = 50, blank = True, null = True)
    solicitante = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} - {} - {}".format(self.origem,self.destino,self.data_hora)
    
class Atendimento(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete = models.CASCADE)
    data_hora = models.DateTimeField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.solicitacao,self.veiculo,self.motorista)