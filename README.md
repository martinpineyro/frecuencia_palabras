SCRIPT PARA DETERMINAR LA FRECUENCIA CON LA QUE APARECE CADA PALABRA DE ARCHIVOS PDF



1) El programa procesa el archivo pdf y genera un string con todas las palabras del documento
2) Filtra caracteres que se quieran dejar fuera: '01234567890!"#$%&()*+,-./:;<=>¿?@[\\]^_`{|}~\t\n'
3) Genera un Diccionario con las palabras y su correspondiente contador
4) Incluye lista negra de palabras para dejar fuera del análisis ciertas palabras específicas: 
   blacklist =['o', 'e', 'de', 'que', 'el', 'y', 'a', 'la', 'los', 'un', 'una', 'en', 'las', 'del', 'hay', 'más', 'está', 'estos', 'eso', 'este', 'esta', 'estas', 'para', 'con', 'se', 'como', 'al', 'por', 'as', 'por', 'su', 'sus', 'lo', 'es', 'ha', 'han', 'no', 'nos', 'entre']
5) Calcula el porcentaje del total de palabras del documento que representa el contador
6) Genera un archivo .csv con todas las palabras, el contador y porcentaje
