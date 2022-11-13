import unittest
from challenges import hex_to_base, fixed_xor

class Set1TestCase(unittest.TestCase):

    def test_hex_to_base(self):
        self.hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        self.b64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(hex_to_base(self.hex_string), self.b64_string)

    def test_fixed_xor(self):
        self.first_xor_string = '1c0111001f010100061a024b53535009181c'
        self.second_xor_string = '686974207468652062756c6c277320657965'
        self.result = '746865206b696420646f6e277420706c6179'

if __name__ == '__main__':
    unittest.main()