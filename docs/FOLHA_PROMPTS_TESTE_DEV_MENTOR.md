## Teste de Usabilidade — Folha de Prompts (Dev Mentor, POO em Python)

Use os prompts abaixo diretamente no Dev Mentor para que a ferramenta ANALISE e PROponha CORREÇÕES (plano de refatoração e passos). Execute-os na ordem.

### 1) Panorama inicial
- Prompt (copiar e colar):
  - "Analise a pasta `oop_demo/` e descreva, em tópicos, o propósito de cada arquivo e como eles se relacionam. Em seguida, gere uma lista priorizada dos 5 principais problemas a corrigir primeiro e por quê."

### 2) cliente.py — correções
- Prompt:
  - "Abra `oop_demo/cliente.p0y`. Identifique riscos de parâmetro mutável padrão e a validação fraca de e-mail. Proponha um plano de correção passo a passo (sem precisar escrever o código completo), incluindo: mudança de assinatura, pontos do código afetados e teste/checagem de regressão. Remova também apresentação do `to_dict` (descrever como separar)."

### 3) produto.py — correções
- Prompt:
  - "Revise `oop_demo/produto.py`. Padronize as regras de desconto (faixa válida, comportamento para valores inválidos) e proponha critérios de aceitação. Indique como extrair formatação do `to_dict` e onde colocar. Liste riscos e rollback."

### 4) pedido.py — correções
- Prompt:
  - "Analise `oop_demo/pedido.py`. Aponte os pontos a corrigir: argumento mutável por padrão, efeito colateral em `total_bruto` e método `fechar` muito longo. Forneça um plano de refatoração em etapas (divisão de responsabilidades, onde mover validações e formatação, e como trocar prints por logs). Inclua uma checklist de testes/validações após as mudanças."

### 5) repositorio.py — correções
- Prompt:
  - "Examine `oop_demo/repositorio.py`. Proponha uma política única de erros/retornos (quando lançar exceção vs retornar Optional/bool) e descreva as mudanças necessárias no arquivo e chamadores. Inclua uma matriz simples decisão→ação e um plano de migração."

### 6) servico_pedidos.py — correções
- Prompt:
  - "Analise `oop_demo/servico_pedidos.py`. Quebre o método orquestrador em funções menores, separe regras de negócio de apresentação e discuta alternativas a passar ids primitivos (ex.: objetos/DTOs). Traga um roteiro de refatoração com ordem sugerida, critérios de sucesso e impactos esperados."

### 7) utils.py — correções
- Prompt:
  - "Revise `oop_demo/utils.py`. Apresente uma estratégia para eliminar estado global e funções genéricas sem uso, incluindo opções (ex.: injeção de dependências, objetos de configuração imutáveis). Forneça passos e riscos."

### 8) Plano integrado e verificação final
- Prompt:
  - "Com base nas propostas anteriores, consolide um plano integrado de refatoração com etapas numeradas, estimativa de esforço, ordem de execução, critérios de aceite por etapa e checagens finais (linters, testes ou verificações manuais). Inclua um plano de rollback por etapa."

### Entrega (PDF)
- Abra este arquivo no VS Code e use: Imprimir → Salvar como PDF (ou extensão Markdown → PDF).


