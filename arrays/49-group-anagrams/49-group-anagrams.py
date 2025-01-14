# create a hashmap sortedstring: [unsorted strings]
# iterate through list -> O(m)
# for each string, sort the string -> O(nlogn)
# add sorted string to key and unsorted to value
# return values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {} # {sorted_string: [unsorted_string, ...]}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in anagrams_dict:
                anagrams_dict[sorted_string] = []
            anagrams_dict[sorted_string].append(string)
        return list(anagrams_dict.values())
    
# Time complexity: O(m * nlogn ) where m is the number of strings and n is the length of the longest string

# Faster solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list) # {(tuple of char_count): [strings]}
        max_chars = 26
        for string in strs:
            # Creates a list of size 26 for each char, initialized to 0
            # Used to store the count of each character in the string.
            char_count = [0] * max_chars
            for char in string:
                # ord(ch) gives the ASCII value of the character ch
                # Subtracting ord('a') from it normalizes the index
                # so that 'a' corresponds to 0, 'b' to 1, ..., and 'z' to 25
                # increment the count by one
                char_count[ord(char) - ord('a')] += 1
            anagrams_dict[tuple(char_count)].append(string)
        return list(anagrams_dict.values())

# Ex. For this input: 
# strs = ["eat","tea","tan","ate","nat","bat"]
# Resulting hashmap should look like: 
# {
# (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
# (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
# (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']
# }

# Time complexity: O(m * n) where m is the number of strings and n is the length of the longest string