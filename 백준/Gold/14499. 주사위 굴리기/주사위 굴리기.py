import sys

input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())

mapp = [ list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

class Dice:
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.front = 0
        self.back = 0
        self.left = 0
        self.right = 0
        self.y = 0
        self.x = 0

    def set_yx(self,y,x):
        self.y = y
        self.x = x

    # def print_dice(self):
    #     print('top',self.top, end=" ")
    #     print('bottom',self.bottom, end=" ")
    #     print('front',self.front, end=" ")
    #     print('back',self.back, end=" ")
    #     print('left',self.left, end=" ")
    #     print('right',self.right, end=" ")
    #     print('x',self.x, end=" ")
    #     print('y',self.y)


    def go_down(self):
        tmp = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = tmp
        self.y += 1
        self.copy_num()

    def go_up(self):
        tmp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = tmp
        self.y-=1
        self.copy_num()

    def go_right(self):
        tmp = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = self.top
        self.top = tmp
        self.x += 1
        self.copy_num()

    def go_left(self):
        tmp = self.bottom
        self.bottom = self.left
        self.left = self.top
        self.top = self.right
        self.right = tmp
        self.x -= 1
        self.copy_num()

    def copy_num(self):
        global mapp
        if mapp[self.y][self.x] == 0:
            mapp[self.y][self.x] = self.bottom
        else:
            self.bottom=mapp[self.y][self.x]
            mapp[self.y][self.x] = 0
        print(self.top)

dice = Dice()
dice.set_yx(y,x)

for i,order in enumerate(orders):
    if order == 1 and dice.x + 1 < M:
        dice.go_right()
    elif order == 2 and dice.x - 1 >= 0:
        dice.go_left()
    elif order == 3 and dice.y - 1 >= 0:
        dice.go_up()
    elif order == 4 and dice.y + 1 < N:
        dice.go_down()
    # dice.print_dice()

