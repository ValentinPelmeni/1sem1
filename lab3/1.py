import turtle as t
import random as rd#    После подключения модулей лучше делать отступ в одну строку для улучшения читабельности

for i in range(100):   
    t.forward(rd.randint(0, 100))#   Пробел после запятой (pep8)
    t.left(rd.randint(0, 359))#  Пробел после запятой (pep8)
