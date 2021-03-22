def magic_num(n):
    final_num = ""
    for i in str(n):
        final_num += str(int(i)**2)
    return int(final_num)

print(magic_num(1769))