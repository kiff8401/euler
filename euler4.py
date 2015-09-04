# Basically brute forced the stuff, not a solution that I am pround of 
def getLargestPalindrome(n):
    #print('Getting largest palindromic product output of ' + str(n) + ' digit numbers');
    for seed in range(999,909,-1):
        foundSol = 0;
        for i in range(999,817,-1):
            
            tempStr = str(i) ;
            newNumber = tempStr + tempStr[::-1];

            generatedPalindrome = int(float(newNumber));

            if(generatedPalindrome%seed == 0 and generatedPalindrome/seed < 1000):
                print(generatedPalindrome);
                print(seed);
                print(generatedPalindrome/seed);
                foundSol = 1
                break;
        if(foundSol == 1):
            break;
        

getLargestPalindrome(2);
