for i in range(ord('а'), ord('я') + 1):
    print(chr(i), end=' ')
    if i == ord('е'):
        print('ё', end=' ')
