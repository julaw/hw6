import re
import unittest

file1='regex_sum_42.txt'

def sumNums(fileName):
    file=open(fileName)
    count = 0
    for line in file:
        line = line.rstrip()
        x = re.findall('[0-9]+', line)
        for num in x:
            count+= int(num)
    return count


sumNums(file1) 


def countWord(fileName, word):
    pass

def listURLs(fileName):
    pass


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
