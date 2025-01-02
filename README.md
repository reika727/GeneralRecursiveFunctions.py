# GeneralRecursiveFunctions.py
[この記事](https://qiita.com/reika727/items/b0b2e5c496644c56f0f8)の検証用に作ったプログラムです。

## Example
```python3
# 関数と作用素を組み合わせて関数を作ってみる例
from general_recursive_functions import *

# 定数関数 C0 は常に 0 を返す
print(C0(42, 84, 126)) # 0

# 後者関数と定数関数を合成して 1 を返す関数を作る
print(composition(S, C0)(168)) # 1

# 原始再帰作用素で足し算を作ってみる
print(primitive_recursion(P(1), composition(S, P(2)))(2, 3)) # 2 + 3 = 5
```

```python3
# 定義済みの関数を使ってみる例
from examples import *

print(exponentiate(2, 3)) # 8
print(is_prime(3)) # True
print(is_prime(4)) # False
```

## general_recursive_functions/primitive_recursive_functions
原始再帰関数を形作る関数と作用素を定義しています。

- `C0()`: 定数関数 $C^k_0$ です。
- `S()`: 後者関数 $S$ です。
- `P()` 射影関数 $P^k_i$ です。
- `composition()`: 合成作用素 $\circ$ です。
- `primitive_recursion()`: 原始再帰作用素 $\rho$ です。

## general_recursive_functions
最小化作用素を定義しています。

- `mu()`: 最小化作用素 $\mu$ です。

## examples.py
様々な $\mu$ 再帰関数の実例を定義しています。それぞれの関数の意味については前述の[記事](https://qiita.com/reika727/items/b0b2e5c496644c56f0f8)の方を参照ください。

## test.py
テストコードです。~~全然書いてないけど~~
