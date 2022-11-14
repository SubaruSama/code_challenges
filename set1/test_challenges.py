import unittest

from challenges import fixed_xor, hex_to_base


class Set1TestCase(unittest.TestCase):

    def test_hex_to_base(self):
        self.hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        self.b64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(hex_to_base(self.hex_string), self.b64_string)

    def test_fixed_xor(self):
        self.first_xor_string = '1c0111001f010100061a024b53535009181c'
        self.second_xor_string = '686974207468652062756c6c277320657965'
        self.result = '746865206b696420646f6e277420706c6179'

        # Check if the function fixed_xor is checking if the inputs provided
        # are the same size. If not, it should throw and exception.
        with self.assertRaises(AssertionError) as context_manager:
            fixed_xor(self.first_xor_string, self.second_xor_string[:-1])
        self.assertEqual(context_manager.exception.args[0], 'The inputs MUST be the same size')

        # Check if the return of xored strings are equal to result
        self.assertEqual(fixed_xor(self.first_xor_string, self.second_xor_string), self.result)

if __name__ == '__main__':
    unittest.main()