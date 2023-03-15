"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Fadhil Lawal
Date:   7/1/2020
"""
import a1
src = input("Enter Source Currency: ")
dst = input("Enter Target Currency: ")
amt = input("Enter Original AMount: ")
output = a1.exchange(src,dst,amt)
print("You Can Exchange",amt,src,"for",output,dst,end = ".")
