## Folha do Teste — Dev Mentor (Python OOP)

Esta folha é para você, participante do teste. O Dev Mentor é uma extensão do VS Code que analisa seu código e sugere melhorias sem fornecer código pronto. Durante este teste, você NÃO deve editar o código.

### Objetivo
Usar o Dev Mentor para identificar e explicar problemas de POO no arquivo `oop_demo/models.py`.

### Passo a passo (20–30 min)
1) Preparação (2 min)
   - Abra o projeto no VS Code
   - Rode: `npm install` e depois `npm run dev`

2) Exploração (3–5 min)
   - Abra `oop_demo/models.py`
   - Leia rapidamente e use o Dev Mentor para um diagnóstico inicial. Não altere o arquivo.

3) Tarefas com apoio do Dev Mentor (10–15 min, sem editar o código)
   - Detectar: God Object, método longo, inconsistência de erros.
   - Identificar: argumento mutável padrão, herança problemática (substituição), dados primitivos/agrupados.
   - Apontar código morto (funções/atributos não usados).
   - Solicitar passos de correção em alto nível, riscos e impactos.

4) Revisão final (3–5 min)
   - Rode o app apenas para observar comportamento atual (opcional)
   - Peça ao Dev Mentor um resumo das melhorias sugeridas e próximos passos

### Prompts sugeridos ao Dev Mentor
- "Revise `oop_demo/models.py` e identifique smells (God Object, método longo, erros inconsistentes, mutável padrão, herança). Explique impactos."
- "Sem escrever código, como eliminar o argumento mutável padrão em `Product` e evitar efeitos colaterais?"
- "Proponha uma política única de erros e como aplicá-la nos métodos `add_*` e descontos."
- "A hierarquia `Product`/`Service` viola substituição? Como reorganizar a modelagem?"
- "`find_entity(kind, id)` indica obsessão por primitivos. Quais alternativas orientadas a tipos/classe?"
- "`process_everything` mistura camadas. Como dividir responsabilidades?"

### Critérios de conclusão (sem alterar o código)
 - Você obteve do Dev Mentor um plano claro (em passos) para corrigir:
   - God Object e método longo
   - Política única de erros
   - Arg. mutável padrão e herança/substituição
   - Dados primitivos/agrupados e código morto

### Observações
 - O Dev Mentor não deve fornecer código pronto; apenas orientação.
 - Se travar, peça para priorizar por impacto/rapidez e indicar riscos.


