"""
Calculadora de IMC (Índice de Massa Corporal)
Autora: Amanda Albuquerque Silva
"""


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o IMC a partir do peso (kg) e da altura (m)."""
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    return peso / (altura ** 2)


def classificar_imc(imc: float) -> str:
    """Retorna a classificação do IMC segundo a OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


def ler_float(mensagem: str) -> float:
    """Lê um número decimal do usuário, tratando erros de entrada."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex: 70.5).")


def main():
    print("=" * 40)
    print("        CALCULADORA DE IMC")
    print("=" * 40)

    peso = ler_float("Digite seu peso (kg): ")
    altura = ler_float("Digite sua altura (m), ex 1.70: ")

    try:
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print("\nResultado:")
        print(f"  IMC: {imc:.2f}")
        print(f"  Classificação: {classificacao}")
    except ValueError as erro:
        print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()
