def total(basket):

        

          

    book_count = [0,0,0,0,0] #intialize empty list for counting the amount of every book

        

          

    for i in range(1,6):

        

          

        book_count[i-1] = basket.count(i) #Count amount of every book

        

          

    sets = [0] * max(book_count) #initialize empty list for the number of sets we can make, which is equal to the max amount of any book

        

          

    for j in range(max(book_count)): #fill up the sets by looping through the book_count list

        

          

        for k in range(len(book_count)):

        

          

            if book_count[k] > 0:

        

          

                book_count[k] -= 1

        

          

                sets[j]+=1

        

          

    count_5 = 0 

        

          

    count_3 = 0

        

          

    bill = 0

        

          

    prices = [800,1520,2160,2560,3000] #prices for set of 1, 2 ...

        

          

    for k in sets: #Count number of sets with 5 books and 3 books, because if there is a set of 5 and 3, it should always be replaced by two sets of 4.

        

          

                    #This is the only possible instance where it is beneficial to not completely maximize a set.

        

          

        if k == 5:

        

          

            count_5 += 1

        

          

        if k == 3:

        

          

            count_3 += 1

        

          

        bill += prices[k-1]

        

          

    bill -= min(count_5,count_3)*40 #For every combination of a set of 5 and 3, subtract 40 cents (3000+2160 - (2*2560) = 40)

        

          

    return(bill)

        

          