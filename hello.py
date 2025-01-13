#!/usr/bin/env python3

# 注: エラトステネスの篩の実装により、個別の素数判定関数は不要になりました

def find_primes_under_n(n: int) -> list[int]:
    """
    エラトステネスの篩を使用してn未満の素数を全て求める関数
    
    Args:
        n (int): 上限値（この値未満の素数を求める）
    
    Returns:
        list[int]: n未満の素数のリスト
    
    Raises:
        ValueError: nが2未満の場合
    """
    if n < 2:
        raise ValueError("nは2以上の整数である必要があります")
    
    # 篩の初期化
    sieve = [True] * n
    sieve[0] = sieve[1] = False  # 0と1は素数ではない
    
    # エラトステネスの篩による素数判定
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # iが素数なら、その倍数を全て除外
            for j in range(i * i, n, i):
                sieve[j] = False
    
    # 素数のリストを生成
    return [i for i in range(n) if sieve[i]]

def main():
    """
    メイン関数：100未満の素数を表示する
    """
    n = 100  # 上限値
    primes = find_primes_under_n(n)
    print(f"{n}未満の素数:")
    print(primes)
    print(f"合計: {len(primes)}個の素数")

if __name__ == "__main__":
    main()
