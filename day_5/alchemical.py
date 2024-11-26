import re

with open('input') as input:
    formula: str = input.readline().rstrip()

def reduce_formula(formula: str) -> str:

    def react(formula: str) -> str:
        formula, n = re.subn(r'([a-zA-Z])(?!\1)(?i:\1)', '', formula)
        return formula
    
    while len(formula) > len(formula := react(formula)):
        pass

    return formula

def advanced_reduce_formula(formula: str, eliminated_reagent: str) -> str:
    formula, _ = re.subn(r'(?i)'+eliminated_reagent, '', formula)
    return reduce_formula(formula)

def most_efficient_formula(formula: str) -> str:
    return min((advanced_reduce_formula(formula, chr(char)) for char in range(ord('a'), ord('z')+1)), key = lambda x: len(x))

with open('output', 'w') as output:
    output.write( str(len(reduce_formula(formula))) + '\n')
    output.write( str(len(most_efficient_formula(formula))) + '\n')