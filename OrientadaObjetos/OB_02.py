class Livro():

    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome desde método é __init__ 
    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self, titulo, isbn):
        
        # Atributos são propriedades
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe.')

    def imprime(self, titulo, isbn):
        print('Foi criado o livro %s com ISBN %d' % (titulo, isbn))    

livro1 = Livro()

livro1.titulo





