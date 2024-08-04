# チャレンジ1: テストと検証

## 説明
テストに関する知識を活用し、次の要件を満たすようにしてください。
- このチャレンジで必須の要件は「富士」だけです。
- 「キリマンジャロ」はオプションです。

## 標準レベルの要件
次の2つの引数を受け取る関数 `my_assert` をPythonで書いてください。
1. `expr` はブール値として評価される式です。
2. `msg` はオプションのメッセージであり、`expr` が `False` と評価された場合に `msg` を返します。
3. `msg` が提供されていない場合に汎用エラーメッセージを返すようにします。

次に、`my_assert` を使用して、ここに書かれている関数をテストします。「# ----ここにコードを書いてください----」というコメント以降にコードを書いてください。

```python
# ----これらの関数を変更する必要はありません----

names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----*/
# ----難易度: 富士----

# `my_assert` をここに定義し、以降のテストに使用してください。

# `contains` 用のテスト `test_contains` を作成してください

# `add_name` 用のテスト `test_add_name` を作成してください

# `add_two` 用のテスト `test_add_two` を作成してください

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください

# `greeting` 用のテスト `test_greeting` を作成してください


# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
```
