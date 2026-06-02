#!/usr/bin/env python3
"""Generate a 5-level repository catalog for Livro Vivo.

The script is intentionally dependency-free and writes atomically so the catalog can
be regenerated, checked, and rolled back in constrained environments.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "REPOSITORY_CATALOG.md"
DEFAULT_DEPTH = 5
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", ".mypy_cache"}
SKIP_FILES = {"REPOSITORY_CATALOG.md"}
TEXT_EXTENSIONS = {
    "", ".md", ".txt", ".json", ".csv", ".py", ".svg", ".yml", ".yaml",
    ".toml", ".ini", ".cfg", ".rst",
}


@dataclass(frozen=True)
class Entry:
    path: Path
    depth: int
    size: int
    sha256: str
    lines: int | None
    category: str
    evidence: str
    route: str
    risk: str


def relative_depth(path: Path) -> int:
    return len(path.relative_to(REPO_ROOT).parts)


def is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def count_lines_if_text(path: Path, data: bytes) -> int | None:
    if not is_text_candidate(path):
        return None
    try:
        return data.decode("utf-8").count("\n") + (0 if data.endswith(b"\n") or not data else 1)
    except UnicodeDecodeError:
        return None


def categorize(path: Path) -> str:
    name = path.name
    suffix = path.suffix.lower()
    rel = path.relative_to(REPO_ROOT).as_posix()
    if rel.startswith("scripts/"):
        return "script/ferramenta"
    if rel.startswith("derivatives/"):
        return "derivada gerada"
    if rel.startswith("Docs/"):
        return "nota/documento auxiliar"
    if suffix == ".json":
        return "metadado/dado estruturado"
    if suffix == ".csv":
        return "dataset"
    if suffix == ".svg":
        return "recurso visual"
    if suffix == ".pdf":
        return "publicação compilada"
    if name in {"License.md", "PRIVACY_POLICY.md", "TAKEDOWN_POLICY.md"}:
        return "política/licença"
    if name in {"README.md", "MASTER_INDEX.md", "INDEX.md", "FILE_DESCRIPTIONS.md", "REPOSITORY_CATALOG.md"}:
        return "navegação/catálogo"
    if suffix == ".md":
        return "conteúdo markdown"
    return "arquivo solto/sem extensão"


def evidence_level(path: Path, category: str) -> str:
    suffix = path.suffix.lower()
    if category in {"script/ferramenta", "dataset", "metadado/dado estruturado", "derivada gerada"}:
        return "verificável por execução ou parse"
    if suffix in {".md", ""}:
        return "documental/narrativo; requer curadoria de afirmações"
    if suffix in {".pdf", ".svg"}:
        return "artefato; requer inspeção visual/documental"
    return "catalogado; evidência pendente"


def navigation_route(path: Path, category: str) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    if category == "script/ferramenta":
        return f"executar/validar → {rel}"
    if category == "derivada gerada":
        return f"derivadas → {rel}"
    if category == "dataset":
        return f"dados → {rel}"
    if category == "navegação/catálogo":
        return f"índices → {rel}"
    return f"leitura → {rel}"


def risk_note(path: Path, category: str, lines: int | None) -> str:
    if category == "arquivo solto/sem extensão":
        return "normalizar descrição e destino de leitura"
    if category == "derivada gerada":
        return "não editar manualmente sem regenerar"
    if category == "script/ferramenta":
        return "testar antes de usar em pipeline"
    if lines is not None and lines > 1000:
        return "arquivo grande; revisar por seções"
    return "baixo; manter referências cruzadas"


def iter_files(max_depth: int) -> Iterable[Path]:
    stack: list[tuple[Path, int]] = [(REPO_ROOT, 0)]
    while stack:
        directory, depth = stack.pop()
        try:
            children = sorted(os.scandir(directory), key=lambda item: item.name.lower())
        except OSError as exc:
            print(f"warning: cannot scan {directory}: {exc}", file=sys.stderr)
            continue
        for child in reversed(children):
            path = Path(child.path)
            if child.is_dir(follow_symlinks=False):
                if child.name in SKIP_DIRS or depth >= max_depth:
                    continue
                stack.append((path, depth + 1))
            elif child.is_file(follow_symlinks=False):
                rel = path.relative_to(REPO_ROOT)
                if rel.name in SKIP_FILES:
                    continue
                if len(rel.parts) <= max_depth:
                    yield path


def build_entries(max_depth: int) -> list[Entry]:
    entries: list[Entry] = []
    for path in sorted(iter_files(max_depth), key=lambda item: item.relative_to(REPO_ROOT).as_posix().lower()):
        data = read_bytes(path)
        category = categorize(path)
        lines = count_lines_if_text(path, data)
        entries.append(
            Entry(
                path=path.relative_to(REPO_ROOT),
                depth=relative_depth(path),
                size=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
                lines=lines,
                category=category,
                evidence=evidence_level(path, category),
                route=navigation_route(path, category),
                risk=risk_note(path, category, lines),
            )
        )
    return entries


def render_catalog(entries: list[Entry], max_depth: int) -> str:
    by_category: dict[str, int] = {}
    for entry in entries:
        by_category[entry.category] = by_category.get(entry.category, 0) + 1

    lines = [
        "# Catálogo Operacional do Repositório",
        "",
        "> Catálogo gerado por `scripts/catalog_repository.py` para organizar arquivos soltos, criar navegação verificável e separar fato documental, hipótese, artefato e lacuna útil.",
        "",
        "## Escopo e garantias",
        "",
        f"- Profundidade analisada: {max_depth} níveis a partir da raiz do repositório.",
        f"- Arquivos catalogados: {len(entries)}.",
        "- Diretórios ignorados: `.git`, caches Python e dependências externas.",
        "- Escrita segura: atualização atômica com arquivo temporário; use Git para rollback.",
        "- Sem rede e sem dependências externas: execução local, reproduzível e auditável.",
        "",
        "## Resumo por categoria",
        "",
        "| Categoria | Arquivos |",
        "|---|---:|",
    ]
    for category, count in sorted(by_category.items()):
        lines.append(f"| {category} | {count} |")

    lines.extend([
        "",
        "## Matriz de navegação e auditoria",
        "",
        "| Arquivo | Nível | Categoria | Tamanho | Linhas | Evidência | Rota | Risco/Mitigação | SHA-256 |",
        "|---|---:|---|---:|---:|---|---|---|---|",
    ])

    for entry in entries:
        line_count = "—" if entry.lines is None else str(entry.lines)
        lines.append(
            "| "
            f"`{entry.path.as_posix()}` | {entry.depth} | {entry.category} | {entry.size} | {line_count} | "
            f"{entry.evidence} | {entry.route} | {entry.risk} | `{entry.sha256[:12]}` |"
        )

    lines.extend([
        "",
        "## Failsafe, failover e rollback",
        "",
        "1. **Failsafe:** se um arquivo não puder ser lido, o script avisa em `stderr` e continua catalogando o restante.",
        "2. **Failover:** o catálogo é escrito em arquivo temporário antes de substituir o destino final.",
        "3. **Rollback:** qualquer versão anterior pode ser recuperada por Git (`git checkout -- REPOSITORY_CATALOG.md`) antes de commit, ou por commit anterior depois de commit.",
        "4. **Mitigação:** arquivos gerados são marcados para evitar edição manual sem regeneração.",
        "5. **Watchdog manual:** rode `python3 scripts/catalog_repository.py --check` no CI/local para detectar catálogo desatualizado.",
        "",
        "## Lacunas úteis detectáveis",
        "",
        "- Arquivos sem extensão devem receber descrição explícita em índices ou no catálogo.",
        "- Afirmações narrativas, espirituais ou metafóricas devem permanecer como parábolas/conceitos até receberem fonte ou teste.",
        "- Artefatos binários exigem inspeção visual ou validação externa; o hash apenas prova integridade do arquivo, não verdade do conteúdo.",
        "",
    ])
    return "\n".join(lines)


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temp_name = handle.name
    os.replace(temp_name, path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or check the 5-level repository catalog.")
    parser.add_argument("--max-depth", type=int, default=DEFAULT_DEPTH, help="maximum file depth from repo root")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="catalog output path")
    parser.add_argument("--check", action="store_true", help="fail if the catalog is not up to date")
    args = parser.parse_args()

    entries = build_entries(args.max_depth)
    content = render_catalog(entries, args.max_depth)
    output = args.output if args.output.is_absolute() else REPO_ROOT / args.output

    if args.check:
        current = output.read_text(encoding="utf-8") if output.exists() else ""
        if current != content:
            print(f"catalog out of date: {output.relative_to(REPO_ROOT)}", file=sys.stderr)
            return 1
        print(f"catalog up to date: {output.relative_to(REPO_ROOT)} ({len(entries)} files)")
        return 0

    write_atomic(output, content)
    print(f"catalog written: {output.relative_to(REPO_ROOT)} ({len(entries)} files, depth {args.max_depth})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
