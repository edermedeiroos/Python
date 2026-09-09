# 🐍 Estudos de Python

Repositório dedicado ao aprendizado, anotações práticas e resolução de exercícios de Python, cobrindo desde os conceitos fundamentais da linguagem até tópicos intermediários e avançados como Programação Orientada a Objetos (POO), iteradores e geradores.

---

## 📌 Conteúdo do Repositório

O projeto é estruturado em duas grandes seções: **Aulas** (exemplos conceituais e guias práticos) e **Exercícios** (resoluções de desafios e cursos).

### 📚 Aulas (`/Aulas`)
Contém exemplos práticos divididos por áreas de estudo:

* **Condições**: Estruturas condicionais (`if`, `elif`, `else`).
* **Iterações**: Iteradores, `Generator`, `IterTools` e protocolos de iteração.
* **Módulos e Funções**: Funções (`def`), funções lambda, closures, decoradores, escopo, recursividade e criação de módulos/pacotes.
* **Operadores**: Operadores aritméticos, lógicos e de comparação.
* **POO (Programação Orientada a Objetos)**:
  * Criação e uso de `Classes`
  * `Encapsulamento`, `Herança` e `Polimorfismo`
  * `Abstração`
  * `Relações` entre classes (associação, agregação, composição)
  * Métodos especiais (`Special Methods` / Dunder methods)
  * `Context Manager` (`with`)
  * Decoradores de classe (`@property`, `@staticmethod`, `@classmethod`)
* **Repetição**: Estruturas de repetição (`for`, `while`, comandos `break` e `continue`).
* **Tipos de Dados**: Manipulação e métodos de tipos primitivos e estruturas de dados:
  * `Int`, `Float`, `Bool`, `Strings`
  * `Listas`, `Tuplas`, `Dicionários`, `Set`
  * Manipulação de `Arquivos`
* **Tratamento de Erros**: Tratamento de exceções (`try/except/finally/else`) e lançamento personalizado (`raise`).
* **Outros**: Tópicos complementares sobre complexidade de código, identidade de objetos (`id`), formatação de cores no terminal e interpretador Python.

---

### 💻 Exercícios (`/Exercícios`)
Desafios e listas de exercícios práticos resolvidos:

* **Curso em Vídeo**: +110 exercícios práticos com foco em lógica, estruturas de dados e bibliotecas padrão.
* **Curso Otávio Miranda**: Exercícios e módulos focados em Python procedural, funcional e boas práticas.
* **Fase Zero**: Materiais e resoluções de desafios de entrada/nivelamento.
* **Python Direto ao Ponto**: Rascunhos e exercícios rápidos de fixação.

---

## 🚀 Como Executar

### Pré-requisitos
* **Python 3.10+** (recomendado Python 3.11 ou superior)
* Git instalado

### 1. Clonar o repositório
```bash
git clone https://github.com/edermedeiroos/estudos-python.git
cd estudos-python
```

### 2. Criar e ativar um ambiente virtual (opcional, porém recomendado)
* **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar qualquer script
Por exemplo, para executar uma aula de POO ou um exercício específico:
```bash
python "Aulas/POO/Classes.py"
python "Exercícios/Curso_em_Video/Ex001.py"
```

---

## 📄 Licença

Este repositório está sob a licença [MIT](LICENSE).
