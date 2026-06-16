# 🛒 Sistema de Compras em Python

Sistema de caixa virtual em Python

---
# 📌 O que é esse sistema?

Nosso sistema é um caixa virtual simples e completo.
Assim como uma operadora de caixa que passa o código de barras,
aqui você digita o nome do produto, o preço e a quantidade —
tudo pelo computador, de forma prática e rápida.

 Se a compra passar de R$ 100,00, o sistema aplica
automaticamente um desconto de 10% no total.
Como uma operadora de caixa, porém virtual.

---
 Requisitos

- Computador (o sistema não roda em celular)
- Windows (Utilizando o comando python)
- Linux e macOS (Utilizando o comando python3)
- Biblioteca customtkinter instalada (para o Mini PDV com interface gráfica)


pip install customtkinter


---

 Versões do Sistema

 Versão 1 — Sistema de Compras no Terminal

Versão simples que roda direto no terminal. O operador digita
os dados pelo teclado e o resultado aparece como texto.

Como usar:

Passo 1 — Digite o produto
Assim como uma operadora passava o código de barras, aqui você
digita o nome do produto no sistema.

Passo 2 — Informe a quantidade
Depois de digitar o produto, o sistema pergunta quantas unidades
você quer adicionar.

Passo 3 — Continue ou finalize
Você pode continuar adicionando mais produtos à vontade.
Quando terminar, o sistema soma tudo e aplica o desconto
de 10% automaticamente se o total passar de R$ 100,00.

Exemplo de uso:

```
Digite o nome do produto: Arroz
Digite o preço do produto: R$ 5.00
Digite a quantidade de 'Arroz': 3
Deseja adicionar mais itens? (s/n): n

--- RESUMO DA COMPRA ---
Total sem desconto: R$ 15.00
Nenhum desconto aplicado.
Total a pagar: R$ 15.00
```

---

 Versão 2 — Mini PDV com Interface Gráfica

Versão avançada com janela gráfica em modo escuro (Dark Mode),
botões coloridos e geração de cupom fiscal na tela —
igual ao caixa de um mercado de verdade.

Como usar:

1. Preencha os campos: Nome do Produto, Preço Unitário e Quantidade
2. Clique em **Adicionar Item** para lançar o produto no carrinho
3. Repita para cada produto da compra
4. Clique em **Emitir Nota Fiscal** para fechar a venda e gerar o cupom

Exemplo de cupom gerado:

```
=============================================
           NOTA FISCAL DE VENDA
=============================================
 ITEM               QTD   PRECO     TOTAL
---------------------------------------------
 Arroz               3      5.00     15.00
 Feijão              2      8.00     16.00
---------------------------------------------
 Subtotal Bruto:               R$     31.00
 Desconto Aplicado (10%):      R$      0.00
---------------------------------------------
 TOTAL A PAGAR:                R$     31.00
=============================================
        OBRIGADO PELA PREFERÊNCIA!
=============================================
```


 Funcionalidades

- Registrar produtos com nome, preço e quantidade
- Permitir adicionar vários itens na mesma compra
- Calcular o total automaticamente
- Aplicar desconto de 10% para compras acima de R$ 100,00
- Exibir resumo final da compra
- Interface gráfica moderna com cupom fiscal formatado (Versão 2)
- Validação de dados — protege contra erros de digitação
- Reset automático do caixa após emissão da nota

  Como o sistema funciona por dentro

 Bibliotecas utilizadas

- *customtkinter*: responsável pela janela gráfica, botões,
  campos de texto e o modo escuro (Dark Mode)

 Principais funções

| Função | O que faz |
|---|---|
| `__init__` | Desenha toda a janela e os elementos visuais na tela |
| `adicionar_item` | Captura os dados digitados, calcula o subtotal e adiciona ao carrinho |
| `emitir_nota_fiscal` | Aplica o desconto, gera o cupom formatado e reseta o caixa |

Regra de negócio

Se o total da compra ultrapassar R$ 100,00, o sistema aplica
automaticamente 10% de desconto sobre o valor total.

👩‍💻 Desenvolvido por alunos da Escola da Nuvem

## 👥 Estrutura da Equipe e Engenharia Colaborativa

O projeto foi desenvolvido em formato de Startup (GMD) através do Discord, simulando um fluxo real de engenharia de software no mercado de trabalho:

* **Derli Joaquim de Souza (Desenvolvedor da Inteligência de Negócio)** 
  * Responsável pela criação da lógica matemática inicial em terminal, estruturando o algoritmo de soma contínua e a regra de negócio principal para aplicação automatizada do desconto de 10%.
* **Maiara Souza de Castro (Engenheira de Software e Interface)** 
  * Responsável pela refatoração e evolução do sistema, realizando a migração completa do terminal para uma Interface Gráfica Avançada (GUI) com CustomTkinter, arquitetura orientada a objetos (classes), segurança e tratamento de dados (`try/except`) e estilização da nota fiscal.
* **Gabriela Silva (Gerência de Configuração e QA)**
  * Responsável pela infraestrutura do repositório original no GitHub, gerenciamento de acessos da equipe e testes de qualidade do software.

 Atualizando papéis da equipe no README.
