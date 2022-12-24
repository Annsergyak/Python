#Новогодний тест
import easygui
easygui.msgbox('Это викторина на знание новогодних традиций')
'OK'
otvet=''
score=0

otvet = easygui.buttonbox('1. Когда в Древней Руси начинался год?',
choices=['1 января', '1 июня', '1 марта'])
if otvet != '1 марта':
    easygui.msgbox('Неправильный ответ')
else:
    easygui.msgbox('Ваш ответ правильный '+otvet)
    score+=1

otvet = easygui.buttonbox('2. В каком году начали праздновать НГ?',
choices=['998', '1700', '1905'])
if otvet != '1700':
    easygui.msgbox('Неправильный ответ')
else: easygui.msgbox('Ваш ответ правильный '+otvet)