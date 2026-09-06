# Sistema de Fila de Atendimento por Prioridade

Script em Python que organiza uma lista de chamados de atendimento por ordem de prioridade, usando nível de urgência como critério principal e horário de chegada como critério de desempate.

## Contexto

Sistemas de atendimento (suporte técnico, triagem, help desk) raramente atendem por ordem simples de chegada — casos mais urgentes precisam furar a fila. Este projeto simula essa lógica: dado um conjunto de chamados, cada um com um nível de urgência (1 a 5) e um horário de chegada, o programa determina automaticamente a ordem correta de atendimento.

## O que o programa faz

- Recebe uma lista de chamados, cada um com nome, urgência e horário de chegada
- Compara chamados dois a dois, aplicando uma regra de prioridade única:
  - Urgência mais alta é atendida primeiro
  - Em caso de empate na urgência, quem chegou primeiro (menor horário) tem prioridade
- Aplica essa regra repetidamente até organizar a fila completa, do mais ao menos prioritário
- Exibe a fila final, em ordem, no terminal

## A lógica de ordenação

O programa implementa manualmente um algoritmo de ordenação por seleção: a cada rodada, percorre todos os chamados ainda pendentes para encontrar o mais prioritário entre eles, remove esse chamado da lista de pendentes e o acrescenta à fila organizada — repetindo o processo até não sobrar nenhum pendente. Essa abordagem foi escolhida deliberadamente para entender o mecanismo de ordenação por trás dos panos, em vez de usar uma função pronta da linguagem.

## Por que a regra de comparação é única para todos os níveis

Em vez de tratar cada nível de urgência com uma lógica separada, o programa usa **uma única função de comparação**, aplicada a qualquer par de chamados. O comportamento de "prioridade em cascata" (se não há ninguém de urgência 5, passa para urgência 4, e assim por diante) surge naturalmente da aplicação repetida dessa regra única — não é necessário nenhum tratamento especial por nível.

## Como rodar

```bash
python sistema-fila.py
```

## Exemplo de saída

```
• LISTA DE ATENDIMENTOS •
DANILO MENDES DE ASSIS
BRUNO CÉSAR CAVALCANTE
CARLOS ALBERTO BEZERRA DE ALMEIDA
JOSÉ CARLOS PEREIRA
EDUARDO ALVES DO NASCIMENTO
DIEGO DA SILVA CUNHA
ANDERSON NOGUEIRA BASTOS
MARIA APARECIDA DOS SANTOS
FELIPE PRADO DA ROCHA
CARLA MONTENEGRO DIAS
ANA GOUVEIA DE OLIVEIRA
```

## O que este projeto exercitou

- Definição de funções (`def`) para encapsular uma regra de comparação reutilizável
- Retorno de valores (`return`) para reaproveitar o resultado de uma função em outra parte do código
- Estruturas de decisão em cascata (`if`/`elif`/`else`) aninhadas, para critério principal e critério de desempate
- Laço `while`, para repetir um processo um número indeterminado de vezes, até uma condição deixar de ser verdadeira
- Manipulação de listas: `.copy()` (evitar alterar a lista original), `.append()` (construir a fila organizada) e `.remove()` (retirar um item já processado)
- Raciocínio algorítmico: comparação par a par como única ferramenta disponível para ordenar uma coleção inteira

## Tecnologias

- Python 3.14 (apenas biblioteca padrão, sem dependências externas)

## Possíveis evoluções futuras

- Ler a lista de chamados a partir de um arquivo de texto ou entrada do usuário, em vez de lista fixa no código
- Adicionar um terceiro critério de desempate (ex: tipo de atendimento)
- Simular chegada de chamados em tempo real, reorganizando a fila dinamicamente a cada novo chamado
- Comparar o desempenho desta implementação manual com a função `sorted()` nativa do Python, usando uma chave de ordenação customizada