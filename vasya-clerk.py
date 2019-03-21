"""
kyu6. The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.
Examples:

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change
"""

def tickets(people):
    cnt25 = 0
    cnt50 = 0
    for note in people:
        if note == 25:
            cnt25 += 1    
        elif note == 50:
            if cnt25 == 0:
                return "NO"
            else:
                cnt25 = cnt25 - 1
                cnt50 += 1
        elif note == 100:
            if (cnt50 < 1):
                if cnt25 < 3:
                    return "NO"
                cnt25 = cnt25 - 3
            else:
                if cnt25 < 1:
                    return "NO"
                else:
                    cnt50 = cnt50 - 1
                    cnt25 = cnt25 - 1
                
    return "YES"

"""OTHER SOLUTION"""
def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'
