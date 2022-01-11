darkconflicts

Projeto de um jogo onde você será um hacker e fara missoes, dinheiro com virus, destruir servidores (bots do jogo, e jogadores reais)...


Como utilizar

Clona repositório

git clone https://github.com/mwkresolve/darkconflicts.git

cd darkconflicts

Preparando o ambiente virtual

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

Roda as migrações

python manage.py migrate

Criar superusuario

python manage.py createsuperuser

Inicia o servidor

python manage.py runserver

Popular o banco de dados com as informações do jogo
acesse http://127.0.0.1:8000/controller e clique nos botões na ordem de cima pra baixo
para gerar os softwares, os bots, os hardwares... por enquanto é o que temos..

Qualquer ajuda é bem vinda :)
