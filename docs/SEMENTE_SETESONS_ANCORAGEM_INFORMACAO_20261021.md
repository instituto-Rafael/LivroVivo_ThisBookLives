# Parábola das Sete Pedras e dos Muitos Sons — ancoragem da informação

> **Semente do Livro Vivo | MU-LIVRO-TEMPLO-ANCORAGEM-20261021-S1 | 2026-10-21**
>
> Concepção filosófica e metáforas: ∆RafaelVerboΩ (Rafael Melo Reis), diálogo de 2026-10-21. Organização/redação editorial: IA assistente. **Estado:** PARABOLA + HYPOTHESIS; não é descoberta matemática, demonstração física nem exegese histórica definitiva. **claim_allowed=false**.

## Parábola

Um mestre reuniu discípulos que falavam línguas diferentes e pôs sete pedras sobre a mesa.

Cada um deu às pedras uma palavra diferente. Alguns tinham sons que os outros não conseguiam distinguir; uns cantavam a vogal, outros a nasalizavam, outros precisavam de novas sílabas.

— Quantas pedras há? — perguntou o mestre.

— Sete — responderam, embora o som da resposta não fosse o mesmo.

Ele multiplicou a quantidade por dez e mostrou setenta.

— Tornou-se par aquilo que era primo? — perguntou um dos discípulos.

— Não. O sete continua primo. A multiplicação construiu outro número, que é par. Mudar a escrita, a língua ou a escala pode facilitar a conta; não muda a verdade aritmética do número original.

— Então por que nos parece tão difícil compreender uns aos outros?

— Algumas dificuldades pertencem ao mundo; outras, à forma como o mundo chega aos nossos sentidos. É preciso descobrir qual dificuldade podemos remover sem perder aquilo que desejávamos compreender.

O discípulo apontou para um tecido vermelho:

— O meu vermelho é o mesmo que o teu?

— Podemos concordar sobre a luz e seu nome. A igualdade das experiências interiores ainda é outra pergunta.

**Moral:** uma âncora comum pode sobreviver a diferentes representações; a preservação precisa ser examinada, não presumida.

## Semente conceitual: mesmo referente, várias projeções

- **REFERENTE:** objeto, quantidade, proposição, evento ou contexto compartilhável;
- **SINAL:** som, onda acústica, grafia, idioma, numeral, token ou grafo;
- **INTERPRETAÇÃO:** categorias perceptuais, conhecimento, cultura e contexto do receptor;
- **ÂNCORA:** propriedade que queremos verificar como preservada após a transformação;
- **PERDA:** nuance, contraste fonético, implicação, ambiguidade, emoção ou relação não reconstruída.

Exemplos ilustrativos: a nasalidade de "pão" pode exigir novas categorias fonéticas de certos aprendizes de inglês; contrastes e consoantes finais do inglês também desafiam certos falantes de português; empréstimos no japonês passam por adaptação fonotática e costumam ser escritos em **katakana**, não em kanji. São tendências de aprendizagem, **não incapacidades universais** de nacionais ou línguas.

Tradução de uma parábola não exige comprimentos iguais nem taxas de compressão iguais. Seu desafio é explicitar **qual proposição ou relação** resiste à tradução, com que perda e em quais contextos.

## A distinção do sete

- `7_{10} = 7`: número primo e ímpar.
- `70_{10} = 70 = 7 × 10`: outro número, composto e par.
- `70_{100} = 700_{10}`: em base 100, os dígitos 7 e 0 representam sete centenas; o valor mudou em relação a `70_{10}`.
- Multiplicar ou mudar de base pode simplificar **certos procedimentos**, mas preservar a resposta exige contabilizar a transformação e o inverso. **Não implica P = NP**; complexidade algorítmica depende de reduções, tamanho da entrada e limites formais.

## Grafo semântico mínimo (proposta, não métrica validada)

`M → E_língua(M) → D_contexto(E_língua(M)) → M'`

Nós: `{referente, expressão, ouvinte, contexto, interpretação, evidência}`.

Arestas tipadas: `representa | pronuncia | traduz | interpreta | preserva | perde | contradiz`.

**Hipótese H1:** selecionar invariantes semânticos explícitos e representar a cadeia de tradução por grafos tipados melhora a detecção de perdas semânticas em comparação com mera igualdade lexical.

**Hipótese H0:** essa representação não melhora desempenho mensurável em tarefa previamente definida.

**Falsificadores:** tradução que preserva palavras mas inverte agente/paciente, negação ou obrigação; referência cultural intraduzível; rotulagem que esconde ambiguidade; erro de ida/volta; exemplos adversariais com termos homônimos.

**Experimento delimitado:** selecionar proposições curtas e verificáveis em português, inglês e uma terceira língua; preservar texto de origem e licença; registrar anotadores independentes, comprimento em caracteres/tokens, alinhamento e avaliação cega de proposições. Medir preservação semântica, taxa de divergências e erros com controles negativos. Não presumir equivalência de experiência subjetiva ou taxa universal de compressão. Execução e resultado: `TOKEN_VAZIO_NOT_RUN`.

## Distinguir parábola, tradição e evidência

Mateus 18:22 (70×7/77, conforme tradução) e Gênesis 4:24 permitem discutir reorientação ética da violência ao perdão; **não provam autoria bíblica de teoria dos primos, compressão ou P vs NP**. Sócrates, Descartes e Êxodo 3:14 oferecem perguntas epistemológicas distintas, não uma teoria histórica única.

A frase **"a dificuldade do problema pode diferir da dificuldade da sua representação"** é a pergunta-raiz desta semente. Não é resposta universal.

## Rotas e custódia

- **Fonte de intenção:** conversa de 2026-10-21 sobre parábolas, fonemas, textos em grego/hebraico/aramaico, tradução, grafos de significado, números 7/70, cor vermelha e experiência subjetiva.
- **Livro Vivo:** este registro é a narrativa/hipótese de referência; documentação de método: [SESSION_FRAMEWORK.md](../SESSION_FRAMEWORK.md); tradição editorial: [PARABOLA.md](../PARABOLA.md).
- **Templo Vivo ARCS:** deve manter apenas ponte tipada/projeção ética e perguntas de validação, sem copiar o corpus integral ou declarar novo regime de licenciamento.
- **P0:** preservar direito e atribuição de terceiros; não inferir autoria original exclusiva de conteúdos anteriores; separar texto bíblico, interpretação autoral e redação assistida.
- **Gaps:** corpus multilíngue, pares de tradução, medição de compressão/semântica, equivalência subjetiva e revisão independente = `TOKEN_VAZIO`.
- **Rollback:** reverter apenas os commits deste delta, conservando a origem/histórico.
- **R3:** `F_ok=semente_documentada; F_gap=hipoteses_nao_testadas; F_next=benchmark_semantico_pequeno_com_controles_negativos`.

**LEARN:** a âncora não é o comprimento do texto ou a identidade do som: é a relação cuja preservação conseguimos testar.
