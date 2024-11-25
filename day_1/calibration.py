from itertools import cycle, tee
from collections.abc import Iterable
import re

with open('input') as input:
    readings: Iterable[int] = map(int, re.findall(r'([+-]\d+)', input.read()))

def final_reading(readings: Iterable[int]) -> int:
    return sum(readings)

def repeat_reading(readings: Iterable[int]) -> int:
    current_value: int = 0
    read_values: set[int] = set()
    loop: Iterable[int] = cycle(readings)

    while not current_value in read_values:
        read_values.add(current_value)
        current_value += next(loop)
    
    return current_value

with open('output', 'w') as output:
    readings_final, readings_repeat = tee(readings)
    output.write( str(final_reading(readings_final)) + '\n')
    output.write( str(repeat_reading(readings_repeat)) + '\n')