# 🧪 Automação de Testes — Petstore API + SauceDemo Web

Projeto de automação de testes com cobertura de API REST e Web E2E, desenvolvido com Python, Pytest e Selenium, seguindo o padrão Page Object Model.

---

## 📁 Estrutura do Projeto

```
test-automation/
├── .github/
│   └── workflows/
│       ├── api-tests.yml       # Pipeline CI para testes de API
│       └── web-tests.yml       # Pipeline CI para testes Web
│
├── api-tests/
│   ├── tests/
│   │   ├── test_user.py        # Testes do endpoint /user
│   │   ├── test_pet.py         # Testes do endpoint /pet
│   │   └── test_store.py       # Testes do endpoint /store
│   ├── utils/
│   │   └── api_client.py       # Cliente HTTP reutilizável
│   └── requirements.txt
│
├── web-tests/
│   ├── pages/
│   │   ├── base_page.py        # Classe base (Page Object)
│   │   ├── login_page.py       # Página de login
│   │   ├── inventory_page.py   # Página de produtos
│   │   ├── cart_page.py        # Página do carrinho
│   │   └── checkout_page.py    # Página de checkout
│   ├── tests/
│   │   ├── conftest.py         # Configuração do WebDriver
│   │   └── test_saucedemo.py   # Testes E2E
│   └── requirements.txt
│
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Linguagem principal |
| Pytest | Framework de testes |
| Requests | Chamadas HTTP para API |
| Selenium 4 | Automação Web |
| WebDriver Manager | Gerenciamento automático do ChromeDriver |
| pytest-html | Geração de relatórios HTML |
| GitHub Actions | Pipeline de CI/CD |

---

## ✅ Cenários Automatizados

### 🔌 API — Petstore (`https://petstore.swagger.io/v2`)

**User:**
- Criar usuário
- Buscar usuário por username
- Atualizar usuário
- Login e logout
- Deletar usuário
- Verificar retorno 404 após deleção

**Pet:**
- Criar pet
- Buscar pet por ID
- Atualizar pet
- Buscar pets por status
- Deletar pet
- Verificar retorno 404 após deleção

**Store:**
- Consultar inventário
- Criar pedido
- Buscar pedido por ID
- Deletar pedido
- Verificar retorno 404 após deleção

---

### 🌐 Web — SauceDemo (`https://www.saucedemo.com`)

- Login com credenciais válidas
- Login com credenciais inválidas (validação de erro)
- Adicionar produto ao carrinho
- **Fluxo E2E completo:** Login → Adicionar produtos → Carrinho → Checkout → Confirmação

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.11+
- Google Chrome instalado
- Git

---

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/test-automation.git
cd test-automation
```

---

### 2. Testes de API

```bash
cd api-tests
pip install -r requirements.txt
pytest tests/ -v
```

Para gerar relatório HTML:

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

---

### 3. Testes Web

```bash
cd web-tests
pip install -r requirements.txt
pytest tests/ -v
```

Para gerar relatório HTML:

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

---

## ⚙️ Pipeline de CI/CD (GitHub Actions)

O projeto possui duas pipelines independentes:

- **`api-tests.yml`** → Ativada em push/PR na pasta `api-tests/`
- **`web-tests.yml`** → Ativada em push/PR na pasta `web-tests/`

Ambas podem ser disparadas manualmente via **Actions > Run workflow**.

Ao final de cada execução, um relatório HTML é gerado e disponibilizado como **artefato** para download.

---

## 🏗️ Design Patterns Utilizados

### Page Object Model (POM)
Cada página da aplicação web é representada por uma classe Python separada, encapsulando os seletores e ações daquela página. Isso evita duplicação de código e facilita manutenção.

```
BasePage → LoginPage
         → InventoryPage
         → CartPage
         → CheckoutPage
```

### API Client Centralizado
Um módulo `api_client.py` centraliza as chamadas HTTP, evitando repetição e facilitando mudança de URL base.

---

## 👤 Credenciais de Teste (SauceDemo)

| Usuário | Senha |
|---|---|
| `standard_user` | `secret_sauce` |

---

## 📊 Exemplo de Saída dos Testes

```
api-tests/
========================= test session starts ==========================
tests/test_user.py::test_create_user          PASSED
tests/test_user.py::test_get_user             PASSED
tests/test_user.py::test_update_user          PASSED
tests/test_user.py::test_login_user           PASSED
tests/test_user.py::test_logout_user          PASSED
tests/test_user.py::test_delete_user          PASSED
tests/test_user.py::test_get_deleted_user_returns_404  PASSED
tests/test_pet.py::test_create_pet            PASSED
...
========================= 18 passed in 12.34s ==========================

web-tests/
========================= test session starts ==========================
tests/test_saucedemo.py::test_login_sucesso                PASSED
tests/test_saucedemo.py::test_login_invalido               PASSED
tests/test_saucedemo.py::test_adicionar_produto_ao_carrinho PASSED
tests/test_saucedemo.py::test_fluxo_completo_compra        PASSED
========================= 4 passed in 28.51s ===========================
```
