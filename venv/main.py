from random import randint


def generator(lenth, upperletter, lowerletter, integer, simbols):
    simbolsforpassword = upperletter + lowerletter  + integer + simbols
    password = ''
    for i in range(lenth):
        password += str(simbolsforpassword[randint(0, len(simbolsforpassword) - 1)])
    return password

upperletter = [chr(x) for x in range(65, 91)]
lowerletter = [chr(x) for x in range(97, 123)]
integer = [x for x in range(10)] + [x for x in range(10)] + [x for x in range(10)]
simbols = '! " # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _` { | } ~'.split(' ')
# print(upperletter)
# print(lowerletter)
# print(integer)
# print(simbols)
simbolsforpassword = upperletter + lowerletter  + integer + simbols
# print(simbolsforpassword)
for _ in range(15):
    print(generator(10, upperletter, lowerletter, integer, simbols))
