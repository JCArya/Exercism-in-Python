def slices(series, length):

        

          

    if length < 0:

        

          

        raise ValueError("slice length cannot be negative")

        

          

    elif length == 0:

        

          

        raise ValueError("slice length cannot be zero")

        

          

    elif length > len(series) and series != "":

        

          

        raise ValueError("slice length cannot be greater than series length")

        

          

    elif series == "":

        

          

        raise ValueError("series cannot be empty")

        

          

    else:

        

          

        liste =[]

        

          

        for i in range(0,len(series)-length+1):

        

          

            liste.append(series[i:i+length])

        

          

        return liste