#!/usr/bin/env python3
import unittest
from hello import find_primes_under_n

class TestPrimeNumbers(unittest.TestCase):
    """素数計算機能のテストクラス"""

    def test_negative_input(self):
        """負の数を入力した場合、空のリストが返されることを確認"""
        self.assertEqual(find_primes_under_n(-1), [])

    def test_zero_input(self):
        """0を入力した場合、空のリストが返されることを確認"""
        self.assertEqual(find_primes_under_n(0), [])

    def test_one_input(self):
        """1を入力した場合、空のリストが返されることを確認"""
        self.assertEqual(find_primes_under_n(1), [])

    def test_two_input(self):
        """2を入力した場合、空のリストが返されることを確認"""
        self.assertEqual(find_primes_under_n(2), [])

    def test_three_input(self):
        """3を入力した場合、[2]が返されることを確認"""
        self.assertEqual(find_primes_under_n(3), [2])

    def test_small_range(self):
        """10未満の素数が正しく計算されることを確認"""
        self.assertEqual(find_primes_under_n(10), [2, 3, 5, 7])

    def test_hundred_range(self):
        """100未満の素数が正しく計算されることを確認"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                   43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(find_primes_under_n(100), expected)

    def test_large_range(self):
        """1000未満の素数の個数が正しいことを確認（個数のみ検証）"""
        primes = find_primes_under_n(1000)
        self.assertEqual(len(primes), 168)  # 1000未満の素数は168個

if __name__ == '__main__':
    unittest.main()
