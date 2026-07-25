from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1 

        print(f":open_boo: u just open the book {self.titulo} that has {self.total_paginas} and u are on the page {self.pagina_atual} of {self.total_paginas}")

    def avancar_pagina(self, qtd=1):
        count = 0 
        for pg in range(0, qtd, 1):
         if not self.fim_livro():
            self.pagina_atual += 1
            print(f"[bold][red]pag{self.pagina_atual} ->[/red][/bold] ", end=" ")
            time.sleep(0.2)
            count  += 1
        print(f"u jump {count} pages, u are on the page [bold][blue]{self.pagina_atual}[/bold][/blue] of {self.total_paginas}")
        if self.fim_livro():
            print(f":closed_book: u arrived at end of the book")
    def fim_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False

        #return True if self.pagina_atual == self.total_paginas else return False




l1 = Livro(titulo="Never Finished", paginas=300)
l1.avancar_pagina(30)
l1.avancar_pagina(15)
l1.avancar_pagina(50)