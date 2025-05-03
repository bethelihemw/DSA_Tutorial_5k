def reverseVowels(self, s: str) -> str:
        vowel = ['A','E','I','O','U','a','e','i','o','u']
        s_list = list(s)
        left = 0
        # "A","E","I","O","U
        right = len(s) -1
        while left < right:
            if s_list[left] in vowel and s_list[right] in vowel:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left += 1
                right -= 1
            elif s_list[left]  in vowel and s_list[right] not in vowel:
                right -= 1
            elif s_list[left]  not in vowel and s_list[right]  in vowel:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s_list)
