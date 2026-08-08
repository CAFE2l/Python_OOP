from index import * 


def main():
    f1 = FuncionarioHorista(nome="Paulo",  valor_hora=25, qtd_horas=2000)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = FuncionarioMensalista(nome= "Amanada", salario_bruto=9500)
    f2.calc_sal()
    f2.analisar_sal()



if __name__ == "__main__":
    main()