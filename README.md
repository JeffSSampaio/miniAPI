<h1>- Mini API Flask - Organiza;'ao e Versionamento</h1>

(Projeto desenvolvido para o TDE - Modulo 1. Organizacao e Versionamento (Mini API em Flask), considerando a estruturacao
de escalabilidade e suportar evolucao futura com versionamento Git e documentacao clara.

ESTRUTURA DO PROJETO
miniAPI/
│
├── src/
│   ├── __init__.py
│   ├── app.py              # factory principal
│   ├── config.py           # configuração da aplicação e banco
│   ├── extensions.py       # inicialização do SQLAlchemy
│   ├── models.py           # modelo Usuario
│   ├── routes.py           # rotas CRUD
│   ├── instance/
│   │   └── api.db          # banco SQLite local
│   └── __pycache__/        # arquivos compilados (ignorados)
│
├── tests/                  # reservado para testes (Módulo 2)
├── .gitignore
├── requirements.txt
└── README.md

<h1>INSTALACAO E EXECUCAO LOCAL</h1>
1. Clonar o repositorio.

      * git clone <URL_DO_REPOSITORIO>
         * cd miniAPI

2. Criar e ativar ambiente virtual.

       * python -m venv maquinavirtual
       * source maquinavirtual/bin/activate   # Linux/Mac
       * maquinavirtual\Scripts\activate      # Windows

4. Instalar dependencias.

       * pip install -r requirements.txt

6. Executar a aplicacao.
   
       * python src/app.py

<h1>ENDPOINS OBRIGATORIOS</h1>

## 🚀 Endpoints Disponíveis

| Método | Endpoint               | Descrição                                |
|--------|------------------------|------------------------------------------|
| **GET**    | `/api/usuarios/`         | Lista todos os usuários cadastrados      |
| **POST**   | `/api/usuarios/`         | Cria um novo usuário (`JSON: nome, email`) |
| **PUT**    | `/api/usuarios/<id>/`    | Atualiza dados de um usuário existente   |
| **DELETE** | `/api/usuarios/<id>/`    | Remove um usuário                        |


<h1>TECNOLOGIAS UTILIZADAS</h1>

* Python 3.12
* Flask 3.1.2
* Flask-SQLAlchemy 3.1.0
* Flask-Migrate 4.0.0
* SQLite (banco local)

<h1>ESTRATEGIA DE VERSIONAMENTO E BRANCHES</h1>

Branch	            Função
main	              versão estável / produção
develop	            integração de features antes do merge em main
feature/*	          desenvolvimento de novas funcionalidades
hotfix/*	          correções emergenciais

<h1>FLUXO APLICADO</h1>
* Criada a branch develop a partir de main.
* Criadas features como feature/create-app, feat/config-db, feature/routes.
* Cada feature teve commits e PRs abertos e mergeados em develop e, depois, em main.

<h1>PRINCIPAIS COMMITS:</h1>

* feat: criar estrutura inicial do app Flask
* feat: inicialização do DB, adição do factory do Flask
* feat: model de usuário criado
* feat: adicionado requisições GET/POST/PUT/DELETE
* fix: corrigir imports e inicializar db
* chore: atualizar .gitignore e remover venv do git

<h1>AUTORES:</h1>

* Matheus T. O. da Penha  matheus.penha@cest.edu.br 
* Meiryelle Gusmão Macedo meiryelle.macedo@cest.edu.br
* Jefferson Sousa Sampaio Junior jefferson.sampaio@cest.edu.br
* Henrique Augusto Santos Matos augusto.smatos@cest.edu.br

Licença
Este projeto é acadêmico e faz parte da avaliação do Módulo 1 — Organização e Versionamento (Mini API em Flask).


