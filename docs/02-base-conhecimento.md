# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Registrar e consultar receitas e despesas do usuário |
| `categorias.json` | JSON | Definir categorias financeiras aceitas pelo agente |
| `orcamento_mensal.json` | JSON | Armazenar orçamento mensal e limites por categoria |
| `resumo_usuario.json` | JSON | Guardar informações básicas do usuário e objetivo financeiro |

---

## Adaptações nos Dados

A base de conhecimento foi personalizada para o contexto do Coink AI, focando em finanças pessoais e controle de gastos mensais. Foram criados arquivos simulados com informações de despesas, receitas, categorias financeiras e orçamento mensal, permitindo que o agente forneça respostas contextualizadas e úteis ao usuário.

Os dados foram estruturados para representar situações reais do dia a dia, como compras em supermercado, transporte, assinaturas, lazer e recebimento de salário.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da aplicação em Python. Sempre que o usuário registra uma nova movimentação, os dados podem ser atualizados e reutilizados durante a sessão.

### Como os dados são usados no prompt?

Os dados são consultados dinamicamente conforme a solicitação do usuário. Informações como total gasto no mês, histórico de transações, categorias e orçamento disponível são inseridas no contexto enviado ao modelo para gerar respostas mais precisas e personalizadas.

---

## Exemplo de Contexto Montado

```txt
Dados do Usuário:
- Nome: Bryan
- Objetivo: Controlar gastos mensais e economizar
- Orçamento Mensal: R$ 3.000
- Gasto Atual no Mês: R$ 1.245
- Saldo Restante: R$ 1.755

Últimas Transações:
- 02/04: Supermercado - R$ 180,50
- 05/04: Uber - R$ 22,00
- 07/04: Netflix - R$ 39,90
- 10/04: Restaurante - R$ 65,00

Categorias Disponíveis:
- Alimentação
- Transporte
- Lazer
- Moradia
- Saúde
- Educação
- Outros
