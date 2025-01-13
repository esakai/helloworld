#!/usr/bin/env python3

def is_prime(n: int) -> bool:
    """
    素数判定を行う関数
    
    Args:
        n (int): 判定する数値
    
    Returns:
        bool: 素数の場合True、それ以外の場合False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_under_100() -> list[int]:
    """
    100未満の素数を全て求める関数
    
    Returns:
        list[int]: 100未満の素数のリスト
    """
    return [n for n in range(2, 100) if is_prime(n)]

def main():
    """
    メイン関数：100未満の素数を表示する
    """
    primes = find_primes_under_100()
    print("100未満の素数:")
    print(primes)
    print(f"合計: {len(primes)}個の素数")

if __name__ == "__main__":
    main()
