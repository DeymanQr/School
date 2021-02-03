alph = '0123456789abcdefghijklmnopqrstuvwxyz'


def from16to10(a: str):
    if a[0] == '-':
        return from16to10(a[1:]) * -1
    if len(a) < 2:
        return alph.index(a)
    return from16to10(a[:-1]) * 16 + alph.index(a[-1])


def from10to2(a: int, leng):
   b =  a < 0
   if b:
      a *= -1
   answ = ''
   while a > 0:
       answ = str(a%2) + answ
       a //= 2
   while len(answ) < leng:
       answ = '0' + answ
   if b:
      answ = '-' + answ
   return answ


def from2to10(a: int):
   if a < 0:
      return from2to10(a*-1) * -1
   if a // 10 < 1:
       return a%2
   return from2to10(a//10)*2 + a%10


def from16to2(a: str):
   b = a[0] == '-'
   if b:
      a = a[1:]
   answ = ''
   while a:
       answ = from10to2(alph.index(a[-1]), 4) + answ
       a = a[:-1]
   if b:
      answ = '-' + answ
   return int(answ)


def from2to16(a: int):
   b = a < 0
   if b:
      a *= -1
   answ = ''
   while a > 0:
       answ = alph[from2to10(a % int(10**4))] + answ
       a //= 10000
   if b:
      answ = '-' + answ
   return answ


def from2to8(a):
   b = a < 0
   if b:
      a *= -1
   answ = ''
   while a > 0:
       answ = alph[from2to10(a % int(10**3))] + answ
       a //= 1000
   if b:
      answ = '-' + answ
   return answ


def from16to8(a):
   return from2to8(from16to2(a))


def fromanyto10(a: str, b: int):
   if a[0] == '-':
      return fromanyto10(a[1:], b) * -1
   if len(a) < 2:
      return alph.index(a)
   return fromanyto10(a[:-1], b) * b + alph.index(a[-1])


def from10toany(a: int, b: int):
   c =  a < 0
   if c:
      a *= -1
   answ = ''
   while a > 0:
       answ = alph[a%b] + answ
       a //= b
   if c:
      answ = '-' + answ
   return answ


def fromanytoany(a: str, b: int, c: int):
   return from10toany(fromanyto10(a, b), c)

