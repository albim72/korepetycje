
 
# funkcja zwraca liczbę odwróconą (kolejność cyfr)

def reverse(n): 
    rev = 0
    while (n != 0): 
        rev = (rev * 10) + (n % 10) 
        n //= 10
    return rev 
  
# funkcja znajduje sumę liczb z pozycji parzystch i nieparzystych



def getSumEven(n): 
  
    n = reverse(n) 
    sumEven = 0
    c = 1
  
    while (n != 0): 
  
        # jeśli c jest parzysta, to cyfra jest pobierana z parzystego miejsca
       
        if (c % 2 == 0): 
            sumEven += n % 10
        
        n //= 10
        c += 1
  
    return sumEven 


def getSumOdd(n): 
  
    n = reverse(n) 
    sumOdd = 0
    
    c = 1
  
    while (n != 0): 
  
        # jeśli c jest parzysta, to cyfra jest pobierana z parzystego miejsca
       
        if (c % 2 != 0): 
            sumOdd += n % 10
        
        n //= 10
        c += 1
  
    return sumOdd 
    

def getSum(n): 
  
    sumOdd = getSumOdd(n)
    sumEven = getSumEven(n)
  
    return sumOdd + sumEven 
  


