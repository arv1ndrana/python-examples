import unittest

def prime_number(number):
    if number < 2:
        return False
    
    for index in range(2,number):
        if number % index == 0:
            return True
        return False

class test_is_prime(unittest.TestCase):
    def unit_test(self):
        self.assertTrue(prime_number(7))
        self.assertTrue(prime_number(1))
        self.assertTrue(prime_number(0))
        self.assertTrue(prime_number(47))
        self.assertTrue(prime_number(887))

if __name__ == '__main__':
    unittest.main()
