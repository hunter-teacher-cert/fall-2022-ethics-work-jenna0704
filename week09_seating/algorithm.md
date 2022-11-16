### Write up a description of the algorithm you will implement

## check_needs(traveler_disctionary)
This function is used to determine whether a traveler needs to be seated with their companion.A traveler needs to be seated with their companion if they are 15 years or younger or if they have accessibility needs. 
This function will take in a dictionary of travelers in a group, the keys are the names for the travelers in the group and the values are true or false indicating whether they need to be sitted with their companion. 
This function will loop through each name in the traveler_dictionary and check if the traveler is 15 years or younger or if they have accessibility needs, and return the value. 


## simulate_family_size()
generate random family size assuming 40% chance that the traveler is traveling alone


## simulate_travelers(family_size)
simulate random travelers that have special needs and need to be sitted together


## get_adj_seats(plane, family_size)


### family size of 2
Case 1: 'win', 'avail'\
Case 2: 'avail', 'avail'\
Case 3: 'avail', 'win'

### family size of 3
Case 1:'win', 'avail', 'avail'\
Case 2:'avail', 'avail', 'avail'\
Case 3:'avail', 'avail', 'win'\
