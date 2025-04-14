# Documentação do Projeto BrazilTruckTycoon

## Descrição
Este projeto é uma API desenvolvida em Django com Django REST Framework (DRF) e utiliza autenticação JWT (JSON Web Token) com a biblioteca `rest_framework_simplejwt`. Além disso, o projeto está configurado para permitir requisições de diferentes origens utilizando o middleware `django-cors-headers`.

---

## Requisitos

### Versões das Dependências
- **Python**: 3.10 ou superior
- **Django**: 5.2
- **Django REST Framework**: 3.16.0
- **Django REST Framework Simple JWT**: 5.5.0
- **django-cors-headers**: 4.7.0

### Outras Dependências
As dependências adicionais estão listadas no arquivo [`requirements.txt`](requirements.txt).

---

## Como Executar o Projeto

### Passo 1: Clonar o Repositório
Clone o repositório para sua máquina local:
```bash
git clone https://github.com/seu-usuario/BrazilTruckTycoon.git
cd BrazilTruckTycoon
```

### Passo 2: Criar e Ativar um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:
```bash
python -m venv venv
```

Ative o ambiente virtual:
- No Windows:
  ```bash
  venv\Scripts\activate
  ```
- No Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

### Passo 3: Instalar as Dependências
Instale as dependências do projeto utilizando o `pip`:
```bash
pip install -r requirements.txt
```

### Passo 4: Configurar o Banco de Dados
O projeto utiliza SQLite como banco de dados padrão. Para configurar o banco de dados, execute as migrações:
```bash
python manage.py migrate
```

### Passo 5: Criar um Superusuário
Crie um superusuário para acessar o painel administrativo:
```bash
python manage.py createsuperuser
```

### Passo 6: Executar o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

O servidor estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Endpoints Principais

### Autenticação JWT
- Obter Token de Acesso:
  - **URL**: `/api/token/`
  - **Método**: POST
  - **Body**:
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha"
    }
    ```
- Atualizar Token de Acesso:
  - **URL**: `/api/token/refresh/`
  - **Método**: POST
  - **Body**:
    ```json
    {
      "refresh": "seu_refresh_token"
    }
    ```

### Recursos da API
- **Cargos**:
  - Listar, criar, atualizar e deletar cargos no endpoint `/api/cargo/`.

---

## Configurações Importantes

### CORS
O projeto está configurado para permitir requisições de qualquer origem. Caso deseje restringir as origens permitidas, edite a configuração `CORS_ALLOW_ALL_ORIGINS` no arquivo `settings.py`.

### Autenticação
A autenticação padrão utiliza JWT, configurada no `REST_FRAMEWORK` no arquivo `settings.py`.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

---

## Contribuição
---
