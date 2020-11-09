'''class Person:

    def __init__(self, name):
        self.name = name

    def greet(self, name):
        return f'Hello {name}, my name is {self.name}'

from random import randint
class photoManager:

    names = []

    def __init__(self, name):
        self.name = name
        photoManager.names.append(self.name)

    def nameExists(name):
        if name in photoManager.names:
            return True
        return False

def generate_name():

    name = ''.join((chr(randint(65, 90)) for i in range(6)))
    if photoManager.nameExists(name):
        generate_name()
    return name'''

from operator import add, sub, mul, truediv
class Calculator(object):

    def my_oper(self, symbol, num1, num2):

        operation = {
            '+': add(num1, num2),
            '-': sub(num1, num2),
            '*': mul(num1, num2),
            '/': truediv(num1, num2)
            }
        return operation[symbol]

    def str_to_list(self, string):

        expr = []
        num = ''
        symb = [('*','/'),('+','-')]
        for i in range(len(string)):
            if string[i].isdigit() or string[i] == '.':
                num += string[i]
                if i + 1 >= len(string):
                    expr.append(float(num))
                    num = ''
                elif string[i+1] != '.':
                    if not string[i+1].isdigit():
                        expr.append(float(num))
                        num = ''
            if string[i] in symb[0]:
                expr.append(string[i])
            if string[i] in symb[1]:
                expr.append(string[i])

        i = 0
        while '*' in expr or '/' in expr:

            if expr[i] == '*' or expr[i] == '/':
                expr[i] = self.my_oper(expr[i], expr[i-1], expr[i+1])
                del (expr[i+1])
                del (expr[i-1])
                i -= 2
            i += 1

        i = 0
        while '+' in expr or '-' in expr:

            if expr[i] == '+' or expr[i] == '-':
                expr[i] = self.my_oper(expr[i], expr[i - 1], expr[i + 1])
                del (expr[i + 1])
                del (expr[i - 1])
                i -= 2
            i += 1

        return expr[0]

    def simplification(self, string):
        center = self.str_to_list(string[string.rfind('(') + 1:string.find(')')])
        new = string[:string.rfind('(')]+str(center)+string[string.find(')')+1:]
        return new

    def evaluate(self, string):

        if '(' in string:
            string = self.simplification(string)
        return self.str_to_list(string)

if __name__ == '__main__':

    print(Calculator().evaluate("30*(((400+7)*2*6+2))-5"), '=195355')
    #print(Calculator().evaluate("(((((((5)))))))"))
    print(Calculator().evaluate("2*(2*(2+(2+1)))+2"))
    #print(Calculator().evaluate("5*2-1.2+2"), '=10.8')  #11
    #print(Calculator().evaluate("5*2-(1.2+2)"), '=6.8')  # 11
    #print(Calculator().evaluate("1.235+1"))
