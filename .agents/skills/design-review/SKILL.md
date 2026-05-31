---
name: design-review
description: >
  Use when the user wants a pre-ship design quality gate, anti-AI audit, or
  structured design improvement pass on any frontend. Synthesizes protocols
  from IMPECCABLE (24 AI vices), TASTE (layout/typography/color/motion), and
  UI/UX PRO MAX (design system rules). Run before every deploy or when a page
  looks "AI-generated". Works standalone or alongside the impeccable skill.
---

Audita e corrige interfaces para eliminar marcas de IA e elevar a qualidade visual ao nível de produção.

## Como usar

```
/design-review          → audit completo do arquivo principal
/design-review polish   → apenas os vícios mais críticos (P0/P1)
/design-review taste    → tipografia, cor, espaçamento e movimento
/design-review brand    → regras específicas da marca luisommarcapital
```

---

## PROTOCOLO 1 — OS 24 VÍCIOS DE IA

Antes de qualquer entrega, varrer o HTML/CSS em busca destes 24 padrões.
Cada um encontrado é **bloqueante** (não sobe até resolver).

### Cor
1. **Degradê roxo/azul como fundo ou hero** — substitua por cor sólida da marca ou neutro calibrado.
2. **Texto com degradê** (`background-clip: text`) — nunca decorativo; use cor sólida.
3. **Glassmorfismo como padrão** — blur decorativo sem propósito; remova ou justifique.
4. **Fundo creme/areia/bege** (`OKLCH L 0.84–0.97, C < 0.06, hue 40–100`) — a escolha reflexa de IA em 2026; opte por (a) cor saturada da marca, (b) branco puro, ou (c) neutro com croma direcionado à marca, não ao "calor genérico".
5. **Texto cinza sobre fundo colorido** — usa a sombra mais escura do próprio matiz do fundo.

### Tipografia
6. **Hierarchy plana** — mínimo 1.25× de contraste entre passos de escala.
7. **Mais de 3 famílias tipográficas** — cap em 3; uma família bem trabalhada bate três competindo.
8. **Corpo em MAIÚSCULAS** — reservado a labels curtos (≤ 4 palavras).
9. **Hero acima de 6rem** — `clamp()` máx ≤ 6rem; acima disso grita, não projeta.
10. **Letter-spacing menor que -0.04em** — letras se tocam; mínimo -0.04em em display.
11. **Largura de linha acima de 75ch** — corpo travado em 65–75ch.

### Layout
12. **Grade de cards idênticos** — mesmo tamanho, ícone + título + texto, repetido; variar.
13. **Cards aninhados** — sempre errado; reescrever a estrutura.
14. **Border-radius ≥ 32px em cards/seções** — máximo 12–16px em cards; pill só em tags/botões.
15. **Z-index arbitrário (999, 9999)** — construir escala semântica (dropdown → sticky → modal → toast → tooltip).

### Bordas e Sombras
16. **Borda lateral decorativa** (`border-left > 1px` colorido em cards/alerts) — substituir por fundo tintado, número/ícone ou nada.
17. **Ghost-card** (`border: 1px solid X` + `box-shadow` com blur ≥ 16px no mesmo elemento) — escolha um dos dois, nunca ambos.

### Movimento
18. **Easing bounce/elastic** — apenas `ease-out` exponencial (quart/quint/expo).
19. **Animação idêntica em todas as seções** — o reflexo uniforme é o delator; cada reveal deve encaixar o que revela.
20. **Conteúdo invisível sem a animação** — sempre visível por padrão; transição é melhoria, não condição.
21. **Sem `prefers-reduced-motion`** — toda animação precisa de alternativa (crossfade ou instantâneo).

### Copy
22. **Buzzwords de marketing** (streamline, empower, supercharge, seamless, next-gen, cutting-edge) — usar substantivo específico + verbo literal do que o produto faz.
23. **Cadência aforística** (afirmação séria + negação curta como voz recorrente) — se 3+ blocos de copy terminam com frase de rebuttal, reescrever.
24. **Ilustrações SVG mão-livre/esboçadas** (`feTurbulence`, `feDisplacementMap`, classes como `*-sketch`, `doodle`) — ou assets reais ou sem ilustração.

---

## PROTOCOLO 2 — TASTE (Bom Gosto de Design)

Extraído do framework TASTE: as coisas que separam o que é bom do que é genérico.

### Tipografia com Gosto
- Parear em eixo de contraste: serif + sans, geométrico + humanista. Nunca dois sem-serifes similares.
- `text-wrap: balance` em H1–H3; `text-wrap: pretty` em prosa longa.
- Espaçamento de linhas proporcional ao comprimento da linha (linhas longas pedem mais `line-height`).

