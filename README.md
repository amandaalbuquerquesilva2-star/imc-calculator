# Calculadora de IMC

Uma calculadora de Índice de Massa Corporal (IMC) simples, feita em Python, que roda direto no terminal.

## 📋 Descrição

Este projeto calcula o IMC de uma pessoa a partir do peso (kg) e da altura (m), e retorna a classificação correspondente segundo as faixas da OMS (Organização Mundial da Saúde):

- Abaixo do peso
- Peso normal
- Sobrepeso
- Obesidade grau I
- Obesidade grau II
- Obesidade grau III

O código é organizado em funções puras e testáveis, com tratamento de erros para entradas inválidas (peso ou altura menores ou iguais a zero, ou valores não numéricos).

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/) (linguagem principal)
- [pytest](https://docs.pytest.org/) (testes automatizados)

## 🚀 Como rodar

### Pré-requisitos

- Python 3.8 ou superior instalado ([python.org](https://www.python.org/downloads/))

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/amandaalbuquerquesilva2-star/imc-calculator.git
   cd imc-calculator
   ```

2. (Opcional, mas recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. Execute o programa:
   ```bash
   python imc.py
   ```

4. Digite o peso e a altura quando solicitado:
   ```
   Digite seu peso (kg): 70
   Digite sua altura (m), ex 1.70: 1.75

   Resultado:
     IMC: 22.86
     Classificação: Peso normal
   ```

### Rodando os testes

Instale o pytest e execute:
```bash
pip install pytest
pytest
```

## 📁 Estrutura do projeto

```
imc-calculator/
├── imc.py          # Script principal (lógica + interface de terminal)
├── test_imc.py      # Testes automatizados
├── LICENSE          # Licença MIT
├── .gitignore
└── README.md
```

## 📄 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✍️ Autora

Amanda Albuquerque Silva
