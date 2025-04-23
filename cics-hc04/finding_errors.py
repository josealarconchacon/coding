#CSci 127 Teaching Staff
#October 2017
#A program that converts hex numbers to decimal, but filled with errors...  
# Modified by:  Jose Alarcon Chacon
# Email: jose.alarconchacon76@login.cuny.edu

def convert(s): # fix the function header to def, not define
     """ Takes a hex string as input.
     Returns decimal equivalent.
     """

     total = 0
     
     for c in s: # fix missing colon at the end
          total = total * 16
          ascii = ord(c) # fix the missing parenthesis at the end
          if ord('0') <= ascii <= ord('9'): # fix missing quotes
               #It's a decimal number, and return it as decimal:
               total = total+ascii - ord('0')
          elif ord('A') <= ascii <= ord('F'): # fix mismatched quotes
               #It's a hex number between 10 and 15, convert and return:
               total = total + ascii - ord('A') + 10
          elif ord('a') <= ascii <= ord('f'): # fix elif and assignment operator
               #Check if they used lower case:
               #It's a hex number between 10 and 15, convert and return:
               total = total + ascii - ord('a') + 10 # fix the operator
          else:
               #Not a valid number!
               return(-1)
     return(total)

def main(): # fix missing colon
    hexString = input("Enter a number in hex: ") # fix mismatched quotes
    print("The number in decimal is", convert(hexString)) # fix prnt to print


#Allow script to be run directly:
if __name__ == "__main__":
     main()
 