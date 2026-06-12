def add(a, b, c=0):
    try:
        # 型チェック：int または float 以外なら -1
        if not isinstance(a, (int, float)):
            return -1
        if not isinstance(b, (int, float)):
            return -1
        if not isinstance(c, (int, float)):
            return -1

        # 境界値チェック：0以上10以下でなければ -2
        if not (0 <= a <= 10):
            return -2
        if not (0 <= b <= 10):
            return -2
        if not (0 <= c <= 10):
            return -2

        # 正常処理
        return int(a + b) + int(c)

    except:
        return -1
