## Dev Mentor — Proposta Simples (Python OOP)

### Contexto
Este repositório foi preparado para um teste de usabilidade do "Dev Mentor", uma extensão do VS Code que atua como tutor de código: não entrega código pronto, mas analisa o seu código e sugere melhorias e correções.

O projeto agora é um mini-domínio em Python orientado a objetos (pasta `oop_demo/`) com problemas intencionais (code smells) para análise. O objetivo é avaliar o Dev Mentor como tutor — sem editar o código durante o teste.

### Objetivo do projeto (o que implementar/refatorar)
No Python (`oop_demo/models.py`), existem propositalmente:
- God Object (`SystemManager`) com responsabilidades demais.
- Método longo (`process_everything`) misturando regras e formatação.
- Tratamento de erros inconsistente (ora retorna valor especial, ora lança exceção).
- Argumento mutável padrão em `Product` (`tags=[]`).
- Herança com violação de substituição (métodos com semânticas diferentes em `Product` vs `Service`).
- Dados agrupados/obsessão por primitivos (`find_entity(kind, id)`).
- Código morto (funções e campos não usados).

### Critérios de aceitação
ATENÇÃO: Durante o teste, não é para corrigir esses pontos. O objetivo é o Dev Mentor identificar, priorizar e explicar como resolver, com passos e boas práticas, sem fornecer código pronto.

### Pontos intencionais para o Dev Mentor encontrar
Para o Dev Mentor diagnosticar:
- God Object e método longo.
- Padrão mutável, inconsistência de erros e herança problemática.
- Dados agrupados/primários e código morto.

### Escopo e limite
Sem dependências externas. O foco é leitura e análise de OOP/código, sem alterações durante o teste.

### Entregáveis sugeridos
Não há entregáveis técnicos durante o teste. Apenas respostas/orientações do Dev Mentor e anotações do participante.


