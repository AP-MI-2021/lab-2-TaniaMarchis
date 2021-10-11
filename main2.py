def printMenu():
    print("1.Găsește ultimul număr prim mai mic decât un număr dat.")
    print("2.Determină dacă un număr dat este palindrom.")
    print("3.Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.")
    print("Pentru a inchide, introdu x")


def NrPrim(n):
    '''
    Functia verifica daca un numar este prim sau nu
    :param n: numar intreg
    :return: True, daca numarul este prim sau False, in caz contrar
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    Functia determina cel mai mare numar prim mai mic decat n
    :param n: numar intreg
    :return: cel mai mare numar prim mai mic decat n
    '''
    for i in range(n - 1, 1, -1):
        if NrPrim(i) == True:
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(8) == 7
    assert get_largest_prime_below(22) == 19
    assert get_largest_prime_below(18) == 17

def is_palindrome(n):
    '''
    verifica daca un numar dat este palindrom
    :param n: numar natural
    :return:  True, daca n este palindrom sau False, in caz contrar
    '''
    oglindit=0
    auxiliar=n
    while auxiliar > 0:
        oglindit=oglindit*10+auxiliar%10
        auxiliar=auxiliar//10

    if oglindit==n:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(55) is True
    assert is_palindrome(158) is False
    assert is_palindrome(71) is False
    assert is_palindrome(353) is True

def is_superprime(n):
    '''
    functia verifica daca toate prefixele unui numar sunt prime
    :param n: numar natural
    :return: True, daca numarul este superprim sau False, in caz contrar
    '''
    if n<2:
        return False
    while n>0:
        if n<2:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i=i+1
        n=n//10
    return True

def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(239) is False


while True:
    printMenu()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        n = int(input("Dati nr: "))
        print(get_largest_prime_below(n))
    elif optiune=="2":
        n = int(input("Dati nr: "))
        print(is_palindrome(n))
    elif optiune=="3":
        n = int(input("Dati nr: "))
        print(is_superprime(n))
    elif optiune=="x":
        break
    else:
        print("Optiune gresita")