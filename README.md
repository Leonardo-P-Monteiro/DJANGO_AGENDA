# DJANGO_AGENDA

Uma aplicação web de agenda de contatos desenvolvida com Django, permitindo gerenciar seus contatos de forma eficiente e organizada.

## 📋 Sobre o Projeto

DJANGO_AGENDA é uma aplicação web que permite aos usuários gerenciar seus contatos pessoais e profissionais. Com uma interface intuitiva, você pode adicionar, editar, excluir e buscar contatos facilmente.

## 🚀 Funcionalidades

- Cadastro e autenticação de usuários
- Adição, edição e remoção de contatos
- Categorização de contatos (trabalho, família, amigos, etc.)
- Busca avançada de contatos
- Visualização detalhada das informações de cada contato
- Responsividade para acesso em diferentes dispositivos

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem de programação
- [Django](https://www.djangoproject.com/) - Framework web
- [HTML/CSS/JavaScript](https://developer.mozilla.org/) - Frontend
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [SQLite](https://www.sqlite.org/) - Banco de dados (desenvolvimento)
- [PostgreSQL](https://www.postgresql.org/) - Banco de dados (produção)
- [Docker](https://www.docker.com/) - Virtualziação

## 📦 Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- virtualenv (opcional, mas recomendado)

### Passos para instalação

1. Clone o repositório:
```bash
git clone https://github.com/Leonardo-P-Monteiro/DJANGO_AGENDA.git
cd DJANGO_AGENDA
```

2. Crie e ative um ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (crie um arquivo .env na raiz do projeto):
```
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário (admin):
```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

8. Acesse a aplicação no navegador:
```
http://127.0.0.1:8000/
```

## 🖼️ Screenshots

*[Adicione screenshots da sua aplicação aqui]*

## 📋 Estrutura do Projeto

```
DJANGO_AGENDA/
├── agenda/                  # Aplicação principal
│   ├── migrations/          # Migrações do banco de dados
│   ├── static/              # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/           # Templates HTML
│   ├── admin.py             # Configuração do admin
│   ├── forms.py             # Formulários
│   ├── models.py            # Modelos do banco de dados
│   ├── urls.py              # URLs da aplicação
│   ├── views.py             # Views da aplicação
├── django_agenda/           # Projeto Django
│   ├── settings.py          # Configurações do projeto
│   ├── urls.py              # URLs do projeto
│   ├── wsgi.py              # Configuração WSGI
├── static/                  # Arquivos estáticos globais
├── media/                   # Uploads de mídia
├── templates/               # Templates globais
├── .gitignore               # Arquivos ignorados pelo Git
├── manage.py                # Script de gestão do Django
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

## 🚀 Deploy

### Para deploy em produção:

1. Configure as variáveis de ambiente para produção
2. Colete arquivos estáticos:
```bash
python manage.py collectstatic
```
3. Configure um servidor web como Nginx ou Apache
4. Use Gunicorn ou uWSGI como servidor WSGI

## 👨‍💻 Autor

[Leonardo P. Monteiro](https://github.com/Leonardo-P-Monteiro)

---

⭐️ Desenvolvido por Leonardo P. Monteiro.
