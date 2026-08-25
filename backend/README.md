# Science Burger Tech — Backend (planejamento)

> **Status atual: não implementado.** Esta pasta existe apenas como
> arquitetura preparatória para o backend que será desenvolvido
> futuramente, 100% em **Python**, preferencialmente com **FastAPI**.

## Por que essa pasta existe agora?

O front-end atual usa dados mockados (ver `js/cardapio.js`) e
funções assíncronas já preparadas para, no futuro, trocarem uma
Promise local por uma chamada `fetch` real (ver comentários
`TODO BACKEND PYTHON` espalhados pelo código). Ter a estrutura de
pastas do backend definida desde já evita uma nova reorganização
completa do projeto quando essa etapa começar.

## Estrutura planejada

```text
backend/
├── app/
│   ├── main.py        # bootstrap da aplicação FastAPI
│   ├── routes/         # um router por recurso (products, orders, contact)
│   ├── models/         # modelos de banco de dados (ORM)
│   ├── schemas/         # schemas Pydantic de request/response
│   ├── services/         # regras de negócio
│   └── database/         # engine/sessão do banco + migrations
├── tests/
├── requirements.txt
└── README.md
```

## Endpoints planejados (documentação, não implementados)

| Método | Rota                | Descrição                                   |
|--------|----------------------|----------------------------------------------|
| GET    | `/api/products`      | Lista todos os produtos do cardápio           |
| GET    | `/api/products/{id}` | Detalhe de um produto                        |
| POST   | `/api/orders`        | Cria um pedido a partir do carrinho          |
| GET    | `/api/orders/{id}`   | Consulta o status de um pedido               |
| POST   | `/api/contact`       | Recebe o envio do formulário de contato       |

## O que NÃO está implementado nesta etapa

- Banco de dados
- Autenticação
- Regras de negócio
- Endpoints funcionais
- Persistência real de pedidos/contato (o front-end usa
  `localStorage` apenas para o carrinho, ver `js/cart.js`)

## Como isso vai se conectar ao front-end

Cada função assíncrona do front-end que hoje resolve dados locais
(`loadProducts()` em `js/cardapio.js`, `createOrder()` em
`js/cart.js`) já está isolada especificamente para que, no futuro,
seu corpo seja substituído por uma chamada `fetch()` para os
endpoints acima — sem precisar alterar quem as chama.
