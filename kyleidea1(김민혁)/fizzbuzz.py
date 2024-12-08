def play():
    for i in range(15):
        if i%3 == 0:
            fizz()
        elif i%5 == 0:
            buzz()
        elif i%3 == 0 and i%5 == 0:
            fizzbuzz()
        else:
            print(i)
    return

def fizz(): #민혁
    # 3의 배수에서 fizz 를 출력하는 함수를 작성해주세요.
    pass

def buzz(): #정희
    # 5의 배수에서 fizz 를 출력하는 함수를 작성해주세요.
    pass

def fizzbuzz(): #주송
    # 15의 배수에서 fizz 를 출력하는 함수를 작성해주세요.
    pass

#이런 식으로 하든.. 