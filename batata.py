class Livro:

    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.pagina_atual = 0

    def abrir_livro(self):

        self.pagina_atual = 1

    def ler_paginas(self, quantidade):

        if self.pagina_atual == 0:
            print("Você precisa abrir o livro primeiro!")
        else:
            self.pagina_atual += quantidade
            if self.pagina_atual > self.numero_paginas:
                self.pagina_atual = self.numero_paginas 

    def exibir_progresso(self):

        paginas_lidas = self.pagina_atual
        paginas_restantes = self.numero_paginas - paginas_lidas
        print(f"Você leu {paginas_lidas} páginas. Faltam {paginas_restantes}.")
