import time


a = "There is a Dust"
b = ""

def loading():
    print("loading......")

    time.sleep(5)

def main():
  while True :
    choose = input("Chose a or b : ")

    if choose.lower() == "a":
        loading()
        print(a)
        loading()
        print("Program Stopped")
        break
    elif choose.lower() == "b":
       loading()
       print('Program continew')
       
       
    else:
       print('Invalis Values')


if __name__ == "__main__":
   main()
