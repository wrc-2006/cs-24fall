n=input()
s=input()
keyboard='qwertyuiopasdfghjkl;zxcvbnm,./'
if n=='R':
    for i in s:
        print(keyboard[keyboard.index(i)-1],end='')
else:
    for i in s:
        print(keyboard[keyboard.index(i)+1],end='')