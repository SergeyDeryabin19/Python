def chek_zero(our_number):
    chek_len = len(str(our_number))
    print(chek_len)
    if chek_len==3:
        firs_number = 0
        second_number = our_number[0]
        our_number=[firs_number, second_number]
    
    return print(our_number)

our_number=[5]
chek_zero(our_number)