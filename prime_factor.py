def find_prime_fector(num):
    fector=[]
    divisr=2
    while divisr <= num:
        if num % divisr == 0:
            fector.append(divisr)
            num= num // divisr
        else:
            divisr+=1

    return fector
print(find_prime_fector(60))
