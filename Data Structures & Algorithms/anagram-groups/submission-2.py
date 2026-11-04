from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = defaultdict(list)


        for word in strs:
            sorted_w = ''.join(sorted(word))
            dictionary[sorted_w].append(word)
        
        return list(dictionary.values())
        