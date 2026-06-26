class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        result = []
        for s in strs:
            # Sort the characters in the string
            sorted_s = ''.join(sorted(s))

            # Use the sorted string as a key in our hash map
            if sorted_s in freq:
                freq[sorted_s].append(s)
            else:
                freq[sorted_s] = [s]
                
        # Convert dictionary values to our result list
        for val in freq.values():
            result.append(val)
        return result 

        