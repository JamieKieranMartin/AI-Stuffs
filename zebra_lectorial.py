#
#   Adapted from Peter Norvig (one of the authors of the CAB320 AI textbook)
#

# Last modified on 2019-02-23 
# by f.maire@qut.edu.au



import itertools  # for the 'permutations' iterators


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1


def zebra_puzzle_01():
    '''
    A first attempt to solve the zebra puzzle
    
    Enumerate permutations and test all candidates
    
    Return a tuple (WATER, ZEBRA) indicating their house numbers.
    '''
    #  _ is a general purpose "throwaway" variable name to indicate
    #  that part of a function result is being deliberately ignored
    first, _, middle, _, _ = [1, 2, 3, 4, 5]
    
    # orderings is the list of all permutations of   [1, 2, 3, 4, 5]
    orderings =     [(0, 1, 2, 3, 4), (0, 1, 2, 4, 3), (0, 1, 3, 2, 4), (0, 1, 3, 4, 2), (0, 1, 4, 2, 3), 
    (0, 1, 4, 3, 2), (0, 2, 1, 3, 4), (0, 2, 1, 4, 3), (0, 2, 3, 1, 4), (0, 2, 3, 4, 1), 
    (0, 2, 4, 1, 3), (0, 2, 4, 3, 1), (0, 3, 1, 2, 4), (0, 3, 1, 4, 2), (0, 3, 2, 1, 4), 
    (0, 3, 2, 4, 1), (0, 3, 4, 1, 2), (0, 3, 4, 2, 1), (0, 4, 1, 2, 3), (0, 4, 1, 3, 2), 
    (0, 4, 2, 1, 3), (0, 4, 2, 3, 1), (0, 4, 3, 1, 2), (0, 4, 3, 2, 1), (1, 0, 2, 3, 4), 
    (1, 0, 2, 4, 3), (1, 0, 3, 2, 4), (1, 0, 3, 4, 2), (1, 0, 4, 2, 3), (1, 0, 4, 3, 2), 
    (1, 2, 0, 3, 4), (1, 2, 0, 4, 3), (1, 2, 3, 0, 4), (1, 2, 3, 4, 0), (1, 2, 4, 0, 3), 
    (1, 2, 4, 3, 0), (1, 3, 0, 2, 4), (1, 3, 0, 4, 2), (1, 3, 2, 0, 4), (1, 3, 2, 4, 0), 
    (1, 3, 4, 0, 2), (1, 3, 4, 2, 0), (1, 4, 0, 2, 3), (1, 4, 0, 3, 2), (1, 4, 2, 0, 3), 
    (1, 4, 2, 3, 0), (1, 4, 3, 0, 2), (1, 4, 3, 2, 0), (2, 0, 1, 3, 4), (2, 0, 1, 4, 3), 
    (2, 0, 3, 1, 4), (2, 0, 3, 4, 1), (2, 0, 4, 1, 3), (2, 0, 4, 3, 1), (2, 1, 0, 3, 4), 
    (2, 1, 0, 4, 3), (2, 1, 3, 0, 4), (2, 1, 3, 4, 0), (2, 1, 4, 0, 3), (2, 1, 4, 3, 0), 
    (2, 3, 0, 1, 4), (2, 3, 0, 4, 1), (2, 3, 1, 0, 4), (2, 3, 1, 4, 0), (2, 3, 4, 0, 1), 
    (2, 3, 4, 1, 0), (2, 4, 0, 1, 3), (2, 4, 0, 3, 1), (2, 4, 1, 0, 3), (2, 4, 1, 3, 0), 
    (2, 4, 3, 0, 1), (2, 4, 3, 1, 0), (3, 0, 1, 2, 4), (3, 0, 1, 4, 2), (3, 0, 2, 1, 4), 
    (3, 0, 2, 4, 1), (3, 0, 4, 1, 2), (3, 0, 4, 2, 1), (3, 1, 0, 2, 4), (3, 1, 0, 4, 2), 
    (3, 1, 2, 0, 4), (3, 1, 2, 4, 0), (3, 1, 4, 0, 2), (3, 1, 4, 2, 0), (3, 2, 0, 1, 4), 
    (3, 2, 0, 4, 1), (3, 2, 1, 0, 4), (3, 2, 1, 4, 0), (3, 2, 4, 0, 1), (3, 2, 4, 1, 0), 
    (3, 4, 0, 1, 2), (3, 4, 0, 2, 1), (3, 4, 1, 0, 2), (3, 4, 1, 2, 0), (3, 4, 2, 0, 1), 
    (3, 4, 2, 1, 0), (4, 0, 1, 2, 3), (4, 0, 1, 3, 2), (4, 0, 2, 1, 3), (4, 0, 2, 3, 1),
    (4, 0, 3, 1, 2), (4, 0, 3, 2, 1), (4, 1, 0, 2, 3), (4, 1, 0, 3, 2), (4, 1, 2, 0, 3),
    (4, 1, 2, 3, 0), (4, 1, 3, 0, 2), (4, 1, 3, 2, 0), (4, 2, 0, 1, 3), (4, 2, 0, 3, 1), 
    (4, 2, 1, 0, 3), (4, 2, 1, 3, 0), (4, 2, 3, 0, 1), (4, 2, 3, 1, 0), (4, 3, 0, 1, 2), 
    (4, 3, 0, 2, 1), (4, 3, 1, 0, 2), (4, 3, 1, 2, 0), (4, 3, 2, 0, 1), (4, 3, 2, 1, 0)]

    
    for red, green, ivory, yellow, blue in orderings:
        for Englishman, Spaniard, Ukranian, Japanese, Norwegian in orderings:
            for dog, snails, fox, horse, ZEBRA in orderings:
                for coffee, tea, milk, oj, WATER in orderings:
                    for OldGold, Kools, Chesterfields, LuckyStrike, Parliaments in orderings:
                        #  We ignore some of the constraints for simplicity
                        if ( Englishman == red # constraint 2
                             and Spaniard == dog # constraint 3
                             # missing other constraints
                             #           :
                            ):
                            return WATER, ZEBRA
    return None, None


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#   Remark on zebra_puzzle_01
#       if  'orderings'  was a very large list, it would be significantly more 
#        efficient to use a generator to enumerate the permutations.


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# A 2nd attempt ...
# We use 'iterators' 
# Enumerate and test all candidates

