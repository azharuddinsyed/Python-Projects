# Sample calculator program

main_func = input("Enter mathematical operation\n"
                  "(a = add, s=sub, m=multiplication, d=division, o=modulus, "
                  "sq=square, po=power, fa=factorial): ")


#i, j = 1, 0

if (main_func == 'a' or main_func =='s' or main_func=='m' or main_func== 'd' or main_func=='o' or main_func=='po'):

    i, j = 1, 0

    while (j < i):
         a = int(input("Enter first number: "))
         b = int(input("Enter second number: "))
         main_func = input("Enter mathematical operation\n(a = add, s=sub, m=multiplication, d=division, "
                           " o=modulus, po=power): ")
         if main_func == 'a':
            c = a + b
            print("The sum of {} and {} is".format(a, b),c)
            co = input("Do you wish to do another calculation\n(y=yes,n=no):\n")
            if co == 'y':
               i, j = 1, 0
            else:
               print("Bye")
            i, j = 0, 0
         elif main_func == 's':
            c = a - b
            print("The difference of {} and {} is".format(a, b), c)
            co=input("Do you wish to do another calculation\n(y=yes,n=no):\n")
            if co =='y':
                i, j = 1,0
            else:
                print("Bye")
                i, j = 0, 0
         elif main_func == 'm':
              c = a * b
              print("The product of {} and {} is".format(a, b), c)
              co = input("Do you wish to do another calculation\n(y=yes,n=no):\n")
              if co == 'y':
                i, j = 1, 0
              else:
                print("Bye")
                i, j = 0, 0
         elif main_func == 'd':
              c = a // b
              print("The division of {} and {} is".format(a, b), c)
              co = input("Do you wish to do another calculation\n(y=yes,n=no):\n")
              if co == 'y':
                 i, j = 1, 0
              else:
                 print("Bye")
                 i, j = 0, 0
         elif main_func == 'o':
              c = a % b
              print("The modulus of {} and {} is".format(a, b), c)
              co = input("Do you wish to do another calculation\n(y=yes,n=no):\n")
              if co == 'y':
                 i, j = 1, 0
              else:
                 print("Bye")
                 i, j = 0, 0
         elif main_func == 'po':
              power = pow(a, b)
              print("{} to the power of {} is".format(a, b), power)
              co = input("Do you wish to do another calculation\n(y=yes,n=no):\n")
              if co == 'y':
                 i, j = 1, 0
              else:
                 print("Bye")
                 i, j = 0, 0
         else:
            i = 1
            j = 0
            print("Invalid option, start again")

elif main_func == 'sq':
    a=int(input("Enter number:"))
    square = a**2
    print("The square of {} is".format(a),square)

elif main_func == 'fa':
    a=int(input("Enter number: "))
    i=1
    res=1
    while(i<=a):
        if a>0:
            res=res*i
            i+=1
    print("Factorial of {} is:".format(a),res)

else:
    print("You have entered an invalid option")









#else:
#    print("Coding in progress for {func1} or {func2} functions".format(func1="factorial", func2="power"))


