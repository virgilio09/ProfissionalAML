# ProfissionalAML
A.M.L (Autônomo, Microempreendedor, Liberal)
Projeto desenvolvido na disciplina de programação web II
## Como usar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
```
git clone https://github.com/virgilio09/ProfissionalAML.git
cd ProfissionalAML
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```