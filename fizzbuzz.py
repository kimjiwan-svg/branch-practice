def fizz_buzz(num):
    if num % 15 == 0:
        return 'fizzbuzz'

    elif num % 3 == 0:
        return 'fizz'

    elif num % 5 == 0:
        return 'buzz'

    else:
        return f'{num}'

if __name__ == '__main__':
    num = int(input('정수를 입력하시오:'))
    print(fizz_buzz(num))
