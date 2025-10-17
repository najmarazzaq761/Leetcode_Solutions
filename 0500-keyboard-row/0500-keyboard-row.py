class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Step 1: Create dictionary with keyboard rows
        keyboard = {
            "firstrow": set("qwertyuiop"),
            "secondrow": set("asdfghjkl"),
            "thirdrow": set("zxcvbnm")
        }
        
        result = []  # to store valid words
        
        # Step 2: iterate over each word
        for word in words:
            lower_word = word.lower()  # make it case-insensitive
            first_char = lower_word[0]
            
            # Step 3: find which row the first letter belongs to
            if first_char in keyboard["firstrow"]:
                row = keyboard["firstrow"]
            elif first_char in keyboard["secondrow"]:
                row = keyboard["secondrow"]
            else:
                row = keyboard["thirdrow"]
            
            # Step 4: check if all letters are from the same row
            if all(char in row for char in lower_word):
                result.append(word)
        
        return result
