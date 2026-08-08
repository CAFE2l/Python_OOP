from index import *
from rich.table import Table

def main():
    dist = 10

    moto = Moto(dist)
    carreta = Carreta(dist)
    van = Van(dist)
    

    table = Table("Distancia", "Tipo", "Frete")
    for entrega in [moto, carreta, van]:
        entrega.calc_frete()
        frete_str = f"[bold][green]R${entrega.frete:.1f}[/][/]" if entrega.frete > 0 else "[red]Distancia invalida[/red]"
        table.add_row(f"{dist}Km", type(entrega).__name__, frete_str)
    print(table)

if __name__ == "__main__":
    main()

