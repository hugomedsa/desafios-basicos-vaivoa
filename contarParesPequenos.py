def contarParesPequenos(array_a,array_b,constante_k):
  array_b.reverse()
  pares_pequenos = 0
  for index, numero in enumerate(array_a):
    if int(f'{numero}{array_b[index]}') < constante_k:
      pares_pequenos+=1

  return pares_pequenos


#EXEMPLO
a = [1, 2, 3,1]
b = [1, 2, 3,4]
k = 31

contarParesPequenos(a, b, k)








