#!/usr/bin/env/ python3
#
# Author: Jiri Kalina <jiri.kalina.jr@gmail.com>
# Date: 07-05-2021  10:57:23
# Title: generators.py
# Annotation: Generators/FunctionalInPython - by James Powell
#             Python as Functional paradigm lang
#             https://www.youtube.com/watch?v=RdhoN4VVqq8&list=LL&index=7&t=374s


# FUNCTIONAL PROGRAMING EXAMPLE
template = '{region:<{align}}   {profit:<14,.0f}'.format
# print(template)
def output(markets, write=print, template=template):
    align = max(map(len, markets))
    for region, profit in markets.items():
        line = template(region=region, profit=profit, align=align)
        write(line)

output({region:Accounting(profit) for region, profit in markets.items()})

#   console-output:
# ----------------------------
# Central America     -675,140
# US                -2,724,620
# Antarctica                 -
# Asia              -3,614,396
# EU                  -771,665
# CEMEA             -3,480,172


# FIBONACI
def fib(a=1, b=1):
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fib(),10)))

# Task: look at "islice" doocumentation