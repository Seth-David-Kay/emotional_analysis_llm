import sys
import analysis

tweet = input("Enter the text: ")
num_iterations = input("Enter number of times to run: ")

while True:
    try:
        num_iterations = int(num_iterations)
        break
    except:
        num_iterations = input("Enter a number: ")
        continue

analysis.choose_all(tweet, num_iterations)
