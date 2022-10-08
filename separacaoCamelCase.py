def separacaoCamelCase(strings,nomeVariavel):
  start = 0
  separadas = []
  for index,letra in enumerate(nomeVariavel):
    if index == 0:
      pass
    else:
      if letra.isupper():
        separadas.append(nomeVariavel[start:index])
        start = index
      else:
        if index == len(nomeVariavel)-1:
          separadas.append(nomeVariavel[start:])
  for c in separadas:
    if c.lower() in strings:
      validacao = True
    else:
      validacao = False
      break
  return print(validacao)


#EXEMPLOS

palavras = ["is", "valid", "right"]
separacaoCamelCase(palavras, 'Isvalid')
separacaoCamelCase(palavras, 'isVaLid')
separacaoCamelCase(palavras, 'isRightValid')
separacaoCamelCase(palavras, 'isrightVaLid')