import string
ALPHABET = string.ascii_lowercase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        def get_new_words(word: str):
            for i in range(len(word)):
                for c in ALPHABET:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList:
                        yield new_word

        queue = [(beginWord, 1)]
        while queue:
            word, level = queue.pop(0)
            if word == endWord:
                return level
            for new_word in get_new_words(word):
                queue.append((new_word, level+1))
                wordList.remove(new_word)
        return 0
        