def run():
    x = 0
#    for i in range(1,101):
#        number = {i: i ** 3}
#        print(number)

    my_dic={i: round(i**0.5, 2) for i in range(1,1001)}
    print(my_dic)

if __name__ == '__main__':
    run()