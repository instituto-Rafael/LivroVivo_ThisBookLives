# Protocolo Célula de Domínio do Livro Vivo V1

## 1. Finalidade

Este protocolo transforma uma semente humana em uma célula de domínio navegável e auditável, sem exigir que a pessoa domine programação, matemática, engenharia de dados ou mecanismos internos de inteligência artificial.

A invariante é:

```text
sentido humano
→ semente preservada
→ linguagem do domínio
→ módulos auxiliares opcionais
→ proposta limitada
→ decisão humana
→ evidência
→ receipt
→ memória indexada
```

Um módulo auxiliar pode calcular, classificar, traduzir, simular ou validar, mas deve devolver seu resultado na linguagem do domínio principal. Matemática e código são realidades paralelas de apoio, não requisitos de entrada para a pessoa.

## 2. Ledger semelhante a blockchain

O ledger é **semelhante a blockchain**, mas não é uma blockchain pública. Ele é uma cadeia hash append-only local ou federada:

```text
previous_event_sha256
+ corpo canônico do evento
+ digest triplo do objeto
→ digest triplo do evento atual
```

Isso fornece indício verificável de alteração e linhagem. Não fornece consenso público, token financeiro, prova de trabalho nem verdade automática.

```text
integridade por hash != verdade factual
commit != execução
proposta da IA != autorização humana
```

## 3. Diretório canônico

```text
data/living_book/
├── domain_cells/
│   └── music.v1.json
└── ledger/
    └── genesis.music.v1.json

schemas/
└── living_book_domain_cell.schema.json

scripts/
└── validate_living_book_domain_cell.py

tests/
└── test_living_book_domain_cell.py
```

Domínios futuros reutilizam o mesmo contrato:

```text
domain_cells/
├── music.v1.json
├── agriculture.v1.json
├── law.v1.json
├── health.v1.json
├── crafts.v1.json
└── education.v1.json
```

Cada domínio conserva seu vocabulário e suas perguntas práticas. Módulos compartilhados podem auxiliar vários domínios, mas não podem redefini-los silenciosamente.

## 4. Os dois espelhos

### Espelho humano

O espelho humano preserva:

- intenção;
- vocabulário;
- contexto vivido;
- consentimento;
- correções;
- direito de pausar, revogar, rejeitar ou reinterpretar;
- autoridade final sobre publicação e divulgação sensível.

### Espelho IA

O espelho IA pode:

- organizar;
- comparar;
- traduzir entre domínio e módulos auxiliares;
- marcar lacunas;
- propor testes;
- gerar artefatos limitados;
- explicar evidências e limites.

Ele não pode:

- aprovar a própria proposta;
- publicar autonomamente;
- divulgar material privado;
- promover claim;
- executar conteúdo não confiável;
- sobrescrever a semente humana;
- apresentar apoio matemático como se fosse declaração da pessoa.

Os espelhos formam um par assimétrico:

```text
humano = autoridade e sentido
IA     = serviço, análise e proposta
```

## 5. Célula de domínio

Uma célula contém sete superfícies:

1. `seed`: intenção de origem, preferencialmente em resumo que preserve privacidade;
2. `mirrors`: responsabilidades humana e da IA;
3. `modules`: domínio principal e módulos auxiliares opcionais;
4. `relations`: pontes tipadas entre módulos;
5. `governance`: responsáveis, gates de aprovação, contestação e rollback;
6. `privacy_security`: classificação, minimização, segredos e entrada não confiável;
7. `workflow_proof`: estados, gatilhos, falsificadores, receipts e indexação.

## 6. Interação orientada ao domínio

No exemplo musical, a pessoa pode dizer:

> “Aprendo melodias de ouvido e quero entender por que algumas progressões parecem naturais.”

A interface principal continua musical:

```text
melodia
ritmo
harmonia
instrumento
prática
escuta
composição
```

Módulos opcionais podem usar internamente:

```text
matemática → proporções, periodicidade, relações em grafo
código      → análise de áudio ou geração de catálogo
IA          → comparação, explicação e exercícios
segurança   → direitos, consentimento e gravações privadas
```

Mas a saída retorna como orientação musical. A pessoa só vê equações ou código quando escolher essa rota.

## 7. Relações tipadas

As relações não são links genéricos. Cada aresta declara seu significado:

- `EXPLAINS` — um módulo explica outro;
- `MEASURES` — produz medição declarada;
- `VALIDATES` — aplica teste delimitado;
- `TRANSLATES_TO_DOMAIN` — converte apoio para a linguagem do domínio;
- `DEPENDS_ON` — exige outro artefato ou estado;
- `CONTRADICTS` — preserva oposição ainda aberta;
- `GOVERNED_BY` — identifica autoridade de política;
- `EVIDENCED_BY` — aponta para receipt ou fonte.

Relação desconhecida falha de modo fechado.

## 8. Estados do fluxo

```text
CAPTURED
→ CLASSIFIED
→ MAPPED
→ PROPOSED
→ HUMAN_APPROVED
→ EXECUTED_BOUNDED
→ VERIFIED
→ RECEIPTED
→ INDEXED
```

A célula pode parar em qualquer estado. Falta de aprovação ou evidência vira `TOKEN_VAZIO` tipado, nunca sucesso inventado.

Nenhum gatilho da V1 pode executar, publicar, revelar dados privados ou promover claims automaticamente.

## 9. Prova de ação

Todo módulo capaz de executar deverá produzir, quando materializado:

```text
intent_id
object_id
digests de entrada
comando ou procedimento exato
ambiente
decisão de política
digest da aprovação humana
início e fim
status de saída
outputs e digests
testes e falsificadores
rollback
F_ok / F_gap / F_next
```

Este pacote V1 prova apenas coerência estrutural do exemplo e do ledger. Não prova teoria musical, habilidade de usuário, execução Android nem eficácia científica.

## 10. Digest triplo

A implementação de referência usa três algoritmos disponíveis na biblioteca padrão sobre JSON canônico:

```text
SHA-256
SHA3-256
BLAKE2b-256
```

BLAKE3 permanece como perfil futuro compatível quando houver implementação verificada no ambiente. A lista é explícita para impedir substituição silenciosa.

## 11. Invariantes de governança, privacidade e segurança

```text
claim_allowed = false por padrão
texto privado bruto não entra no repositório
segredos são proibidos
conteúdo não confiável nunca é executado
IA não aprova saída da própria IA
aprovação humana vincula-se ao digest exato do objeto
publicação exige gate separado e explícito
módulo auxiliar não pode exigir conhecimento de programação
fonte nunca é sobrescrita por derivada
```

## 12. Fronteira da primeira prova

O validador incluído verifica:

- estrutura obrigatória;
- assimetria de autoridade humano/IA;
- proibição de segredos e conteúdo privado bruto;
- acessibilidade dos módulos auxiliares;
- relações tipadas;
- ordem da máquina de estados;
- proibições de gatilhos;
- digests triplos;
- ligação do evento gênese;
- `claim_allowed=false`.

O resultado é uma **semente estrutural validada**, e não um middleware autônomo completo.
