# Sistema Web de Gestão de Tarefas

## Descrição

Projeto desenvolvido na disciplina de Laboratório de Programação Back-End.

O sistema foi criado em Python e possui atividades realizadas ao longo das semanas da disciplina, utilizando Git para controle de versão.

## Tecnologias Utilizadas

- Python 3
- Git
- Ambiente Virtual (venv)
- Requests

## Arquivos do Projeto

- `main.py` - Exibe a mensagem inicial do sistema.
- `cadastro_tarefa.py` - Cadastro de tarefas utilizando entrada de dados e operadores.
- `menu_tarefas.py` - Menu para cadastrar, listar e concluir tarefas.
- `requirements.txt` - Dependências do projeto.
- `README.md` - Documentação do projeto.

## Como Executar

Ativar o ambiente virtual:

```bash
.venv\Scripts\activate
```

Instalar as dependências:

```bash
pip install -r requirements.txt
```

Executar o programa principal:

```bash
python main.py
```

Executar o cadastro de tarefas:

```bash
python cadastro_tarefa.py
```

Executar o menu de tarefas:

```bash
python menu_tarefas.py
```

## Menu de Tarefas

O arquivo `menu_tarefas.py` possui as seguintes opções:

1. Cadastrar tarefa
2. Listar tarefas
3. Atualizar situação de uma tarefa
4. Encerrar sistema

## Limitação

As tarefas são armazenadas apenas durante a execução do programa.

Ao fechar o sistema, os dados cadastrados são perdidos.

## Autor

Guilherme