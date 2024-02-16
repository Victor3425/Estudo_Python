class Funcionarios():

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print('Funcionário(a) ' + self.nome + ' tem salário de R$' + str(self.salario) + ' e o cargo é ' + self.cargo)


Func1 = Funcionarios('Mary', 20000, 'Cientista de Dados')

# hasattr perguntando se tem esse atributo
print(hasattr(Func1, 'nome'))

print(hasattr(Func1, 'salario'))

# setattr modifica o atributo
print(setattr(Func1, 'salario',4500))

# getattr mostrar ou pegar esse atributo
print(getattr(Func1, 'salario',4500))

#delattr apagar esse atributo
print(delattr(Func1, 'salario'))

print(hasattr(Func1, 'salario'))

print(Func1.listFunc())