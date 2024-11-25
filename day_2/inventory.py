from collections import Counter

with open('input') as input:
    box_ids = input.readlines()

def checksum(box_ids: list[str]) -> int:

    def has_two_repeat(box_id: str) -> bool:
        return 2 in Counter(box_id).values()
    def has_three_repeat(box_id: str) -> bool:
        return 3 in Counter(box_id).values()

    twice  = [has_two_repeat  (box_id) for box_id in box_ids].count(True)
    thrice = [has_three_repeat(box_id) for box_id in box_ids].count(True)

    return twice * thrice

def find_closest(box_ids: list[str]):

    def matching(a_box_id: str, another_box_id: str) -> str:
        return ''.join([s for (s, t) in zip(a_box_id, another_box_id) if s == t])
    
    return max([matching(v, w) for v in box_ids for w in box_ids if v != w], key=len)

with open('output', 'w') as output:
    output.write( str(checksum(box_ids)) + '\n')
    output.write( str(find_closest(box_ids)) + '\n')