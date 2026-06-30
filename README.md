````markdown
# 📚 Caderno Temático - Inteligência Artificial aplicada à Engenharia de Confiabilidade (SRE)

> Projeto desenvolvido como parte do desafio da DIO para explorar o uso do **NotebookLM** como ferramenta de aprendizagem ativa, utilizando Inteligência Artificial para organização do conhecimento, curadoria de conteúdo e construção de um guia de estudos técnico.

---

# 🚀 Objetivo

Este projeto demonstra como utilizar o **NotebookLM** para estudar um tema técnico de forma estruturada, explorando documentação oficial, artigos técnicos e boas práticas da indústria.

O tema escolhido foi **Inteligência Artificial aplicada à Engenharia de Confiabilidade (Site Reliability Engineering - SRE)**, com foco em compreender como modelos de IA podem apoiar equipes de operações na análise de incidentes, observabilidade e automação.

Ao final deste estudo, espera-se compreender como a IA pode auxiliar em:

- Observabilidade
- Análise automática de logs
- Correlação de eventos
- Detecção de anomalias
- Resposta automatizada a incidentes
- Geração de playbooks
- AIOps
- Engenharia de Prompt

---

# 🎯 Objetivos de Aprendizagem

- Entender os fundamentos de AIOps.
- Estudar como LLMs podem auxiliar equipes SRE.
- Conhecer ferramentas modernas de observabilidade.
- Aprender técnicas de Engenharia de Prompts.
- Criar uma biblioteca de prompts reutilizáveis.
- Consolidar o conhecimento em um guia de estudos.

---

# 📖 Curadoria de Fontes

As seguintes fontes abertas foram utilizadas para alimentar o NotebookLM.

| Fonte | Link |
|--------|------|
| Google SRE Book | https://sre.google/books/ |
| NIST AI Risk Management Framework | https://www.nist.gov/itl/ai-risk-management-framework |
| MITRE ATT&CK Framework | https://attack.mitre.org/ |
| Kubernetes Documentation | https://kubernetes.io/docs/ |
| OpenTelemetry Documentation | https://opentelemetry.io/docs/ |

---

# 🤖 Engenharia de Prompts

Durante o estudo foram testados diversos prompts para avaliar a qualidade das respostas do NotebookLM.

---

## Prompt 1

### Objetivo

Compreender o conceito de AIOps.

**Prompt**

```text
Explique o conceito de AIOps considerando ambientes Kubernetes.
```

### Resultado

Resposta ampla e introdutória.

### Ajuste realizado

```text
Explique AIOps considerando clusters Kubernetes em produção, apresentando exemplos utilizando Prometheus, Grafana, Loki e OpenTelemetry.
```

### Resultado

Resposta muito mais detalhada e contextualizada.

---

## Prompt 2

### Objetivo

Entender como um LLM pode apoiar um SRE.

**Prompt**

```text
Como um modelo de linguagem pode auxiliar um engenheiro SRE durante um incidente crítico?
```

### Resultado

Excelente correlação entre documentação oficial e conceitos técnicos.

---

## Prompt 3

### Objetivo

Criar um fluxo operacional.

**Prompt**

```text
Gere um playbook para resposta a incidentes baseado nas práticas do Google SRE.
```

### Ajuste

```text
Inclua um fluxograma textual das etapas.
```

---

## Prompt 4

### Objetivo

Comparação técnica.

```text
Compare observabilidade tradicional com AIOps utilizando uma tabela.
```

---

## Prompt 5

### Objetivo

Gerar material para entrevistas.

```text
Quais perguntas podem ser feitas em uma entrevista para SRE envolvendo AIOps?
```

---

# ⚠️ Cicatrizes (Troubleshooting)

Durante o desenvolvimento foram encontrados alguns desafios.

## Problema 1

Respostas muito genéricas.

### Solução

Adicionar contexto detalhado ao prompt.

---

## Problema 2

Mistura entre IA Generativa e Machine Learning.

### Solução

Solicitar que apenas as fontes carregadas fossem utilizadas.

---

## Problema 3

Respostas muito longas.

### Solução

Adicionar limite de tamanho.

```text
Responda em até 300 palavras.
```

---

## Problema 4

Poucos exemplos práticos.

### Solução

Solicitar explicitamente.

```text
Inclua exemplos reais de produção.
```

---

# 📚 Miniguia de Estudos

## O que é AIOps?

