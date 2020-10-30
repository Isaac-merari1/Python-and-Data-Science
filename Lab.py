import random
#Q1
#print("Hello world") 
#world = "World"
#print("Hello",  world )

#Q2
#number = int(input( "please enter a number\n"))8
#if (number % 2 == 0):
#    print(" even number")
#elif (number % 2 == 1):
 #   print(" odd number") 
#else:
#    print("invalid")

#Q3
#name = " merari "
#age = 100
#print(" my name is %s and my age is %d %(name , age))

# Q4
#print("Rsndom number between 1 and 10")
#guess_number int(input(" Guess your number"))
#random_number = random.radiant(1,10)

#while (guess_number is random):
 #   guess_number = int(input(" you guessed wrong \ try again"))
  #  print(f"{random_number}  is the random number")


#Q5
#numbers_list = [1,4,9,16,25]
#for number in numbers_list:
 #   print(number)

# number_tuple = (1,4,9,16,25)   
 #for number in number_tuple:
  #   print(number)


     #Q6
     age = int(input(" enter your age"))
     total = 0
     start = 1
     

     while start <= age:
         total += start
         start

     for i in range(1, age, +1):
         total +=i

         months = total * 12
         days = total * 365
         hours = total * 8760

         sum_ages = range (1, age +1)
         final_sum = sum(sum_ages)
          sum_ages = 



          #fibonacci
          x,y = 0,1
          count = 0

          while count <= 21:
              count +=1
              print(y)
              x,y = y, x+y 

              #Q8
              name = "ISAAC ADU"
              print(name[-1])

              for i in name:
                  print(i, end =  ":")

        #Q9
        def countable(li, num):
        print(" Enter 10 numbers")
        number_list = []
        

        count = 1

        while count <= 10:
            number = int(input("Enter number:"))

            if (number in range(1,9)):
                number_list.append(number)
            count += 1

            print(countable(number_list, 5))
            print(number_list.count(5))


            #Q10
            numbers = [1,4,9,16,25]
            odd_numbers = [n for
             n in numbers if n % 2 ==1]
            print(odd_numbers)









            #functions
            #Q1 
            def last_element(list):
                value = list.pop()
                return [value, *list]

                numbers = [1,2,3,4,5]
                print(last_element(numbers))


                #Q3
                def func(list, indeces):
                    li = []
                    for i in indeces:
                        li.append(list[i])
                    return tuple(li)

                    numbers =[11, 221, 312, ]

                    for i in 


                    def func(list, indices):
    li = []
    for i in indices:
        li.append(list[i])
    return tuple(li)

numbers = [11, 221, 312, 1234, 235]
indices = [0,2,4]

print(func(numbers, indices)





























  











