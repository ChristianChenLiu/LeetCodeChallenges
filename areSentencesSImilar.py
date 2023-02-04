class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): 
            return False 
        
        adj = collections.defaultdict(set)
        for a, b in similarPairs: 
            adj[a].add(b)
            adj[b].add(a)
        
        for i in range(len(sentence1)): 
            if sentence1[i] != sentence2[i] and sentence2[i] not in adj[sentence1[i]]: 
                return False 
        return True 