AIOps (Artificial Intelligence for IT Operations) é a aplicação de Inteligência Artificial para automatizar operações de infraestrutura, monitoramento e resposta a incidentes.

### Benefícios

- Detecção automática de anomalias
- Correlação de eventos
- Redução do MTTR
- Automação operacional
- Análise inteligente de logs
- Predição de falhas

---

## Observabilidade

A observabilidade permite compreender o estado interno de um sistema por meio de dados gerados durante sua operação.

### Os três pilares

- Logs
- Métricas
- Traces

### Ferramentas

- Prometheus
- Grafana
- Loki
- Jaeger
- OpenTelemetry

---

## IA aplicada ao SRE

Principais aplicações:

- Classificação automática de incidentes
- Correlação inteligente de eventos
- Geração automática de RCA
- Criação de playbooks
- Sumarização de logs
- Recomendações de ações corretivas

---

## Engenharia de Prompt

Boas práticas:

- Informar contexto
- Definir objetivo
- Limitar tamanho da resposta
- Solicitar referências
- Pedir exemplos práticos
- Definir formato esperado

---

# 📖 Glossário

| Termo | Definição |
|---------|-----------|
| AIOps | Artificial Intelligence for IT Operations |
| RCA | Root Cause Analysis |
| LLM | Large Language Model |
| MTTR | Mean Time To Recovery |
| MTBF | Mean Time Between Failures |
| Observabilidade | Capacidade de compreender o comportamento interno de um sistema através de seus dados |
| SLI | Service Level Indicator |
| SLO | Service Level Objective |
| SLA | Service Level Agreement |
| Trace | Caminho completo percorrido por uma requisição |

---

# 💡 Biblioteca de Prompts

## Explicação

```text
Explique o conceito abaixo considerando um ambiente Kubernetes em produção.
```

---

## Comparação

```text
Compare as tecnologias abaixo apresentando vantagens, desvantagens, limitações e casos de uso.
```

---

## Resumo

```text
Faça um resumo executivo do documento contendo os principais conceitos em até 500 palavras.
```

---

## Flashcards

```text
Crie 20 flashcards para revisão rápida.
```

---

## Quiz

```text
Crie um quiz com 15 perguntas de múltipla escolha e apresente o gabarito ao final.
```

---

## Roadmap

```text
Monte um plano de estudos de 30 dias baseado apenas nos documentos carregados.
```

---

## Playbook

```text
Crie um playbook operacional baseado nas boas práticas presentes nas fontes carregadas.
```

---

## Perguntas para Entrevista

```text
Quais perguntas técnicas um recrutador pode fazer sobre este tema? Apresente também as respostas esperadas.
```

---

# 🏆 Competências Desenvolvidas

- NotebookLM
- Inteligência Artificial Generativa
- Engenharia de Prompts
- Curadoria de Conteúdo
- Observabilidade
- Kubernetes
- SRE
- AIOps
- Pensamento Crítico
- Documentação Técnica

---

# 📂 Estrutura Recomendada do Repositório

```text
notebooklm-ai-sre-study-guide/
│
├── README.md
├── LICENSE
├── .gitignore
├── assets/
│   ├── notebooklm.png
│   ├── prompts.png
│   └── architecture.png
├── docs/
│   ├── resumo.md
│   ├── glossario.md
│   ├── prompts.md
│   ├── troubleshooting.md
│   └── referencias.md
├── prompts/
│   ├── aiops.md
│   ├── sre.md
│   ├── kubernetes.md
│   ├── observabilidade.md
│   └── incident-response.md
└── pdf/
    └── fontes-utilizadas.pdf
```

---

# 📌 Conclusão

O NotebookLM mostrou-se uma ferramenta eficiente para organizar conhecimento, consolidar conteúdos técnicos e acelerar o aprendizado baseado em documentação oficial. A experiência reforçou que a qualidade das respostas depende diretamente da qualidade das fontes utilizadas e da construção de prompts claros, específicos e contextualizados.

Este projeto demonstra a aplicação prática de Inteligência Artificial como ferramenta de aprendizagem ativa e evidencia competências relevantes para profissionais de Cloud Computing, DevOps, SRE, Observabilidade e Engenharia de Software.

---

## 👨‍💻 Autor

**Marcos Manhanes de Souza**

- LinkedIn: https://www.linkedin.com/
- GitHub: https://github.com/manhanes

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
````
