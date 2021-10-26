Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = set('belajar')
>>> B = set('ajar')
>>> C = set('bela')
>>> (A-B)-C
set()
>>> (A-C)-(B-C)
set()
>>> A = set('bela')
>>> B = set('be')
>>> C = set('bel')
>>> (A-B)-C
{'a'}
>>> (A-C)-(B-C)
{'a'}
>>> 