
Minha versão do sistema desenvolvido para o curso de Django da Jornada de Cursos do CITI-CIN/UFPE. 
O Djangram é uma rede social inspirada no Instagram e desenvolvida utilizando o framework Django, HTML e CSS.


## Como utilizar
* Clona repositório
  ```bash
  $ git clone https://github.com/mwkresolve/darkconflicts.git
  $ cd darkconflicts
  ```
* Preparando o ambiente virtual
  ```bash
  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  ```
* Roda as migrações
  ```bash
  $ python manage.py migrate
  ```

* Criar superusuario
  ```bash
  $ python manage.py createsuperuser
  ```

* Inicia o servidor
  ```bash
  $ python manage.py runserver
  ```

* Popular o banco de dados com as informações do jogo
  ```bash
  $ acesse http://127.0.0.1:8000/controller e clique nos botões na ordem de cima pra baixo
  $ para gerar os softwares, os bots, os hardwares... por enquanto é o que temos..
  ```
Qualquer ajuda é bem vinda :)


