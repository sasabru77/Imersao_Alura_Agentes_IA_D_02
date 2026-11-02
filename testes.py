"""
Imersão Calculadora IA - Testes Unitários em Python
Arquivo: testes.py

Como executar:
    python testes.py
"""

from calculadora import adicionar, subtrair, multiplicar, dividir, porcentagem, calcular
from agente_ia import obter_proximas_sugestoes

def executar_testes():
    print("Iniciando testes em Python...")

    # Testes das operações
    assert adicionar(10, 5) == 15, "Erro na adição"
    assert subtrair(20, 8) == 12, "Erro na subtração"
    assert multiplicar(4, 5) == 20, "Erro na multiplicação"
    assert dividir(50, 2) == 25, "Erro na divisão"
    assert porcentagem(200, 15) == 30.0, "Erro na porcentagem (15% de 200 deve ser 30)"
    assert porcentagem(500, 10) == 50.0, "Erro na porcentagem (10% de 500 deve ser 50)"

    # Teste de proteção de divisão por zero
    try:
        dividir(10, 0)
        assert False, "Deveria falhar em divisão por zero"
    except ValueError:
        pass

    # Teste da função calcular com todas as 5 operações
    assert calcular('+', 7, 3) == 10
    assert calcular('-', 10, 4) == 6
    assert calcular('*', 3, 3) == 9
    assert calcular('/', 18, 2) == 9
    assert calcular('%', 200, 25) == 50.0

    # Teste do agente Alura IA
    sugestoes = obter_proximas_sugestoes([{"a": 50, "operacao": "+", "b": 50, "resultado": 100}], 100)
    assert len(sugestoes) > 0, "Alura IA deve sugerir ao menos 1 passo"

    print("✅ Todos os testes em Python (incluindo porcentagem %) passaram com sucesso!")

if __name__ == "__main__":
    executar_testes()
