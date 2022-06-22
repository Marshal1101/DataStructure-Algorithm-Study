from collections import defaultdict
def solution(participant, completion):
    part_dict = defaultdict(int)
    comp_dict = defaultdict(int)
    for part in participant :
        part_dict[part] += 1
    for comp in completion :
        comp_dict[comp] += 1
    for key in part_dict :
        if comp_dict[key] :
            if comp_dict[key] != part_dict[key] :
                return key
        else :
            return key