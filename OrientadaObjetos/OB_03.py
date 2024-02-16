class Algoritimo():

    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print('Construtor chamado para criar um objeto desta classe.')
        


algo1 = Algoritimo(tipo_algo = 'Ramdom Forest')
algo2 = Algoritimo(tipo_algo = 'Deep Learning')

print(algo1.tipo)
print(algo2.tipo)