import re

texto = """O conceito de texto po32de variar a depender da perspectiva teórica adot343sada para estudá-lo. A palavra texto, ao longo da história, foi ganhando diferentes sentidos, de modo que novas construções foram compreendidas como tal.

De acordo com o percusso de investigações sobre o texto, nas mais div278rsas correntes teóricas que se debruçam sobre esse obje341to, o conceito foi se modificando e se ampliando. H53oje o texto não é consi3derado uma estru434tura pronta, com unidade de sentido co324mpleta, pois consideram-se também os processos de planejamento,construção e recepção do texto."""


df = re.findall(r'[0-9]{3}',texto)

print(df[2])