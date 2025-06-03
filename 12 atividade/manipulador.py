from conta import ContaCorrente, SeguroDeVida


class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total


if __name__ == '__main__':
    # Criação de contas correntes (tributáveis)
    cc1 = ContaCorrente('123-4', 'João', 1000.0)
    cc2 = ContaCorrente('567-8', 'José', 2000.0)

    # Criação de seguros de vida (tributáveis)
    seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

    # Lista de tributáveis
    lista_tributaveis = [cc1, cc2, seguro1, seguro2]

    # Instancia do manipulador
    manipulador = ManipuladorDeTributaveis()

    # Cálculo total dos impostos
    total = manipulador.calcula_impostos(lista_tributaveis)

    # Impressão do resultado
    print(f"Total de impostos calculados: R$ {total:.2f}")