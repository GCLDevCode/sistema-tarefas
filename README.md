Sistema Web de Gestão de Tarefas
Descrição

Este projeto corresponde à estrutura inicial de um Sistema Web de Gestão de Tarefas desenvolvido na disciplina de Laboratório de Programação Back-End.

O objetivo desta etapa é criar uma base reproduzível para o projeto, contendo ambiente virtual Python, gerenciamento de dependências, documentação básica e controle de versão com Git.

Objetivos da atividade
Criar a estrutura inicial do projeto.
Configurar um ambiente virtual Python.
Instalar e registrar dependências.
Utilizar controle de versão com Git.
Documentar o processo de execução do sistema.
Tecnologias utilizadas
Python 3
Git
Ambiente Virtual (venv)
Biblioteca Requests
Estrutura do projeto
sistema-tarefas/
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
└── .venv/
Arquivos

main.py

Arquivo principal da aplicação.
Exibe a mensagem inicial do sistema.

requirements.txt

Lista as dependências instaladas no projeto.
Permite recriar o ambiente em outro computador.

.gitignore

Define arquivos e pastas que não devem ser versionados pelo Git.
Neste projeto, a pasta .venv é ignorada.

README.md

Documento com informações sobre o projeto e instruções de execução.
Pré-requisitos

Antes de executar o projeto, é necessário possuir:

Python 3 instalado.
Git instalado (opcional para controle de versão).
Terminal ou prompt de comando.
Configuração do ambiente virtual

Criar o ambiente virtual:

python -m venv .venv
Ativação no Windows
.venv\Scripts\activate
Ativação no Linux/macOS
source .venv/bin/activate
Instalação das dependências

Com o ambiente virtual ativado:

pip install -r requirements.txt
Execução do projeto

Execute o arquivo principal:

python main.py

Saída esperada:

Sistema Web de Gestão de Tarefas
Controle de versão

Inicialização do repositório Git:

git init
git add .
git commit -m "Cria estrutura inicial do projeto"
Autor

Guilherme

Observações

Este projeto representa a primeira etapa do desenvolvimento do Sistema Web de Gestão de Tarefas e será expandido ao longo das próximas aulas da disciplina.