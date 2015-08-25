__author__ = 'user'

inform = []

for x in range(0,1000):
    title = input('책 제목을 입력하세요> ')
    author = input('저자를 입력하세요> ')
    p = input('가격을 입력하세요> ')
    price = int(p)
    inform += ['{0},{1},{2}'.format(title,author,price)]
    information = list(inform)

    sellect = input('더 입력하시겠습니까?(y/n) ')

    if sellect!='y' and sellect!='n':
        sellect = input('다시 입력해주세요(y/n)')
    elif sellect == 'y':
        continue
    else:
        break


data = ''
for x in range(0,len(information)):
    print(information[x])
    data += (information[x] + '\n')

with open('information','a') as f:
    f.write(data)