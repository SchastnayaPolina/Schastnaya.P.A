string = input()
len_n = 0
temporary_len_n = 0
for i in string:
    if i == 'н':
        temporary_len_n += 1
    else:
        if len_n < temporary_len_n:
            len_n = temporary_len_n
        temporary_len_n = 0
string = string.replace('!', '.')
print(len_n)
print(string)