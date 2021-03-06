# Conceptu

## Teste Python - Conceptu

Criação da API REST com Django e Rest Framework.

Utilizei a seguinte stack

* Python 3.8.6
* Django 3.1.5
* Django Rest Framework 3.12.2
* Postgress 12.5
* Pipenv

Aplicação criada em Django Rest Framework, utilizando os conceitos chave da ferramenta.

A Arquitetura que utilizei e aprecio muito, foi baseada no que é apresentado
por [Daniel Feldroy pydanny](https://github.com/pydanny) no
livro [Two Scoops of Django 3.x: Best Practices for the Django Web Framework](https://www.feldroy.com/products/two-scoops-of-django-3-x)

Eu busquei utilizar o que eu costumo chamar de *"pré DDD"*, separando as responsabilidades de cada entidade de forma
separada dentro da pastas apps, mas ainda falta mais partes desse conceito que também venho estudando.

A criação das *views* e *serializers*, eu usei o máximo que o framework me dá e usei as *viewsets* de forma mais
desacoplads, usando as classes que definem o objeto de utilização.

Usando o método que define *GET* e *POST* separadamente, deixando o código mais limpo e simples de interpretar Um
conceito que tentei utilizar é usar na declaração das váriaveis o uso do verbo de ação em inglês e sua função em seguida
para facilitar a leitura da classe.

Para facilitar o deploy da aplicação, no github vá em actions, coloquei um CI para o Heroku para que eu faça o deploy da
aplicação via apenas via pull request e usando conceitos que o Git Flow trás.

Todo esse ambiente eu criei e produzi com o [*Pipenv*](https://pipenv.pypa.io/en/latest/) para isolar ao máximo as dependências do projeto.

Para acessar a aplicação na raiz acesse [conceptu-teste](https://conceptu-teste.herokuapp.com/)

Para cadastrar um produto , há uma rota especifica para isso, caso precise que seja cadastrado com categoria é necessario mencionar os ID's da categoria desejada

Disponibilizei uma documentação auxiliar para facilitar o entendimento que está
em [Swagger](https://conceptu-teste.herokuapp.com/swagger/)
e [Redoc](https://conceptu-teste.herokuapp.com/redoc/)

Caso queira acessar o [banco de dados](https://conceptu-teste.herokuapp.com/lotus/)  use:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ce6593f96dd5aec19237)

```
 - Login : andre.emidio@conceptu.com
 - Senha : sWVWL0$L#&Cf0
```

Licence: MIT