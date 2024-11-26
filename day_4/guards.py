from collections import Counter
import re

with open('input') as input:
    guard_records: list[str] = input.read().splitlines()

sorted_guard_records: list[str] = sorted(guard_records, key = lambda x: re.findall(r'(\d+)', x))

def calculate_guard_minutes(sorted_guard_records: list[str]) -> dict[int, list[int]]:
    guard_minutes: dict[int, list[int]] = dict()

    for guard_record in sorted_guard_records:
        if 'Guard' in guard_record:
            guard: int = int(re.search(r'#(\d+)', guard_record).group(1))
        elif 'asleep' in guard_record:
            sleep_start: int = int(re.search(r':(\d+)', guard_record).group(1))
        else:
            sleep_end:   int = int(re.search(r':(\d+)', guard_record).group(1))
            guard_minutes[guard] = guard_minutes[guard] if guard in guard_minutes else []
            guard_minutes[guard].extend(range(sleep_start, sleep_end))

    return guard_minutes

def sleepiest(sorted_guard_records: list[str]) -> int:
    guard_minutes: dict[int, list[int]] = calculate_guard_minutes(sorted_guard_records)

    sleepyhead: int = max(guard_minutes, key = lambda x: len(guard_minutes[x]))
    minutes_slept: Counter[int] = Counter(guard_minutes[sleepyhead])
    weakpoint: int = max(minutes_slept, key = lambda x: minutes_slept[x])
    return sleepyhead * weakpoint

def most_predictable(sorted_guard_records: list[str]) -> int:
    guard_minutes: dict[int, list[int]] = calculate_guard_minutes(sorted_guard_records)

    predictable: int = max(guard_minutes, key = lambda x: max(Counter(guard_minutes[x]).values()))
    minutes_slept: Counter[int] = Counter(guard_minutes[predictable])
    weakpoint: int = max(minutes_slept, key = lambda x: minutes_slept[x])
    return predictable * weakpoint

with open('output', 'w') as output:
    output.write( str(sleepiest(sorted_guard_records)) + '\n')
    output.write( str(most_predictable(sorted_guard_records)) + '\n')