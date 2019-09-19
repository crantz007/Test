# Test CamelCase
import  unittest
from unittest import TestCase
import camel

class test_camel_case(unittest.TestCase):

    def test_capitalize(self):
        sentence =[ 'abc','ABC','aBC','ABc']
        capitalized ='Abc'

        for letter in sentence :
            self.assertEqual(capitalized,camel.capitalize(sentence))

    def test_lower_case(self):

        sentence =[ 'abc','ABC','aBC','ABc']
        lower_case = 'abc'

        for letter in sentence :
            self.assertEqual(lower_case,camel.lower(sentence))

    def test_camel_case(self):
       word = camel.sentence({'every','typed','words'})
       self.assertEqual({'every','typed','words'},word)

if __name__ == '__main__':
    unittest.main()