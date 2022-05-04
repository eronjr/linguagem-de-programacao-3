# linguagem-de-programacao-3

Repositório destinado aos arquivos do sistema socilitado na cadeira de linguagem de programação 3 do curso de Ciências da Computação

## Estrutura inicial do projeto

Essa é a estrutura que estamos propondo para o código da aplicação onde irá ter o **client** e o **server** no mesmo repositório com a finalidade de simplificar tendo tudo em um único lugar. Obs: o **server** e **client** não vão compartilhar módulos, cada um terá o seu próprio ambiente de desenvolvimento.

```
|
| -- client     // Diretório onde será hospedado nosso frontend
| -- server     // Diretório onde será hospedado nosso backend
| -- docs       // Diretório onde será hospedado toda documentação da nossa aplicação
```

## Fluxo de git para trabalhar no projeto

- Branchs principais:
  - **Main** contém o código que vai para produção
  - **Develop** é o branch base para criar novas funcionalidades na aplicação.
- Novas features:
  - Executar o comando **git pull origin develop** antes de criar um novo branch **feature** para pegar as atualizações
  - Criar um branch baseado no **develop** onde ele irá possuir a seguinte padrão de nome **feature/nome_da_feature** é a partir dai você começa o seu desenvolvimento
  - Quando finalizar a feature deve enviar o código para o repositório remoto, e abrir uma **pull request** do seu branch feature para a **develop**.
  - Assim que aprovado é mergeado na **develop**.
- Padrão de commit:
  - O commit deve descrever o que você implementou
  - A mensagem deve ser escrita de forma semântica baseada na especificação do [convencional commits](https://www.conventionalcommits.org/en/v1.0.0/).