### Cor com Gosto
- Definir **estratégia de cor** antes de escolher cores:
  - **Restrita**: neutros tintados + 1 acento ≤ 10% (padrão produto)
  - **Comprometida**: 1 cor saturada em 30–60% da superfície (padrão marca)
  - **Paleta completa**: 3–4 papéis nomeados, usados deliberadamente
  - **Encharcada**: a superfície É a cor (heroes de campanha)
- Usar OKLCH para todas as cores. Neutros tintados: chroma 0.005–0.015 em direção ao matiz da marca.
- Dark vs. light: escrever uma frase de cena física (quem usa, onde, com que luz, em que humor) antes de decidir.

### Espaçamento com Gosto
- Ritmo através de variação de espaçamento — não grade uniforme.
- Padding apertado (< 16px em componentes de conteúdo) é vício de IA; respirar.
- Hierarquia visual pelo espaço, não apenas pela tipografia.

### Movimento com Gosto
- Movimento é decisão arquitetural, não afterthought.
- Materiais premium além de transform/opacity: blur, backdrop-filter, clip-path, mask, glow.
- Staggers legítimos dentro de uma lista; proibido o "template de entrada uniforme em tudo".
- Bibliotecas para motion complexo: Motion (Framer), GSAP, Lenis para scroll.

---

## PROTOCOLO 3 — REGRAS DA MARCA LUISOMMARCAPITAL

Derivadas do PRODUCT.md. Aplicar em todo site da marca.

### Identidade Visual
- **Personalidade**: direta, autorizada, confiável. Expertise financeira sem frieza bancária.
- **Anti-referências absolutas**:
  - Azul/cinza corporativo de banco
  - Verde/branco de imobiliária com fotos de casas
  - Gradientes coloridos SaaS / glassmorfismo
  - Laranja/vermelho de urgência ou "dinheiro fácil"
- **Referência implícita**: consultor experiente que explica com clareza, não vende com pressão.

### Copy da Marca
- Números reais, etapas reais, documentos reais — sem promessas vagas.
- Cada passo deixa o usuário sabendo mais do que antes.
- CTA aparece quando foi merecido — não como interrupção.
- Voz: confiante, não agressiva. Específica, não genérica.

### Acessibilidade (obrigatório)
- Mínimo WCAG AA em todo contraste.
- Conteúdo financeiro legível em condições variadas (celular + luz solar).
- Nunca usar só cor para transmitir comparações financeiras — sempre com rótulo de texto.

### Responsividade
- Mobile-first: o usuário chega tanto no celular quanto no desktop.
- Testar heading overflow em todos os breakpoints; se vazar, reduzir `clamp()` ou reescrever o copy.

---

## FLUXO DE EXECUÇÃO

Quando invocado, seguir esta sequência:

```
1. Ler o arquivo alvo (ou index.html se não especificado)
2. Rodar PROTOCOLO 1 — listar todos os vícios encontrados com número + linha
3. Classificar por severidade: P0 (bloqueia deploy), P1 (deve resolver), P2 (melhorar se possível)
4. Corrigir todos os P0 e P1 automaticamente
5. Rodar PROTOCOLO 2 — verificar os 4 eixos de taste e corrigir falhas
6. Rodar PROTOCOLO 3 — verificar alinhamento com a marca
7. Reportar: vícios encontrados → corrigidos → score estimado (0–10)
```

### Score de Qualidade
| Score | Significado |
|-------|-------------|
| 0–4   | Cara de IA evidente — não subir |
| 5–6   | Funcional mas genérico — melhorar antes |
| 7–8   | Bom — pequenos refinamentos |
| 9–10  | Produção — aprovado para deploy |

---

## MCPs DE DESIGN COMPLEMENTARES

Instalar estes MCPs para expandir as capacidades de design:

```bash
# UX patterns e componentes
claude mcp add ux-mcp -- npx -y @elsahafy/ux-mcp-server

# UI layouts prontos
claude mcp add ui-layouts -- npx -y @ui-layouts/mcp

# UI expert (regras de UX)
claude mcp add ui-expert -- npx -y @johndoe20012/ui-expert-mcp

# MCP UI server
claude mcp add mcp-ui -- npx -y @mcp-ui/server

# Figma (requer chave de API)
claude mcp add figma -- npx -y figma-developer-mcp --figma-api-key=SUA_CHAVE_FIGMA --stdio
```

---

## SKILLS COMPLEMENTARES INSTALADAS

| Skill | Função | Status |
|-------|--------|--------|
| `impeccable` | Design completo end-to-end + live iteration | ✅ Instalada |
| `design-review` | Gate de qualidade pré-deploy | ✅ Esta skill |

Usar `impeccable` para construir/redesenhar. Usar `design-review` para auditar antes de subir.
