class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # (1) Eliminate all dashes
        S = S.replace('-', '')      # 5F3Z2e9w
        
        # (2) maintain a grouping list to save the splited letters
        grouping = []
        
        # (3) Special handle for first group if it's not an exact division
        head = len(S) % K
        if head:
            grouping.append( S[:head] )
        
        # (4) General case:
        for index in range(head, len(S), K ):           # head = len(S) % K
            grouping.append( S[ index : index+K ] )
                
        # (5) Link each group togetger and separated by dash '-'
        return '-'.join( grouping ).upper()