"""
Imersão Calculadora IA - Módulo de Operações Matemáticas
Arquivo: calculadora.py

Contém as 5 operações fundamentais da aplicação:
- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Porcentagem (%) [NOVA OPERAÇÃO ADICIONADA]

Desenvolvido em Python puro para iniciantes.
"""

def adicionar(a: float, b: float) -> float:
    """Retorna a soma de a e b (a + b)."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de b em a (a - b)."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação de a por b (a * b)."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão de a por b (a / b).
    Gera um erro se houver tentativa de divisão por zero.
    """
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a / b


def porcentagem(a: float, b: float) -> float:
    """
    Calcula b por cento de a: (a * b) / 100.
    Exemplo: porcentagem(200, 15) retorna 30.0 (15% de 200).
    """
    return (a * b) / 100.0


def calcular(operacao: str, a: float, b: float) -> float:
    """
    Executa a operação matemática correspondente ao operador.
    Operadores aceitos: '+', '-', '*', '/', '%'
    """
    if operacao == '+':
        return adicionar(a, b)
    elif operacao == '-':
        return subtrair(a, b)
    elif operacao in ('*', 'x', 'X'):
        return multiplicar(a, b)
    elif operacao in ('/', '÷'):
        return dividir(a, b)
    elif operacao == '%':
        return porcentagem(a, b)
    else:
        raise ValueError(f"Operação inválida: '{operacao}'. Use apenas +, -, *, / ou %")
