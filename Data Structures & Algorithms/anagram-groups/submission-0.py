class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for x in strs:
        
            if tuple(sorted(x)) in group:
                group[tuple(sorted(x))].append(x)
            else:
                group[tuple(sorted(x))] = [x]

        return list(group.values())