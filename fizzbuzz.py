def fizzbuzz(k):

    

    for i in range(1,k):
        
        if ("3" and "5")  in str(i):
            print("fizzbuzz")
        elif "3" in str(i):
            print("fizz")
        elif "5" in str(i):
            print("buzz")

        elif i % 3 == 0 and i % 5 != 0:
            print("fizz")

        elif i % 3 != 0 and i % 5 == 0:
            print("buzz")

        elif i % 3 ==0 and i % 5 ==0:
            print("fizzbuzz")

        else:
            print(i)






#The following is the same program written with a while loop instead of for.

#    num = 1 
#    while num <= k:
#        if num % 3 == 0 and num % 5 == 0:
#            print("fizzbuzz")
#        elif num % 3 == 0:
#            print("fizz")
#        else: 
#            print(num)
#        num = num + 1



#redux:fizziness

#def fizziness(num):
#    return(num % 3 == 0 or '3' in str(num)  or num % 10 == 3)

#def buzziness(num):
#    return(num % 5 == 0 or '5' in str(num) or num % 10 == 5)

#def redux(k):
#    for k in range(1,k+1):
#        if fizziness(num, 3) and buzziness(num):
#            print("fizzbuzz")
#        elif fizziness(num):
#            print("fizz")
#        elif buzziness(num):
#            print("buzz")
#        else:
#            print(num)

#if __name__ == "__main__":
#    redux(17)
