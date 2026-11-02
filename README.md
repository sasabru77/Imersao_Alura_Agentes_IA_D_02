# 🧮 Imersão Calculadora IA

Calculadora simples em Python desenvolvida para a **Imersão Alura Agentes IA**.
Ela possui **5 operações matemáticas** e um agente de inteligência artificial (**Alura IA**) que sugere o próximo passo de cálculo com base nos seus resultados anteriores.

---

## ➕ Operações Disponíveis

* **Adição (`+`)**: Soma dois números (ex: `10 + 5 = 15`)
* **Subtração (`-`)**: Subtrai dois números (ex: `20 - 8 = 12`)
* **Multiplicação (`*`)**: Multiplica dois números (ex: `4 * 5 = 20`)
* **Divisão (`/`)**: Divide dois números com proteção contra divisão por zero (ex: `50 / 2 = 25`)
* **Porcentagem (`%`)** *(Nova operação adicionada)*: Calcula a taxa percentual de um valor (ex: `200 % 15 = 30`, ou seja, 15% de 200)

---

## 📁 Arquivos do Projeto

* **`calculadora.py`**: Funções das 5 operações matemáticas (adição, subtração, multiplicação, divisão e porcentagem).
* **`agente_ia.py`**: Inteligência da Alura IA que analisa o histórico e sugere os próximos passos.
* **`main.py`**: Programa interativo para rodar no terminal.
* **`app.py`**: Ponto de entrada direto.
* **`testes.py`**: Testes simples para conferir se todas as 5 operações estão funcionando.
* **`requirements.txt`**: Dependências do projeto.

---

## 🚀 Como Rodar

### 1. Iniciar a Calculadora
No seu terminal, digite:
```bash
python main.py
```

### 2. Rodar os Testes
Para testar todas as operações (incluindo a nova operação de porcentagem):
```bash
python testes.py
```

---

## 🤖 Como a Alura IA Funciona

1. Você digita um número e escolhe uma operação (`+`, `-`, `*`, `/`, `%`).
2. Após o resultado, a **Alura IA** sugere até 3 opções lógicas (ex: calcular 10% do valor com `% 10`, parcelar em 2x ou 3x, etc.).
3. Basta digitar `1`, `2` ou `3` para aplicar a sugestão direto na conta!
