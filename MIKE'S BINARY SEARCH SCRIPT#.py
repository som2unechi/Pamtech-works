'''
This is a script to demonstrate the implementation of a binary search on a list of sorted dictionaries
containing a serial number and name
Author: Michael Olu
'''


import time


# creating a list of 1000 elements for test purposes
def create_list(range_value):#look at the bottom of the page to get the arguments of the function.
    x = []
    for i in range(range_value):
        d = {'sn': i, 'name': f'name_{i}'}#refer to the arguments as mentioned above
        x.append(d)
    print(x)
    return x




class Search:
    def __init__(self, data): #passing a function in the class
        self.data = data

    # Binary search method
    def binary_search(self, sn):#argument sn was called from the bottoom of the script
        t = time.time()
        x = self.data
        iteration = 0

        # Creates a loop for search operation
        while True:#what is true
            iteration += 1

            # time delay to fully detect the difference between the binary search and a linear probe search
            time.sleep(0.0000000000000000000001)#what does this time function really delay?

            # checks if the list contains enough elements to initiate a binary search operation
            if len(x) > 1:

                # divides the list into equal parts x1 and x2
                print(len(x))
                x1 = x[:int(len(x) / 2)]
                x2 = x[int(len(x) / 2):]
                print(x1)
                print(x2[0]['sn'])
                print(sn)


                #checks if the target serial number is greater than the serial number of the first element of list x2
                if sn >= x2[0]['sn']:

                    # checks if the target serial number is the first element in list x2. If true, a match has been
                    # found and the operation is completed
                    if x2[0]['sn'] == sn:
                        return f'record found with binary search: {x2[0]}, time taken: {time.time() - t}seconds' \
                               f' with {iteration} iterations'

                    # replaces the new search list with x2 if the target serial number is greater than the first element
                    # of x2. This means that the target serial number is still on the right side of the list.
                    else:
                        x = x2

                else:
                    # checks if the target serial number is the last element if list x1. If true, a match has been
                    # found and the operation is completed
                    if sn == x1[len(x1) - 1]['sn']:
                        return f'record found with binary search: {x1[len(x1) - 1]}, time taken: {time.time() - t}seconds' \
                               f' with {iteration} iterations'

                    # replaces the new search list with x1 if the target serial number is less than the last element
                    # of x1. This means that the target serial number is still on the left side of the list.
                    else:
                        x = x1

            # Only executes if there is only one element in the search list
            elif len(x) == 1:

                # Checks if the target serial number is the element in the list, if true, a match has been found and thr
                # operation has been completed.
                if x[0]['sn'] == sn:
                    return f'record found with binary search: {x[0]}, time taken: {time.time() - t}seconds' \
                               f' with {iteration} iterations'
                else:
                    return f'record not found with binary search!,  time taken: {time.time() - t}seconds' \
                               f' with {iteration} iterations'

    # Linear search method
    def linear_probe(self, sn):
        t = time.time()
        x = self.data
        iteration = 0
        for i in x:
            iteration += 1
            time.sleep(0.0000000000000000000001)
            if sn == i['sn']:
                return f'record found with linear probing: {i}, time taken: {time.time() - t}seconds' \
                        f' with {iteration} iterations'
        return f'record not found with linear probing!, time taken: {time.time() - t}seconds' \
               f' with {iteration} iterations'


test_list = create_list(1000)
search = Search(test_list)

SN=int(input('write your search input figure here:'))

search_1 = search.binary_search(sn=SN)
print(search_1)

search_2 = search.linear_probe(sn=SN)
print(search_2)

#SCRIPT CAN BE VERY USEFUL IN BRUTEFORCE TECHNOLOGY
#RECOMMENADATIONS; TRY USING METHODS AND CLASSES IN THE REGION OF THE FIRST FUNCTION.