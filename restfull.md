### O QUE É?

```
RESTful
```

> É uma API que utiliza requisições HTTP para extrair, inserir, postar e deletar dados.

> Uma API nada mais é do que um código programável que permite que dois softwares diferentes comuniquem-se entre si.
> As APIs são construídas por dois elementos diferentes. O primeiro é uma especificação que descreve como a informação é trocada entre os programas. O segundo é um software de interface, escrito especificamente para esse propósito e publicado para ser utilizado.
> O software que pretende acessar as funcionalidades e capacidades de uma API é descrito como “call”, já o software que cria a API é descrito como “publish”.

```
SERIALIZER
```

> Os serializadores permitem que dados complexos, como querysets e instâncias de modelo, sejam convertidos em tipos de dados Python nativos que podem ser facilmente renderizados em JSON , XML ou outros tipos de conteúdo. Os serializadores também fornecem desserialização, permitindo que os dados analisados ​​sejam convertidos novamente em tipos complexos, após a primeira validação dos dados recebidos.
> Os serializadores no framework REST funcionam de forma muito semelhante às classes Form e ModelForm do Django. Fornecemos uma classe Serializer que fornece uma maneira poderosa e genérica de controlar a saída de suas respostas, bem como uma classe ModelSerializer que fornece um atalho útil para a criação de serializadores que lidam com instâncias de modelo e consultas.

```
VIEW
```

> Uma função view, ou somente view, é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web. Esta resposta pode ser um conteúdo HTML de uma página, ou um redirecionamento, ou um erro 404, ou um documento XML, ou uma imagem . . . ou qualquer coisa, na verdade. O view em si contém qualquer lógica arbitrária que é necessária para retornar uma resposta. Este código pode ficar em qualquer lugar que você quiser, ao longo do seu Python path. Não há outro requerimento – sem “mágica”, por assim dizer. Por uma questão de colocar o código “em qualquer lugar”, vamos criar um arquivo chamado views.py no diretório mysite, que você criou no capítulo anterior.
