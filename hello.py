#!/usr/bin/env python3

# 注: エラトステネスの篩の実装により、個別の素数判定関数は不要になりました

def find_primes_under_100() -> list[int]:
    """
    エラトステネスの篩を使用して100未満の素数を全て求める関数
    
    Returns:
        list[int]: 100未満の素数のリスト
    """
    # 篩の初期化
    limit = 100
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0と1は素数ではない
    
    # エラトステネスの篩による素数判定
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            # iが素数なら、その倍数を全て除外
            for j in range(i * i, limit, i):
                sieve[j] = False
    
    # 素数のリストを生成
    return [i for i in range(limit) if sieve[i]]

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
