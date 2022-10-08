# ARRAY DE INTEIROS
def contarMediaAritmetica(array):
    arith_avg = []
    for interge in array:
        if array.index(interge) == 0:
            previous_num = 0
        else:
            previous_num = array[array.index(interge) - 1]
        if array.index(interge) == len(array)-1:
            next_num = 0
        else:
            next_num = array[array.index(interge) + 1]
        if interge*2 == (previous_num + next_num):
            arith_avg.append(interge)
        else:
            pass

    return print(arith_avg)


#EXEMPLO
array = [0,1,10,40,45.5,51,4,2,4]
contarMediaAritmetica(array)

