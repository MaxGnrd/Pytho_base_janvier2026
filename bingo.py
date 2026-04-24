import random

def gen_grid():
    grid=[[],[],[],[]]
    list_numbers=[]
    for i in range(16):
        number=random.randint(1,99)
        while number in list_numbers:
            number=random.randint(1,99)
        list_numbers.append(number) #permet de rajouter un nombre à la liste de nombres
    return list_numbers

def choose_number():
    number=random.randint(1,99)
    return number
def check_grid(grid,number):
    new_grid=[]
    for num in grid:
        if num==number:
            new_grid.append('X')
        else:
            new_grid.append(num)
    return new_grid
def is_line_complete(grid):
    valid=False
    for i in range(4):               #table de 4 pour que ce soit plus elegant
        line=grid[i*4:(i+1)*4] 
        if line==['X','X','X','X']:
            valid=True
            break
    return valid
if __name__=="__main__":
    grid=gen_grid()

    for i in range (100):
        number=choose_number()
        grid=check_grid(grid,number)
        print(number , grid)
        valid=is_line_complete(grid)
        if valid:
            print ("Bingo,vive les crêpes à la queue de taupe!")
            break