def zebra_puzzle_02():
    '''
    Small improvement: do not create the list orderings
    Return a tuple (WATER, ZEBRA) indicating their house numbers.
    '''

    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    for red, green, ivory, yellow, blue in itertools.permutations(houses):
        for Englishman, Spaniard, Ukranian, Japanese, Norwegian in itertools.permutations(houses):
            for dog, snails, fox, horse, ZEBRA in itertools.permutations(houses):
                for coffee, tea, milk, oj, WATER in itertools.permutations(houses):
                    for OldGold, Kools, Chesterfields, LuckyStrike, Parliaments in itertools.permutations(houses):
                        if ( Englishman == red # constraint 2
                             and Spaniard == dog # constraint 3
                             
                             # missing other constraints
                             
                            ):
                            return WATER, ZEBRA
    return None, None
    
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                    
def zebra_puzzle_03():
    '''
    Include all constraints
    Return a tuple (WATER, ZEBRA) indicating their house numbers.
    '''

    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    for red, green, ivory, yellow, blue in itertools.permutations(houses):
        for Englishman, Spaniard, Ukranian, Japanese, Norwegian in itertools.permutations(houses):
            for dog, snails, fox, horse, ZEBRA in itertools.permutations(houses):
                for coffee, tea, milk, oj, WATER in itertools.permutations(houses):
                    for OldGold, Kools, Chesterfields, LuckyStrike, Parliaments in itertools.permutations(houses):
                        # test the constraints
                        if ( Englishman == red # constraint 2
                             and Spaniard == dog # constraint 3
                             and coffee == green # constraint 4
                             and Ukranian == tea # constraint 5
                             and imright(green, ivory) # constraint 6
                             and OldGold == snails # constraint 7
                             and Kools == yellow # constraint 8
                             and milk == middle # constraint 9
                             and Norwegian == first # constraint 10
                             and nextto(Chesterfields, fox) # constraint 11
                             and nextto(Kools, horse) # constraint 12
                             and LuckyStrike == oj # constraint 13
                             and Japanese == Parliaments # constraint 14
                             and nextto(Norwegian, blue) # constraint 15
                             ):
                            return WATER, ZEBRA

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# The function  zebra_puzzle_03  might take a lot of time to run to completion

# $ HOW TO ESTIMATE ITS RUNNING TIME?


import time  # t = time.clock()



def zebra_puzzle_04(nmax):
    '''
    Test at most nmax candidates
    Return a tuple (WATER, ZEBRA) indicating their house numbers.
    '''
    #  _ is a general purpose "throwaway" variable name to indicate
    #  that part of a function result is being deliberately ignored
    n = 0  # count the number of candidates tested 
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    for red, green, ivory, yellow, blue in itertools.permutations(houses):
        for Englishman, Spaniard, Ukranian, Japanese, Norwegian in itertools.permutations(houses):
            for dog, snails, fox, horse, ZEBRA in itertools.permutations(houses):
                for coffee, tea, milk, oj, WATER in itertools.permutations(houses):
                    for OldGold, Kools, Chesterfields, LuckyStrike, Parliaments in itertools.permutations(houses):
                        # test the constraints

                        if (n < nmax):
                            n +=1
                        else:  
                            print('reached maximum number of tests')                              
                            return None, None 
                        
                        if ( Englishman == red # constraint 2
                             and Spaniard == dog # constraint 3
                             and coffee == green # constraint 4
                             and Ukranian == tea # constraint 5
                             and imright(green, ivory) # constraint 6
                             and OldGold == snails # constraint 7
                             and Kools == yellow # constraint 8
                             and milk == middle # constraint 9
                             and Norwegian == first # constraint 10
                             and nextto(Chesterfields, fox) # constraint 11
                             and nextto(Kools, horse) # constraint 12
                             and LuckyStrike == oj # constraint 13
                             and Japanese == Parliaments # constraint 14
                             and nextto(Norwegian, blue) # constraint 15
                             ):
                            return WATER, ZEBRA


##    ------------------------------------------------------------------------------

# In the prac of Week 02, we will see how to improve dramatically 'zebra_puzzle_04'


##if False:
if __name__ == "__main__":
    # estimate running time of zebra_puzzle_01_a
    nmax = 10*10**6
    t0 = time.time()
#    w,z = zebra_puzzle_02()
    w,z = zebra_puzzle_03()
#    w,z = zebra_puzzle_04(nmax)
    t1 = time.time()
    if w is not None:
        print ("Found a solution:  Water = {}, Zebra = {} ".format(w, z))
    else:
        print ("Took {0} seconds to try unsuccessfully {1} candidates".format(t1-t0, nmax))



##    ------------------------------------------------------------------------------















