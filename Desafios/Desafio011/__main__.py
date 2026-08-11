from index import * 
from rich import print, inspect

def main():
    f1 = Horista(nome="Paulo",  valor_hora=12, horas_trab=200)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista(nome="Amanada", sal_fixo=9500)
    f2.calc_sal()
    f2.analisar_sal()



if __name__ == "__main__":
    main()