from classes import Motorista,Passageiro,Corrida


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create(self):
        # criando corridas
        corridas = []
        while True:
            # Criando passageiro
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            nota = int(input("Digite a nota do passageiro: "))
            passageiro = Passageiro(nome, documento,nota)
            nota = int(input("Digite a nota da corrida: "))
            distancia = int(input("Digite a distância percorrida na corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
            aux = int(input("Deseja adicionar outra corrida? (1 para SIM/ 0 para NAO): "))
            if aux != 1:
                break

        # MOtorista
        nomeM = input("Digite o nome do motorista: ")
        documentoM = input("Digite o documento do motorista: ")
        notaM = int(input("Digite a nota do motorista: "))
        motorista = Motorista(nomeM,documentoM,notaM, corridas,passageiro)
        self.motorista_model.create(motorista)
    
        
    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nome: {motorista['nome']}")
            print(f"Documento: {motorista['documento']}")
            print(f"Nota: {motorista['nota']}")   
            for corrida in motorista.corridas:
                print(f"Nota: {corrida.nota}")
                print(f"Distância: {corrida.distancia}")
                print(f"Valor: {corrida.valor}")
                print("Passageiro:")
                print(f"Nome: {corrida.passageiro.nome}")
                print(f"Documento: {corrida.passageiro.documento}")      

    def update_motorista(self):
        id = input("Enter the id: ")
        nome = input("Insira um novo nome: ")
        documento = input("Insira um novo documento: ")
        nota = int(input("Insira uma nova nota: "))
        self.person_model.update_Motorista(id,nome,documento,nota)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_Motorista(id)
        
    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create ,read, update, delete, quit")
        super().run()
        