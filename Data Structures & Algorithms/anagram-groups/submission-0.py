class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for word in strs:
            sorted_words=tuple(sorted(word))
            hashmap[tuple(sorted_words)].append(word)
                    
        return list(hashmap.values())