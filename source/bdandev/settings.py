"""
Modulo responsavel pelas configuracoes globais do projeto.
"""

from os import path

# Endereco dos codigos fontes do projeto.
PATH_FONTE = path.abspath(path.dirname(__file__))

# Endereco de dados diversos no projeto.
PATH_DATA = path.normpath(path.join(path_dados, '..', 'data'))

# Endereco dos arquivos XML
CORPO_INTEIRO = path.join(path, 'corpo_inteiro.xml')
PARTE_SUPERIOR_CORPO = path.join(path, 'parte_superior_corpo.xml')
PARTE_INFERIOR_CORPO = path.join(path, 'parte_inferior_corpo.xml')