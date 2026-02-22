# Arquivo-time-machine


Organizador automático de arquivos em Python que separa ficheiros de uma pasta com base na data de modificação. Arquivos com mais de 30 dias são movidos para “livros antigos” e os mais recentes para “livros recentes”. Inclui barra de progresso e tratamento de erros, facilitando a organização automática de diretórios.

---

# 📘 README – Organizador de Arquivos por Data

## 📖 Sobre o Projeto

Este projeto é um sistema de organização automática de arquivos desenvolvido em Python. Ele classifica ficheiros de uma pasta conforme a data da última modificação.

Arquivos com mais de 30 dias são movidos para a pasta **“livros antigos”**, enquanto os mais recentes são enviados para **“livros recentes”**.

---

## ⚙️ Funcionalidades

* ✅ Leitura automática de todos os ficheiros da pasta
* ✅ Verificação da data de modificação
* ✅ Organização automática por tempo (≥ 30 dias)
* ✅ Criação automática de pastas
* ✅ Barra de progresso visual no terminal
* ✅ Tratamento de erros para caminhos inválidos

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* datetime
* os
* shutil
* sys
* Manipulação de ficheiros

---

## 📂 Estrutura Criada Automaticamente

Após execução:

```
📁 Pasta Escolhida
   ├── 📁 livros antigos
   └── 📁 livros recentes
```

---

## 🚀 Como Executar

1. Certifique-se de ter Python instalado.
2. Execute o ficheiro:

```bash
python nome_do_arquivo.py
```

3. Informe o caminho completo da pasta que deseja organizar.

Exemplo:

```
c:/Users/win11/Documents/Projetos
```

---

## 📌 Observações

* Apenas ficheiros são movidos (não pastas).
* Caso o caminho seja inválido, o sistema solicitará nova tentativa.
* A organização é baseada na diferença entre a data atual e a data de modificação do ficheiro.

---


