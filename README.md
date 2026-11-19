<h1>- Mini API Flask - Organização, Versionamento e Qualidade</h1>

Projeto desenvolvido para o TDE dos Módulos 1 e 2, abrangendo:
- Organização e Versionamento (Mini API em Flask)
- Estruturação escalável
- Testes automatizados com mock
- Cobertura de testes (pytest-cov)
- Integração com API externa (AwesomeAPI)
- Análise de qualidade com SonarCloud
- GitFlow completo com branches, PRs e commits padronizados

<h1>ESTRUTURA DO PROJETO</h1>

| Pasta / Arquivo                  | Descrição                                           |
|----------------------------------|-----------------------------------------------------|
| `src/`                           | Código-fonte da aplicação                           |
| `src/__init__.py`                | Inicialização do módulo Python                      |
| `src/app.py`                     | Factory principal da aplicação                      |
| `src/config.py`                  | Configurações da aplicação e do banco               |
| `src/extensions.py`              | Inicialização do SQLAlchemy                         |
| `src/models.py`                  | Modelo `Usuario`                                    |
| `src/routes/`                    | Organização das rotas                               |
| `src/routes/routes.py`           | Rotas CRUD dos usuários                             |
| `src/routes/exchange_routes.py`  | Endpoint de câmbio (USD → BRL)                      |
| `src/services/exchange_service.py` | Consumo da AwesomeAPI                             |
| `src/instance/`                  | Arquivos de instância/local                         |
| `tests/`                         | Testes unitários e cobertura                        |
| `coverage.xml`                   | Relatório de cobertura (pytest-cov)                 |
| `sonar-project.properties`       | Configurações do SonarCloud                         |
| `.gitignore`                     | Arquivos ignorados pelo Git                         |
| `requirements.txt`               | Dependências do projeto                             |
| `README.md`                      | Documentação do projeto                             |

<h1>INSTALAÇÃO E EXECUÇÃO LOCAL</h1>

1. Clonar repositório:

<pre>
git clone &lt;URL_DO_REPOSITORIO&gt;
cd miniAPI
</pre>

2. Criar e ativar ambiente virtual:

<pre>
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
</pre>

3. Instalar dependências:

<pre>
pip install -r requirements.txt
</pre>

4. Executar aplicação:

<pre>
python -m src.app
</pre>

<h1>ENDPOINTS OBRIGATÓRIOS</h1>

<h2>CRUD de Usuários</h2>

| Método | Endpoint                 | Descrição                          |
|--------|---------------------------|------------------------------------|
| GET    | `/api/usuarios/`         | Lista todos os usuários            |
| POST   | `/api/usuarios/`         | Cria um novo usuário               |
| PUT    | `/api/usuarios/<id>/`    | Atualiza dados de um usuário       |
| DELETE | `/api/usuarios/<id>/`    | Remove um usuário                  |

<h2>ENDPOINT DO MÓDULO 2 – API DE CÂMBIO</h2>

| Método | Endpoint               | Descrição                                 |
|--------|------------------------|-------------------------------------------|
| GET    | `/exchange/usd-to-brl` | Retorna a cotação atual do dólar (USD → BRL) |

*Implementado utilizando a API externa AwesomeAPI.*

<h1>TESTES E COBERTURA (Módulo 2)</h1>

Teste unitário com **mock da API externa**, conforme exigido:

1. Executar testes:

<pre>
pytest -q
</pre>

2. Gerar relatório de cobertura:

<pre>
pytest --cov=src --cov-report=xml:coverage.xml
</pre>

O arquivo `coverage.xml` é utilizado pelo SonarCloud.

<h1>INTEGRAÇÃO COM SONARCLOUD</h1>

Arquivo obrigatório:

<pre>
sonar-project.properties
</pre>

Conteúdo:

<pre>
sonar.projectKey=miniAPI
sonar.sources=src
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
</pre>

<h1>ESTRATÉGIA DE VERSIONAMENTO E BRANCHES</h1>

| Branch     | Função                                |
|------------|----------------------------------------|
| main       | Versão estável / produção              |
| develop    | Integração de features                 |
| feature/*  | Desenvolvimento de novas funcionalidades |
| fix/*      | Correções                              |
| hotfix/*   | Correções emergenciais                 |

<h1>FLUXO APLICADO (Módulo 2)</h1>

1. Criada branch da feature:

<pre>
git checkout -b feature/exchange-api
</pre>

2. Commits seguindo padrões exigidos:

<pre>
feat(exchange): add usd-to-brl service and endpoint
test(exchange): add mocked awesomeapi test
chore(ci): add sonar properties and coverage
fix(sonar): correct code smells
</pre>

3. Abertura de Pull Request:  
`feature/exchange-api` → `develop`

4. Aplicado o "Loop de Qualidade" até Quality Gate = PASSED.

<h1>AUTORES</h1>

- Matheus T. O. da Penha — matheus.penha@cest.edu.br  
- Meiryelle Gusmão Macedo — meiryelle.macedo@cest.edu.br  
- Jefferson Sousa Sampaio Junior — jefferson.sampaio@cest.edu.br  
- Henrique Augusto Santos Matos — augusto.smatos@cest.edu.br  

<h1>LICENÇA</h1>

Projeto acadêmico — Avaliação dos Módulos 1 e 2 (Mini API Flask + Qualidade + Integração).
