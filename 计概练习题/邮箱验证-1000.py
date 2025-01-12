while True:
    try:
        s=input()
        if s.count('@')==1 and s[0]!='@' and s[0]!='.' and s[-1]!='@' and s[-1]!='.' and '.' in s[s.index('@'):] and s[s.index('@')+1]!='.' and s[s.index('@')-1]!='.':
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
