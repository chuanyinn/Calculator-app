# input a long experssion, more than two numbers and one operator
# this program breaks down the expression on operators according to their
# hierarchy, and calls the function recursively
from operator import add, sub, mul, truediv
operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

exp = raw_input("type your expression here: ")
def calc(expression):
    if expression.isdigit():
        #print expression, "i'm a digit"
        expression = float(expression)
        return expression
    for op in operators.keys():
        if op in expression:
            left, mid, right = expression.partition(op)
            #print left, right, type(left), type(right)
            return operators[op](calc(left), calc(right))
print calc(exp)
