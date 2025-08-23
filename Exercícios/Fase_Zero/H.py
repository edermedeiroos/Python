def is_binary_palindrome(num):
    if num < 0: 
        return False
    if num == 0:
        return True
    binario = ''
    temp_num = num
    while temp_num > 0:
        binario = str(temp_num % 2) + binario
        temp_num //= 2
    return binario == binario[::-1]

n_original = int(input(""))
r = n_original

while r >= 0:
    if is_binary_palindrome(r):
        print(r)
        break
    r -= 1