class Solution:
    def build_struct(self, words):
        struct = {}
        for idx, word in enumerate(words):
            if word not in struct:
                struct[word] = {idx}
                continue
            struct[word].add(idx)
        return struct

    def findSubstring(self, text: str, words: List[str]) -> List[int]:
        total_words = len(words)
        word_len = len(words[0])
        sub_string_len = total_words * word_len
        text_len = len(text)

        if sub_string_len > text_len:
            return []

        res = []
        struct = self.build_struct(words)

        for start_pos in range(text_len - sub_string_len + 1):
            word_indeces = set()
            flag = True
            for i in range(total_words):
                shift = i * word_len
                cur_word = text[start_pos+shift:start_pos+shift+word_len]
                print(cur_word)
                if cur_word not in struct:
                    flag = False
                    break

                possible_poss = struct[cur_word] - word_indeces
                if possible_poss:
                    pos = possible_poss.pop()
                    word_indeces.add(pos)
                    continue

                flag = False
                break

            if not flag:
                continue

            res.append(start_pos)
        return res
