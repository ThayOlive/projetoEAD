Bem-vindo(a)! 
Welcome!

Este projeto foi desenvolvido com o objetivo de facilitar a disponibilização de cursos de uma empresa, através de links de vídeos no youtube não listados, que são aqueles vídeos que só ficam disponíveis 
se o dono do canal compartilhar o link. Futuramente, pretendo incluir uma API do youtube para inserir videos de modo privado. O proejto possui uma interface responsiva e amigável, 
conta com sistema de autenticação
e foi usado a página de administração do próprio Django para cadastro de cursos, inserção de videos e materias, e cadastro de usuários alunos. 

(English: This project was developed with the objective of facilitating the availability of courses for a company, through of unlisted Youtube video links, which are only acessible if the channel owner 
shares the link. In the future, I intent include a Youtube API to insert private videos. The project has a responsive and friendly interface, also include an authentication system
and was used the page of administration of Django for course registration, video and material insertion, and student user management.)

Tecnologias utilizadas: Python, Django Framework, Banco de Dados PostgreSQL, Bootstrap, HTML e CSS. 
(Tools used: Python, Django Framework, Banco de Dados PostgreSQL, Bootstrap, HTML e CSS. )

Fique a vontade para usar e dar sugestões de melhorias! 
(Feel free to use it and to give suggest for improvements!)

 1º PASSO (1st STEP)
 Clone o repositório com:
 git clone <url do respositorio>
 (Clone the repository with:
 git clone <repository url> )
 
 No console, rode:
 (In the console, run:)
 
 2º PASSO (2nd STEP)
 'python -m virtualenv venv' 

 3º PASSO (3rd STEP)
 ative o ambiente virtual:
 activate the virtual envoirement:
 
 'venv\scripts\activate'

 4º PASSO (4th STEP)
 instale as bibliotecas:
 install the required libraries:
 
 'pip install -r requirements.txt'

 5º PASSO (5th STEP)
 No terminal acesse o diretorio da aplicação:
 In the console, navigate to the application directory:
 
 'cd plataforma'
 
 rode as migrações no seu banco de dados local:
 Run the migrations on your local database:
 
 'python manage.py migrate'

 Por último inicie o servidor:
 Finally, start the server:
 
 'python manage.py runserver'
 

