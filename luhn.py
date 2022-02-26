from re import findall, sub

        

          


        

          


        

          

class Luhn:

        

          

    def __init__(self, card_num):

        

          

        self.card = sub(" ", "", card_num)

        

          


        

          

    def valid(self) -> bool:

        

          

        """

        

          

        Runs card number from self.card through Luhn algorithm and returns bool

        

          

        based on whether or not it passes Luhn algorithm validity.

        

          

        """

        

          

        if len(self.card) <= 1 or not self.card.isdigit():

        

          

            return False

        

          

        card_array = [

        

          

            (

        

          

                (double if (double := int(num) * 2) < 10 else double - 9)

        

          

                if index % 2 != 0

        

          

                else int(num)

        

          

            )

        

          

            for index, num in enumerate(list(self.card[::-1]))

        

          

        ]

        

          

        return sum(card_array) % 10 == 0