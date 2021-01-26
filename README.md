# Company Hero

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

Sobre teste unitário, eu estou estudando esse tópico importante e como ainda não tenho uma boa dicção nessa técnica
achei por bem não incluir, entretanto, como já trabalho com *API's*, inclui a
ferramenta [ScanAPI](https://pypi.org/project/scanapi), que é usada para criar testes de integração para os *endpoints*.

Caso baixe o projeto e queira executar o comando é

```
scanapi run scanapi/company_hero.yaml
```

Para facilitar o deploy da aplicação, no github vá em actions, coloquei um CI para o Heroku para que eu faça o deploy da
aplicação via apenas via pull request e usando conceitos que o Git Flow trás.

Todo esse ambiente eu criei e produzi com o *Pipenv* para isolar ao máximo as dependências do projeto.

Os modelos foram criados, sendo que a relação fica disposta em empresas, para tão é necessário criar primeiro o usuário
que deseja, e depois criar a empresa, relacionando seus funcionários

Para acessar a aplicação na raiz acesse [conceptu-teste](https://conceptu-teste.herokuapp.com/)

Disponibilizei uma documentação auxiliar para facilitar o entendimento que está
em [Swagger](https://conceptu-teste.herokuapp.com/swagger/)
e [Redoc](https://conceptu-teste.herokuapp.com/redoc/)

Caso queira acessar o [banco de dados](https://conceptu-teste.herokuapp.com/lotus/)  use:

```
 - Login : andre.emidio@conceptu.com
 - Senha : sWVWL0$L#&Cf0
```

Licence: MIT