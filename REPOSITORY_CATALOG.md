# Catálogo Operacional do Repositório

> Catálogo gerado por `scripts/catalog_repository.py` para organizar arquivos soltos, criar navegação verificável e separar fato documental, hipótese, artefato e lacuna útil.

## Escopo e garantias

- Profundidade analisada: 5 níveis a partir da raiz do repositório.
- Arquivos catalogados: 41.
- Diretórios ignorados: `.git`, caches Python e dependências externas.
- Escrita segura: atualização atômica com arquivo temporário; use Git para rollback.
- Sem rede e sem dependências externas: execução local, reproduzível e auditável.

## Resumo por categoria

| Categoria | Arquivos |
|---|---:|
| arquivo solto/sem extensão | 5 |
| conteúdo markdown | 18 |
| dataset | 1 |
| derivada gerada | 4 |
| metadado/dado estruturado | 1 |
| navegação/catálogo | 4 |
| nota/documento auxiliar | 1 |
| política/licença | 3 |
| publicação compilada | 1 |
| recurso visual | 1 |
| script/ferramenta | 2 |

## Matriz de navegação e auditoria

| Arquivo | Nível | Categoria | Tamanho | Linhas | Evidência | Rota | Risco/Mitigação | SHA-256 |
|---|---:|---|---:|---:|---|---|---|---|
| `.gitignore` | 1 | arquivo solto/sem extensão | 378 | 48 | documental/narrativo; requer curadoria de afirmações | leitura → .gitignore | normalizar descrição e destino de leitura | `603229eedc60` |
| `222` | 1 | arquivo solto/sem extensão | 1236 | 63 | documental/narrativo; requer curadoria de afirmações | leitura → 222 | normalizar descrição e destino de leitura | `e5efb8ebeabf` |
| `ABSTRACT.md` | 1 | conteúdo markdown | 4612 | 62 | documental/narrativo; requer curadoria de afirmações | leitura → ABSTRACT.md | baixo; manter referências cruzadas | `abc0833e4f6a` |
| `APPLICATIONS.md` | 1 | conteúdo markdown | 30254 | 676 | documental/narrativo; requer curadoria de afirmações | leitura → APPLICATIONS.md | baixo; manter referências cruzadas | `b8c35e7ebc0e` |
| `BIBLIOGRAPHY.md` | 1 | conteúdo markdown | 22190 | 451 | documental/narrativo; requer curadoria de afirmações | leitura → BIBLIOGRAPHY.md | baixo; manter referências cruzadas | `085a381198fe` |
| `Biografia.md` | 1 | conteúdo markdown | 6810 | 220 | documental/narrativo; requer curadoria de afirmações | leitura → Biografia.md | baixo; manter referências cruzadas | `c9c3bf56a90f` |
| `Canto do amor cientiespiritual` | 1 | arquivo solto/sem extensão | 2710 | 97 | documental/narrativo; requer curadoria de afirmações | leitura → Canto do amor cientiespiritual | normalizar descrição e destino de leitura | `fd4403ef1434` |
| `capítulo 1.md` | 1 | conteúdo markdown | 4296 | 64 | documental/narrativo; requer curadoria de afirmações | leitura → capítulo 1.md | baixo; manter referências cruzadas | `d11269eae675` |
| `ClayMathEspiral.svg` | 1 | recurso visual | 1192 | 23 | artefato; requer inspeção visual/documental | leitura → ClayMathEspiral.svg | baixo; manter referências cruzadas | `91cf78d34104` |
| `derivatives/all_derivatives.json` | 2 | derivada gerada | 184548 | 3772 | verificável por execução ou parse | derivadas → derivatives/all_derivatives.json | não editar manualmente sem regenerar | `44c5850f0d90` |
| `derivatives/cross_references.json` | 2 | derivada gerada | 3528 | 190 | verificável por execução ou parse | derivadas → derivatives/cross_references.json | não editar manualmente sem regenerar | `5415a322cf3e` |
| `derivatives/DERIVATIVES_REPORT.md` | 2 | derivada gerada | 15233 | 504 | verificável por execução ou parse | derivadas → derivatives/DERIVATIVES_REPORT.md | não editar manualmente sem regenerar | `82ab4078a389` |
| `derivatives/README.md` | 2 | derivada gerada | 8072 | 308 | verificável por execução ou parse | derivadas → derivatives/README.md | não editar manualmente sem regenerar | `9f03120afcba` |
| `DERIVATIVES_INDEX.md` | 1 | conteúdo markdown | 17341 | 465 | documental/narrativo; requer curadoria de afirmações | leitura → DERIVATIVES_INDEX.md | baixo; manter referências cruzadas | `631c8a531569` |
| `Docs/Notas.md` | 2 | nota/documento auxiliar | 3065 | 98 | documental/narrativo; requer curadoria de afirmações | leitura → Docs/Notas.md | baixo; manter referências cruzadas | `c1354535a1fb` |
| `Epilogo.md` | 1 | conteúdo markdown | 22877 | 712 | documental/narrativo; requer curadoria de afirmações | leitura → Epilogo.md | baixo; manter referências cruzadas | `071622937d1c` |
| `FILE_DESCRIPTIONS.md` | 1 | navegação/catálogo | 19229 | 515 | documental/narrativo; requer curadoria de afirmações | índices → FILE_DESCRIPTIONS.md | baixo; manter referências cruzadas | `338c2292455c` |
| `INDEX.md` | 1 | navegação/catálogo | 11731 | 290 | documental/narrativo; requer curadoria de afirmações | índices → INDEX.md | baixo; manter referências cruzadas | `04a13813b541` |
| `Introducao.md` | 1 | conteúdo markdown | 2528 | 85 | documental/narrativo; requer curadoria de afirmações | leitura → Introducao.md | baixo; manter referências cruzadas | `701daa115d48` |
| `License.md` | 1 | política/licença | 8870 | 315 | documental/narrativo; requer curadoria de afirmações | leitura → License.md | baixo; manter referências cruzadas | `138b6422d8ac` |
| `Livro_Sagrado_Rafaeliano.pdf` | 1 | publicação compilada | 5279 | — | artefato; requer inspeção visual/documental | leitura → Livro_Sagrado_Rafaeliano.pdf | baixo; manter referências cruzadas | `87cd0d01829e` |
| `Manifest.md` | 1 | conteúdo markdown | 1133 | 28 | documental/narrativo; requer curadoria de afirmações | leitura → Manifest.md | baixo; manter referências cruzadas | `0c2c23ff6af9` |
| `Manifest_2.md` | 1 | conteúdo markdown | 4059 | 100 | documental/narrativo; requer curadoria de afirmações | leitura → Manifest_2.md | baixo; manter referências cruzadas | `47949dde5a66` |
| `MASTER_INDEX.md` | 1 | navegação/catálogo | 20878 | 555 | documental/narrativo; requer curadoria de afirmações | índices → MASTER_INDEX.md | baixo; manter referências cruzadas | `fb222fa5b152` |
| `META_DATA.json` | 1 | metadado/dado estruturado | 426 | 13 | verificável por execução ou parse | leitura → META_DATA.json | baixo; manter referências cruzadas | `c54f1c50fe62` |
| `METHODOLOGY.md` | 1 | conteúdo markdown | 23429 | 668 | documental/narrativo; requer curadoria de afirmações | leitura → METHODOLOGY.md | baixo; manter referências cruzadas | `6d50ac052f93` |
| `PREFACE.md` | 1 | conteúdo markdown | 9761 | 213 | documental/narrativo; requer curadoria de afirmações | leitura → PREFACE.md | baixo; manter referências cruzadas | `0bee3a6722a9` |
| `Prefacio in code.md` | 1 | conteúdo markdown | 5054 | 107 | documental/narrativo; requer curadoria de afirmações | leitura → Prefacio in code.md | baixo; manter referências cruzadas | `c1fc7f854830` |
| `PRIVACY_POLICY.md` | 1 | política/licença | 349 | 7 | documental/narrativo; requer curadoria de afirmações | leitura → PRIVACY_POLICY.md | baixo; manter referências cruzadas | `f605beb44f13` |
| `Quba` | 1 | arquivo solto/sem extensão | 3333 | 91 | documental/narrativo; requer curadoria de afirmações | leitura → Quba | normalizar descrição e destino de leitura | `0bdaf6b2c841` |
| `QUICK_START.md` | 1 | conteúdo markdown | 8988 | 304 | documental/narrativo; requer curadoria de afirmações | leitura → QUICK_START.md | baixo; manter referências cruzadas | `975c2b46524e` |
| `README.md` | 1 | navegação/catálogo | 49526 | 1591 | documental/narrativo; requer curadoria de afirmações | índices → README.md | arquivo grande; revisar por seções | `760e6564a768` |
| `review1.md` | 1 | conteúdo markdown | 3449 | 130 | documental/narrativo; requer curadoria de afirmações | leitura → review1.md | baixo; manter referências cruzadas | `f38d5174f087` |
| `scripts/catalog_repository.py` | 2 | script/ferramenta | 10259 | 267 | verificável por execução ou parse | executar/validar → scripts/catalog_repository.py | testar antes de usar em pipeline | `c019c52ef843` |
| `scripts/generate_derivatives.py` | 2 | script/ferramenta | 14039 | 348 | verificável por execução ou parse | executar/validar → scripts/generate_derivatives.py | testar antes de usar em pipeline | `e19eb63421b1` |
| `SESSION_FRAMEWORK.md` | 1 | conteúdo markdown | 10775 | 207 | documental/narrativo; requer curadoria de afirmações | leitura → SESSION_FRAMEWORK.md | baixo; manter referências cruzadas | `6ad297817cfe` |
| `TAKEDOWN_POLICY.md` | 1 | política/licença | 369 | 10 | documental/narrativo; requer curadoria de afirmações | leitura → TAKEDOWN_POLICY.md | baixo; manter referências cruzadas | `674932d570f8` |
| `TECHNICAL_SUMMARY.md` | 1 | conteúdo markdown | 12249 | 435 | documental/narrativo; requer curadoria de afirmações | leitura → TECHNICAL_SUMMARY.md | baixo; manter referências cruzadas | `db86e8b6d5ef` |
| `toro_84_bitraf42.csv` | 1 | dataset | 3511 | 85 | verificável por execução ou parse | dados → toro_84_bitraf42.csv | baixo; manter referências cruzadas | `fcde0e63605f` |
| `TRANSFORMATION_SUMMARY.md` | 1 | conteúdo markdown | 14243 | 385 | documental/narrativo; requer curadoria de afirmações | leitura → TRANSFORMATION_SUMMARY.md | baixo; manter referências cruzadas | `772d4fd32f03` |
| `voz` | 1 | arquivo solto/sem extensão | 2423 | 91 | documental/narrativo; requer curadoria de afirmações | leitura → voz | normalizar descrição e destino de leitura | `11f8b91a5dbb` |

## Failsafe, failover e rollback

1. **Failsafe:** se um arquivo não puder ser lido, o script avisa em `stderr` e continua catalogando o restante.
2. **Failover:** o catálogo é escrito em arquivo temporário antes de substituir o destino final.
3. **Rollback:** qualquer versão anterior pode ser recuperada por Git (`git checkout -- REPOSITORY_CATALOG.md`) antes de commit, ou por commit anterior depois de commit.
4. **Mitigação:** arquivos gerados são marcados para evitar edição manual sem regeneração.
5. **Watchdog manual:** rode `python3 scripts/catalog_repository.py --check` no CI/local para detectar catálogo desatualizado.

## Lacunas úteis detectáveis

- Arquivos sem extensão devem receber descrição explícita em índices ou no catálogo.
- Afirmações narrativas, espirituais ou metafóricas devem permanecer como parábolas/conceitos até receberem fonte ou teste.
- Artefatos binários exigem inspeção visual ou validação externa; o hash apenas prova integridade do arquivo, não verdade do conteúdo.
