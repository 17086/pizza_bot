def order_type(LOW, HIGH, question):
    while True:
        try:
            num = int(input(question))
            if num >= 1 and num <= 2:
                return num
            else: 
                print("Please enter a number between", LOW, "and" , HIGH)
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter a number between", LOW, "and" , HIGH)

LOW = 1
HIGH = 2

question = (f"Enter a number between, {LOW} and {HIGH}")

answer = order_type(LOW, HIGH, question)

print(answer)


