class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class MatchDatabaseClient(SimpleCLI):
    def __init__(self, match_database):
        super().__init__()
        self.match_database = match_database
        self.add_command("Pais", self.get_pais)
        self.add_command("Filhos", self.get_filhos)
        self.add_command("Irmaos", self.get_irmao)
        self.add_command("Pets", self.get_pets)
        self.add_command("Dono do pet", self.get_dono)
        self.add_command("Relacionamento", self.get_casamento)
        self.add_command("Dados gerais", self.get_dados)
        

    def get_pais(self):
        nome = input("Entre com o nome: ")
        pais = self.match_database.getPais(nome)
        if(pais == []):
            print('Sem dados disponiveis')
        else:
            print("Pais:", pais)

    def get_filhos(self):
        nome = input("Entre com o nome: ")
        filhos = self.match_database.getFilhos(nome)
        if(filhos == []):
           print('Nao tem filhos')
        else:
           print("Filhos:", filhos)

    def get_irmao(self):
        nome = input("Entre com o nome da pessoa: ")
        irmaos = self.match_database.getirmao(nome)
        if(irmaos == []):
            print('Nao tem irmaos')
        else:
            print("Irmaos:", irmaos)

    def get_pets(self):
        pets = self.match_database.getPets()
        print("Pets:", pets)

    def get_dono(self):
        nome = input("Entre com o nome do pet: ")
        dono = self.match_database.getDono(nome)
        print("Dono:", dono)

    def get_casamento(self):
        nome = input("Entre com o nome da pessoa: ")
        casamento_tempo = self.match_database.getCasamentoTempo(nome)
        casamento = self.match_database.getCasamento(nome)
        if(casamento == []):
            print('Solteiro')
        else:
            print('Casado com',casamento,' há',casamento_tempo,' anos')

    def get_dados(self):
        nome = input("Entre com o nome da pessoa: ")
        profissao = self.match_database.getProfissao(nome)
        print("Profissao:", profissao)
        idade = self.match_database.getIdade(nome)
        print("Idade:", idade)
        sexo = self.match_database.getSexo(nome)
        print("Sexo:", sexo)

    def run(self):
        print("Bem-Vindo ao FamilyTime Database!")
        print("Comandos disponiveis:")
        print("Pais,Filhos,Irmaos,Pets,Dono do pet,Relacionamento,Dados gerais, quit")
        super().run()