a="hello"
print('w'in a)
print(a.capitalize())
print(a.center(15,'&'))
print(a.count('e'))
print(a.endswith("o"))
print(a.find('l'))
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.islower())
print(a.isupper())
b="       "
print(b.isspace())
print(a.istitle())
print('2'.join(a))
print(len(a))
print(a.ljust(10,'8'))
print(a.rjust(10,'$'))
print(a.lower())
print(a.upper())
c="            helloo      "
print(c.lstrip())
print(c.rstrip())
d="hello".maketrans('h','p')
print(a.translate(d))
di=a.maketrans('aeiou','12345')
print(a.translate(di))
print(max('13','55'))
print(min('11','-1'))
print(a.replace("o",'i'))
print(a.rfind('i'))
print(a.rindex('o'))
print(a.split('hel'))
print(a.startswith("h"))
print(a.strip('o'))
print(a.swapcase())
print(a.title())
f="123"
print(f.zfill(9))
import textwrap
e=textwrap.wrap("hello",3)
print(e)
