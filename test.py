def romanToInt(s):
    symbol = ["I","V","X","L","C","D","M"]
    num = [1,5,10,50,100,500,1000]
    i, result = len(s) - 1, 0
    while i >= 0:
        if i > 0 and symbol.index(s[i]) > symbol.index(s[i-1]):
            result += num[symbol.index(s[i])] - num[symbol.index(s[i-1])]
            i -= 2
        else:
            result += num[symbol.index(s[i])]
            i -= 1
    return result

print(romanToInt('MCMXCIV'))