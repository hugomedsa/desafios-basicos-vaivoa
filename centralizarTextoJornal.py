def centralizarTextoJornal(paragrafos, largura):
  paragrafos_ajustados = ["*"*(largura+2)]
  #------------------------------#------------------------------#------------------------------
  def ajustarStrings(string):
    espacos = largura - len(string.strip())
    if espacos%2==0:
      espaco_antes = espaco_depois = espacos//2
    else:
      espaco_antes = espacos//2
      espaco_depois = espacos//2+1
    paragrafos_ajustados.append(("*"+" "*espaco_antes+string.strip()+espaco_depois*" "+"*"))
  #------------------------------#------------------------------#------------------------------
  for paragrafo in paragrafos:
    string_do_paragrafo = ""
    for string in paragrafo:
      string_do_paragrafo+=" "+string
    if len(string_do_paragrafo.strip()) <= largura:
      ajustarStrings(string_do_paragrafo)
    else:
      for string in paragrafo:
        ajustarStrings(string)
  #-------------------------------#-------------------------------#-------------------------------
  paragrafos_ajustados.append("*"*(largura+2))
  return paragrafos_ajustados


#EXEMPLO
paragrafos = [["hello","world"],
         ["How", "areYou", "doing "],
         ["Please look", "and align", "to center"]]
largura = 20

centralizarTextoJornal(paragrafos, largura)