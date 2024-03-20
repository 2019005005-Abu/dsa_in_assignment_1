# 1. Write a Python program to find maximum between two numbers.
# > r
def Finding_maximumNumbe(Number1, Number2):
    if Number1 > Number2:
        print(Number1)
    else:
        print(Number2)


N1 = int(input("N1="))
N2 = int(input("N2="))
Finding_maximumNumbe(N1, N2)


# Write a Python program to find maximum between three numbers.
class FindingMaxOfThree:
    def __init__(self, Num1, Num2, Num3):
        self.Num1 = Num1
        self.Num2 = Num2
        self.Num3 = Num3

    def max_of_three(self):
        if self.Num1 > self.Num2 and self.Num1 > self.Num3:
            return self.Num1
        elif self.Num2 > self.Num1 and self.Num2 > self.Num3:
            return self.Num2
        else:
            return self.Num3


Max = FindingMaxOfThree(10, 20, 30)
max_of_three = Max.max_of_three()
print("Maximum number:", max_of_three)

# Write a Python program to check whether a number is negative, positive or zero.

number_check = int(input("Enter the number to check negative,posotive or  zero"))
if number_check < 0:
    print("Number is Negative")
elif number_check > 0:
    print("Number is positive")
elif number_check == 0:
    print("Number is zer0")
else:
    print("Unvalid")

# Write a Python program to check whether a number is divisible by 5 and 11 or not.
number_check1 = int(
    input(" give a  to check whether a number is divisible by 5 and 11 or not")
)

if number_check1 % 5 == 0 and number_check1 % 10 == 0:
    print("number is divisible by 5 and 11")
else:
    print("number is not  divisible by 5 and 11")


# Write a Python program to check whether a number is even or odd.


def checkingEven_Odd_num(num):
    if num % 2 == 0:
        print("Even Num")
    else:
        print("Odd Num")


n = int(input("Even /Odd="))
ChekindNum = checkingEven_Odd_num(n);
print(ChekindNum)


#Write a Python program to check whether a year is leap year or not.

checkingLeapYea=int(input('check whether a year is leap year or not.'))

if checkingLeapYea%4==0 or checkingLeapYea%100==0 or checkingLeapYea%400==0:
    print('Leap Year');
else:
      print('Not Leap Year');
    
##Write a Python program to check whether a character is alphabet or not.

print("Enter a Character: ")
c = input()
if c>='a' and c<='z':
    print("\nIt is an alphabet")
elif c>='A' and c<='z':
    print("\nIt is an alphabet")
else:
    print("\nIt is not an alphabet!")
    
    
##Write a Python program to input any alphabet and check whether it is vowel or
#consonant.

X=input('Enter the character to check vowel  consonant ');
if  X=='A' or X=='a' or X=='E' or X=='e' or X=='I' or X=='i' or X=='O' or X=='o' or X=='U' or X=='u':
    print('vowel')
else:
    print('consonant ')
    
##Write a Python program to input any character and check whether it is alphabet, digit or special character.

D=input('input any character and check whether it is alphabet, digit or special character')

if (D>='A' and D<='Z') or (D>='a' and D<='z'):
    print('Alphabet');
elif D>=0 and D<=0:
    print('Dight');
else:
    print('special character')
    

'''
Write a Python program to input an amount from the user and print the minimum
number of notes (Rs. 500, 100, 50, 20, 10, 5, 2, 1) required for the amount. How to find
the minimum number of notes required for a given amount in Python programming?
Program to determine the minimum number of notes required for the given
denominations. Logic to find the minimum number of denominations for a given
amount in a Python program.
'''
def minimum_notes(amount):
    denominations = [500, 100, 50, 20, 10, 5, 2, 1]
    notes_count = {}

    for denomination in denominations:
        notes_count[denomination] = amount // denomination
        amount %= denomination

    return notes_count

def main():
    amount = int(input("Enter the amount: "))
    notes = minimum_notes(amount)

    print("Minimum number of notes:")
    for denomination, count in notes.items():
        if count > 0:
            print(f"{count} notes of Rs. {denomination}")

if __name__ == "__main__":
    main()
