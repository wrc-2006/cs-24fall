a=input().lstrip('0')  #a为0时处理结果为空字符串
b=input().lstrip('0')
if not a:
    a='0'
if not b:
    b='0'
print(int(a)+int(b))

'''
或者直接：
print(int(input())+int(input()))
'''