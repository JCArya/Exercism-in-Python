def recite(start, take=1):
    
    l = []

    for i in range(take):

        c1 = start - i
        
        c2 = start - i - 1
        
        s1 = "bottles"
        
        s2 = "bottles"

        if c1 == 1:
            
            l.append("1 bottle of beer on the wall, 1 bottle of beer.")

            l.append("Take it down and pass it around, no more bottles of beer on the wall.")
        if c1 == 0:
            
            l.append("No more bottles of beer on the wall, no more bottles of beer.")

            l.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        
        if c1 > 1:

            if c2 == 1:
                
                s2 = "bottle"

            a = str(c1) + " " + s1 + " of beer on the wall, " + str(c1) + " " + s1 + " of beer."

            b = "Take one down and pass it around, " + str(c2) + " " + s2 + " of beer on the wall."

            l.append(a)
            
            l.append(b)

        if i + 1 < take:

            l.append("")     

    return l

        

          