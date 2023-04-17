class Passageiro:
    def __init__(self,nome:str, documento:str,nota:int):
        self.nome = nome
        self.documento = documento
        self.nota = nota


class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro


class Motorista:
    def __init__(self, nome:str, documento:str,nota:int,corridas:list,passageiro:object):
        self.nome = nome
        self.documento = documento
        self.nota = nota
        self.corridas = corridas
        self.cliente = passageiro

    
    