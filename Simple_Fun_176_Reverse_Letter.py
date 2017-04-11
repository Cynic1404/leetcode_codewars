"""Given a string str, reverse it omitting all non-alphabetic characters.
Example

For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".
Input/Output

[input] string str

A string consists of lowercase latin letters, digits and symbols.
[output] a string"""

import re
patt = re.compile('[^\d\W_]')



def reverse_letter(string):
    string = patt.findall(string)
    return ''.join(string[::-1])




"""Test.describe("Basic test")

Test.assert_equals(reverse_letter("krishan"),"nahsirk")

Test.assert_equals(reverse_letter("ultr53o?n"),"nortlu")

Test.assert_equals(reverse_letter("ab23c"),"cba")

Test.assert_equals(reverse_letter("krish21an"),"nahsirk")"""
