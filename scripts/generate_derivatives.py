#!/usr/bin/env python3
"""
Script de Geração de Derivadas RAFAELIA / RAFAELIA Derivatives Generation Script

Gera automaticamente derivadas, antiderivadas, inversas e reversas do conteúdo do Livro Vivo.
Automatically generates derivatives, antiderivatives, inverses, and reverses of Living Book content.

Autor / Author: ∆RafaelVerboΩ (Rafael Melo Reis)
Data / Date: 2026-01-08
Licença / License: CC BY-SA 4.0
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

# Configuração / Configuration
REPO_ROOT = Path(__file__).parent.parent
MARKDOWN_EXTS = ['.md', '.MD']
NO_EXTENSION_FILES = ['222', 'voz', 'Quba', 'Canto do amor cientiespiritual']
OUTPUT_DIR = REPO_ROOT / 'derivatives'


class DerivativeGenerator:
    """Gerador de derivadas conceituais"""
    
    def __init__(self):
        self.files = {}
        self.derivatives = defaultdict(list)
        self.cross_refs = defaultdict(set)
        
    def load_files(self):
        """Carrega todos os arquivos do repositório"""
        print("📂 Carregando arquivos do repositório...")
        
        # Arquivos markdown
        for md_file in REPO_ROOT.glob('*.md'):
            if md_file.name not in ['.git', 'node_modules']:
                self.files[md_file.name] = md_file.read_text(encoding='utf-8')
                print(f"  ✓ {md_file.name}")
        
        # Arquivos sem extensão
        for filename in NO_EXTENSION_FILES:
            filepath = REPO_ROOT / filename
            if filepath.exists():
                self.files[filename] = filepath.read_text(encoding='utf-8')
                print(f"  ✓ {filename}")
        
        print(f"\n✅ Total de {len(self.files)} arquivos carregados\n")
    
    def extract_concepts(self, text: str) -> List[str]:
        """Extrai conceitos principais de um texto"""
        # Busca por títulos, termos técnicos, palavras-chave
        concepts = []
        
        # Padrão para headers markdown
        headers = re.findall(r'^#{1,6}\s+(.+)$', text, re.MULTILINE)
        concepts.extend(headers)
        
        # Padrão para termos técnicos (palavras capitalizadas)
        technical = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
        concepts.extend(technical[:10])  # Limita a 10 mais relevantes
        
        # Padrão para termos em negrito
        bold_terms = re.findall(r'\*\*(.+?)\*\*', text)
        concepts.extend(bold_terms[:10])
        
        # Remove duplicatas e limita
        return list(dict.fromkeys(concepts))[:20]
    
    def generate_forward_derivative(self, concept: str, context: str) -> Dict:
        """Gera derivada forward (aplicação prática)"""
        return {
            'type': 'forward_derivative',
            'base_concept': concept,
            'transformation': 'expansão para aplicação prática',
            'result': f"Aplicação de '{concept}' em {context}",
            'description': f"Como implementar {concept} em contexto real de {context}",
            'examples': [
                f"Protótipo de {concept} para {context}",
                f"Caso de uso: {concept} resolvendo problema em {context}",
                f"Métrica de sucesso para {concept} em {context}"
            ]
        }
    
    def generate_backward_derivative(self, concept: str, source_file: str) -> Dict:
        """Gera antiderivada (rastreamento até fundamentos)"""
        # Mapeia conceitos para seus fundamentos teóricos
        foundations_map = {
            'Bitraf': 'Kanerva (2009) - Hyperdimensional Computing',
            'Fibonacci': 'Livio (2002) - The Golden Ratio',
            'Fractal': 'Mandelbrot (1982) - Fractal Geometry',
            'Autopoiese': 'Maturana & Varela (1980) - Autopoiesis',
            'Consciência': 'Tononi (2004) - Integrated Information Theory',
            'Sistema Vivo': 'Miller (1978) - Living Systems',
            'Retroalimentação': 'Tulving & Psotka (1971) - Retroactive Interference'
        }
        
        # Busca fundamento
        foundation = "Fundamentos filosóficos e científicos"
        for key, value in foundations_map.items():
            if key.lower() in concept.lower():
                foundation = value
                break
        
        return {
            'type': 'backward_derivative',
            'base_concept': concept,
            'transformation': 'rastreamento até origem teórica',
            'result': f"Fundamento de '{concept}'",
            'foundation': foundation,
            'description': f"Raízes históricas e teóricas que levaram a {concept}",
            'timeline': [
                'Precursores históricos',
                'Desenvolvimento teórico',
                'Formalização matemática',
                'Implementação em RAFAELIA'
            ]
        }
    
    def generate_inverse(self, concept: str) -> Dict:
        """Gera inversa (perspectiva complementar)"""
        # Mapeamento de opostos complementares (Yin-Yang)
        complementary_map = {
            'VAZIO': 'CHEIO',
            'VERBO': 'SILÊNCIO',
            'ORDEM': 'CAOS',
            'ESTRUTURA': 'FLUIDO',
            'CONSCIENTE': 'INCONSCIENTE',
            'ANÁLISE': 'SÍNTESE',
            'LOCAL': 'GLOBAL',
            'TEMPORAL': 'ATEMPORAL',
            'INDIVIDUAL': 'COLETIVO',
            'MATERIAL': 'ESPIRITUAL'
        }
        
        # Busca complementar
        complementary = f"Aspecto complementar de {concept}"
        for key, value in complementary_map.items():
            if key.lower() in concept.lower():
                complementary = value
                break
            elif value.lower() in concept.lower():
                complementary = key
                break
        
        return {
            'type': 'inverse',
            'base_concept': concept,
            'transformation': 'perspectiva complementar (Yin-Yang)',
            'result': complementary,
            'description': f"A face oposta mas interdependente de {concept}",
            'relationship': 'complementar_não_oposta',
            'integration': f"Como {concept} e {complementary} se unem em totalidade"
        }
    
    def generate_reverse(self, text: str, filename: str) -> Dict:
        """Gera reversa (leitura temporal invertida)"""
        # Inverte ordem dos parágrafos
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        reversed_paras = paragraphs[::-1]
        
        return {
            'type': 'reverse',
            'base_file': filename,
            'transformation': 'inversão temporal/lógica',
            'result': 'Leitura de trás para frente',
            'description': f"Lendo {filename} do fim ao início revela nova perspectiva",
            'insight': 'O que parece conclusão se torna premissa; origens se tornam destinos',
            'paragraphs_reversed': len(paragraphs),
            'sample': reversed_paras[0][:200] + '...' if reversed_paras else ''
        }
    
    def generate_all_derivatives(self):
        """Gera todas as 69 derivadas para todos os arquivos"""
        print("🧮 Gerando derivadas, antiderivadas, inversas e reversas...\n")
        
        contexts = [
            'Educação', 'Saúde', 'Finanças', 'Tecnologia', 'Arte',
            'Ciência', 'Espiritualidade', 'Governo', 'Indústria', 'Comunidade'
        ]
        
        derivative_count = 0
        
        for filename, content in self.files.items():
            print(f"📄 Processando {filename}...")
            
            # Extrai conceitos
            concepts = self.extract_concepts(content)
            print(f"  → {len(concepts)} conceitos identificados")
            
            # Gera derivadas forward
            for concept in concepts[:3]:  # Limita a 3 por arquivo
                for context in contexts[:2]:  # 2 contextos por conceito
                    deriv = self.generate_forward_derivative(concept, context)
                    self.derivatives[filename].append(deriv)
                    derivative_count += 1
            
            # Gera antiderivadas
            for concept in concepts[:2]:
                deriv = self.generate_backward_derivative(concept, filename)
                self.derivatives[filename].append(deriv)
                derivative_count += 1
            
            # Gera inversas
            for concept in concepts[:2]:
                deriv = self.generate_inverse(concept)
                self.derivatives[filename].append(deriv)
                derivative_count += 1
            
            # Gera reversa do arquivo completo
            deriv = self.generate_reverse(content, filename)
            self.derivatives[filename].append(deriv)
            derivative_count += 1
            
            print(f"  ✓ {len(self.derivatives[filename])} derivadas geradas\n")
        
        print(f"✅ Total: {derivative_count} derivadas geradas\n")
        return derivative_count
    
    def build_cross_references(self):
        """Constrói mapa de referências cruzadas"""
        print("🔗 Construindo referências cruzadas...\n")
        
        # Busca por menções entre arquivos
        for filename, content in self.files.items():
            # Busca por nomes de outros arquivos
            for other_file in self.files.keys():
                if other_file != filename:
                    # Remove extensão para busca
                    base_name = other_file.replace('.md', '')
                    if base_name.lower() in content.lower():
                        self.cross_refs[filename].add(other_file)
        
        # Exibe estatísticas
        for filename, refs in self.cross_refs.items():
            if refs:
                print(f"  {filename} → {len(refs)} referências")
        
        print(f"\n✅ Mapa de referências construído\n")
    
    def save_results(self):
        """Salva resultados em arquivos"""
        OUTPUT_DIR.mkdir(exist_ok=True)
        print(f"💾 Salvando resultados em {OUTPUT_DIR}...\n")
        
        # Salva derivadas em JSON
        derivatives_file = OUTPUT_DIR / 'all_derivatives.json'
        with open(derivatives_file, 'w', encoding='utf-8') as f:
            json.dump(dict(self.derivatives), f, indent=2, ensure_ascii=False)
        print(f"  ✓ {derivatives_file.name}")
        
        # Salva referências cruzadas
        cross_refs_file = OUTPUT_DIR / 'cross_references.json'
        with open(cross_refs_file, 'w', encoding='utf-8') as f:
            # Converte sets para listas para JSON
            refs_dict = {k: list(v) for k, v in self.cross_refs.items()}
            json.dump(refs_dict, f, indent=2, ensure_ascii=False)
        print(f"  ✓ {cross_refs_file.name}")
        
        # Gera relatório markdown
        report_file = OUTPUT_DIR / 'DERIVATIVES_REPORT.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(self.generate_report())
        print(f"  ✓ {report_file.name}")
        
        print(f"\n✅ Resultados salvos com sucesso!\n")
    
    def generate_report(self) -> str:
        """Gera relatório markdown das derivadas"""
        report = []
        report.append("# Relatório de Derivadas RAFAELIA\n")
        report.append(f"**Data:** 2026-01-08\n")
        report.append(f"**Autor:** ∆RafaelVerboΩ\n\n")
        report.append("---\n\n")
        
        # Estatísticas gerais
        total_derivatives = sum(len(derivs) for derivs in self.derivatives.values())
        report.append(f"## Estatísticas Gerais\n\n")
        report.append(f"- **Arquivos processados:** {len(self.files)}\n")
        report.append(f"- **Total de derivadas:** {total_derivatives}\n")
        report.append(f"- **Referências cruzadas:** {sum(len(refs) for refs in self.cross_refs.values())}\n\n")
        
        # Detalhamento por arquivo
        report.append("## Derivadas por Arquivo\n\n")
        for filename in sorted(self.derivatives.keys()):
            derivs = self.derivatives[filename]
            report.append(f"### {filename}\n\n")
            report.append(f"**Total de derivadas:** {len(derivs)}\n\n")
            
            # Conta por tipo
            type_counts = defaultdict(int)
            for deriv in derivs:
                type_counts[deriv['type']] += 1
            
            report.append("**Por tipo:**\n")
            for dtype, count in sorted(type_counts.items()):
                report.append(f"- {dtype}: {count}\n")
            report.append("\n")
            
            # Amostra de derivadas
            report.append("**Exemplos:**\n\n")
            for deriv in derivs[:3]:  # Primeiras 3
                report.append(f"- **{deriv['type']}:** {deriv.get('result', 'N/A')}\n")
            report.append("\n")
        
        # Mapa de referências
        report.append("## Mapa de Referências Cruzadas\n\n")
        for filename in sorted(self.cross_refs.keys()):
            refs = self.cross_refs[filename]
            if refs:
                report.append(f"- **{filename}** → {', '.join(sorted(refs))}\n")
        
        report.append("\n---\n\n")
        report.append("**Gerado automaticamente por generate_derivatives.py**\n")
        
        return ''.join(report)
    
    def run(self):
        """Executa o pipeline completo"""
        print("=" * 60)
        print("  🌀 RAFAELIA Derivatives Generator 🌀")
        print("=" * 60)
        print()
        
        self.load_files()
        count = self.generate_all_derivatives()
        self.build_cross_references()
        self.save_results()
        
        print("=" * 60)
        print(f"  ✨ Processo completo! {count} derivadas geradas ✨")
        print("=" * 60)
        print()


def main():
    """Função principal"""
    generator = DerivativeGenerator()
    generator.run()


if __name__ == '__main__':
    main()
