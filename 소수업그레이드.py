list_num = [i for i in range(2, 100)]
list_prime = []

while list_num:
    prime = list_num[0]                       
    list_prime.append(prime)                   
    list_num = [x for x in list_num if x % prime != 0]  