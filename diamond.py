__author__ = 'user'


#처음에 파이링 생성되지 않았을때 처리를 하지 못했습니다
with open('diamond','a+') as f:
    data = f.read()
    print(data)

s = input('정수의 크기를 입력하시오> ')
size = int(s)
dia = ''

for y in range(0,size*2+1):
    for x in range(0, size*2+1):
        if y<=x+size and y>=x-size and y<=-x+3*size and y>=-x+size:
            print('*', end=" ")
            dia += '*'
        else:
            print(' ', end=" ")
            dia += ' '
    print(' ')
    dia += '\n'

with open('diamond','w') as f:
    f.write(dia)
