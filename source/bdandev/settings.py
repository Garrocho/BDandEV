"""
Modulo responsavel pelas configuracoes globais do projeto.
"""

from os import path


# Endereco dos codigos fontes do projeto.
PATH_FONTE = path.abspath(path.dirname(__file__))

# Endereco de dados diversos no projeto.
PATH_DATA = path.normpath(path.join(PATH_FONTE, '..', 'data'))

# Endereco dos arquivos XML
CORPO_INTEIRO = path.join(PATH_DATA, 'corpo_inteiro.xml')
PARTE_SUPERIOR_CORPO = path.join(PATH_DATA, 'parte_superior_corpo.xml')
PARTE_INFERIOR_CORPO = path.join(PATH_DATA, 'parte_inferior_corpo.xml')
