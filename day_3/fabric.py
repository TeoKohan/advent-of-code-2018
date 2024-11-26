from functools import partial
import re

class Claim:
    def __init__(self, id: int, left: int, top: int, width: int, height: int) -> None:
        self.id: int = id
        self.left: int = left
        self.top: int = top
        self.width: int = width
        self.height: int = height

with open('input') as input:
    claims = input.readlines()

claims = map(partial(re.findall, r'(\d+)'), claims)
claims = [map(int, claim) for claim in claims]
claims = [Claim(*claim) for claim in claims]

def calculate_claim_map(claims: list[Claim]) -> dict[(int, int), int]:

    def write_claim(claim: Claim, claim_map: dict[(int, int), int]) -> None:
        for i in range(claim.top, claim.top + claim.height):
            for j in range(claim.left, claim.left + claim.width):
                claim_map[(i, j)] = (claim_map[(i, j)] if (i, j) in claim_map else 0) + 1

    claim_map: dict[(int, int), int] = { }
    for claim in claims:
        write_claim(claim, claim_map)
    
    return claim_map

def overlapping_claims(claims: list[Claim]) -> int:
    claim_map: dict[(int, int), int] = calculate_claim_map(claims)
    return [value >= 2 for value in claim_map.values()].count(True)

def non_overlapping_claim(claims: list[Claim]) -> Claim:
    
    def is_claimed_only_once(claim: Claim) -> bool:
        for i in range(claim.top, claim.top + claim.height):
            for j in range(claim.left, claim.left + claim.width):
                if claim_map[(i, j)] != 1:
                    return False
        return True 
    
    claim_map: dict[(int, int), int] = calculate_claim_map(claims)
    return next(claim for claim in claims if is_claimed_only_once(claim))

with open('output', 'w') as output:
    output.write( str(overlapping_claims(claims)) + '\n')
    output.write( str(non_overlapping_claim(claims).id) + '\n')