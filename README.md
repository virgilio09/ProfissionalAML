# ProfissionalAML
A.M.L (Autônomo, Microempreendedor, Liberal)
Projeto desenvolvido na disciplina de programação web II
## Como usar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Accesse: http://127.0.0.1:8000/

```
git clone https://github.com/virgilio09/ProfissionalAML.git
cd ProfissionalAML
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Estrutura Básica do projeto
```
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── profissionalAML
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── servicos
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── static
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
└── templates
```
