import kata
import unittest

class Test_Generate_Hashtag(unittest.TestCase):
    def tests(self):
        # self.assertEqual(inc_dec.increment(3), 4)
        self.assertEquals(kata.generate_hashtag(''), False, 'Expected an empty string to return False')
        self.assertEquals(kata.generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
        self.assertEquals(kata.generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
        self.assertEquals(kata.generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
        self.assertEquals(kata.generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
        self.assertEquals(kata.generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
        self.assertEquals(kata.generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
        self.assertEquals(kata.generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
        self.assertEquals(kata.generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
        self.assertEquals(kata.generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')

if __name__ == '__main__':
    unittest.main()