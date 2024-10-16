"""Iterators, Generators, and List comprehension: task2 """

import re


class Sentence:
    """
        Represents a sentence object.

        Properties:
            - words: Returns a list of words in the sentence.
            - other_chars: Returns a list of non-word characters in the sentence.

        Methods:
            - __repr__: Returns a string representation of the sentence.
            - __getitem__: Retrieves a word or a slice of words from the sentence.
            - __iter__: Returns an iterator over the words in the sentence.
        """
    def __init__(self, sentence: str):
        self.sentence = sentence
        if not isinstance(sentence, str):
            raise TypeError("class only accepts strings")
        if not sentence.endswith(('.', '?', '!')):
            raise ValueError("class only accept full sentences :( ")

    @property
    def words(self):
        """List of words in the sentence."""
        return re.findall(r'\b\w+\b', self.sentence)

    @property
    def other_chars(self):
        """List non-words in the sentence."""
        return re.findall(r'\W', self.sentence)

    def __repr__(self):
        return f"Sentence(words = {len(self.words)}, other_chars = {len(self.other_chars)})"

    def _words(self):
        for word in self.words:
            yield word

    def __getitem__(self, idx):
        return self.words[idx]

    def __iter__(self):
        return SentenceIterator(self)


class SentenceIterator:
    """
    Iterator for iterating over words in a sentence.

    Args:
        sentence: The sentence object or string to iterate over.

    Methods:
        - __iter__: Returns itself as an iterator.
        - __next__: Returns the next word in the sentence.

    Raises:
        - StopIteration: When the end of the sentence is reached.
    """
    def __init__(self, sentence):
        if isinstance(sentence, Sentence):
            self.sentence = sentence
        else:
            self.sentence = Sentence(sentence)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.sentence.words):
            raise StopIteration
        result = self.sentence.words[self.idx]
        self.idx += 1
        return result


if __name__ == "__main__":
    # check not string values.
    # print(Sentence(4))
    # check not complete sentence.
    # print(Sentence("Hello "))
    # check complete string sentence.
    print(Sentence("Hello world!"))
    print(Sentence('Hello world!')._words())
    print(next(Sentence('Hello world!')._words()))
    sentence_instance = Sentence('Hello world!')
    print(sentence_instance.words)
    print(sentence_instance.other_chars)
    print(Sentence('Hello world!')[0])
    print(Sentence('Hello world!')[0:1])

    for w in Sentence('Hello world!'):
        print(w)

    print(iter(Sentence("hello world!")))
    sentence_iterator = SentenceIterator("hello world!")
    print(next(sentence_iterator))
    print(next(sentence_iterator))
