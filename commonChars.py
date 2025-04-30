def commonChars(self, words: list[str]) -> list[str]:
        first= words[0]
        common = list(first)
        for word in words[1:]:
            next_common = []
            word_list = list(word)
            for char in common:
                if char in word_list:
                    next_common.append(char)
                    word_list.remove(char)
            common = next_common
        return common   
