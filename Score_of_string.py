class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ascii= [ord(char) for char in s]
        result_list = []
        
        # Calculate the required absolute differences and store them in the list
        for i in range(1, len(ascii)):
            abs_diff = abs(ascii[i] - ascii[i - 1])
            result_list.append(abs_diff)
        
        score=0
        for i in result_list:
            score+=i    
        return score
                       
# Example usage
solution = Solution()
input_string = "hello"
ascii_codes = solution.scoreOfString(input_string)
print(ascii_codes)
