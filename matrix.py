# Reprezentuje matici (vnořený seznam). Pro tento úkol budeme uvažovat pouze čtvercové matice - budou mít stejný počet řádků a sloupců 2x2, 3x3, 4x4 atd

class Matrix:
    """
    10 bodů
    TODO: inicalizujte matici, zamyslete se, jaké by měla mít privátní atributy a jestli nějaké potřebuje vystavovat
    """
    def __init__(self, matrix):
        self.matrix = matrix

    """
    10 bodů + max 10 bonusových bodů za hezkost
    TODO:
    Pěkně vypíše matici ve formátu
    — — —
   |1|2|6|
    — — —
   |1|2|3|
    — — —
   |1|2|8|
    — — —

    Zkuste vymyslet (najít) i řešení jak pěkně vypisovat matice s nějakými prvky delšími, mohla by se hodit medota stringu rjust
    ————— ————— —————
   |    1|    2|    6|
    ————— ————— —————
   |    1|    2|    3|
    ————— ————— —————
   |    1|   22|45648|
    ————— ————— —————
    """
    def print(self):
        length = 0
        for row in self.matrix:
            length = max(max(row), length)
        print(length)
        print(len(self.matrix)* (" " + "—" * len(str(length))))
        for row in self.matrix:
            print("|", end="")
            for column in row:
                print(" " * (len(str(length)) - len(str(column))), column, sep="", end="|")
            print()
            print(len(self.matrix)* (" " + "—" * len(str(length))))
     
    
    def __repr__(self):
       return str(self.matrix)
            
            
            
if __name__ == "__main__":
    matice1 = Matrix([[1, 25436, 3], [4, 5, 74656], [7, 8, 9]])
    matice1.print()