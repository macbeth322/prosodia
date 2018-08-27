from ..bnf.parser import lang as bnflang
from ..bnf.transform import lt as bnftransform
from .text import bnfrepeattext

ALLOWED_SYMBOLS = r'| !#$%&()*+,-./:;>=<?@[\]^_`{}~'

lang = bnftransform.transform(bnflang.parse(bnfrepeattext))
