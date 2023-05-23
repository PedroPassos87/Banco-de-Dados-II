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


class TeacherCLI(SimpleCLI):
    def __init__(self, db):
        super().__init__()
        self.model = db
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)

    def create(self):
        name = input("Insira o nome: ")
        ano_nasc = input("Insira o ano de nascimento: ")
        cpf = input("Insira o cpf: ")
        self.model.create_teacher(name,ano_nasc,cpf)

    def read(self):
        nome = input("Entre com o nome: ")
        result = self.model.read_teacher(nome)
        if result:
            name, ano_nasc, cpf = result[0]  
            print("Name:", name)
            print("Ano de Nascimento:", ano_nasc)
            print("CPF:", cpf)
            
    def update(self):
        nome = input("Entre com o nome: ")
        cpf = input("Insira um novo cpf: ")
        self.model.update_teacher(nome,cpf)

    def delete(self):
        nome = input("Entre com o nome: ")
        self.model.delete_teacher(nome)
        
    def run(self):
        print("Bem vindo ao TeacherCLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        