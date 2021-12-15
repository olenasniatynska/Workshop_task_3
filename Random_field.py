import random
comp_ships_list = []

def Random_field(n):
    # filling the playing field
    field = []
    for i in range(12):
        temp = []
        for j in range(12):
            temp.append('.')
        field.append(temp)

    ships = [4, 3, 2, 1]
    for k in range(3, -1, -1):
        t = ships[k]
        while t > 0:
            t -= 1
            done = False
            while (done == False):
                napr = random.randint(1, 2)
                if napr == 1:
                    I = random.randint(1, 10)
                    J = random.randint(1, 7)
                    chek = True
                    for i in range(I - 1, I + 2):
                        for j in range(J - 1, J + k + 2):
                            if field[i][j] == '#':
                                chek = False
                                break
                    if chek == True:
                        temp = []
                        for j in range(J, J + k + 1):
                            field[I][j] = '#'
                            temp.append((I, j))
                        if n == 1: comp_ships_list.append(temp)

                        done = True
                else:
                    I = random.randint(1, 6)
                    J = random.randint(1, 10)
                    chek = True
                    for i in range(I - 1, I + k + 3):
                        for j in range(J - 1, J + 2):
                            if field[i][j] == '#':
                                chek = False
                                break
                    if chek == True:
                        temp = []
                        for i in range(I, I + k + 1):
                            field[i][J] = '#'
                            temp.append((i, J))
                        if n == 1: comp_ships_list.append(temp)
                        done = True
    return field

if __name__ == '__main__':
    comp_field = Random_field(1)
    for i in comp_field:
        for j in i:
            print(j,end = ' ')
        print()
