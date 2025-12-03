import random
from matrix import Matrix

# Továrna na matice, má vždy pevně stanovené dimenze maticí - všechny matice čtvercové a jsou stejného rozměru (1x1, 2x2, 3x3, 4x4, ...)
class MatrixFactory:

    """
    10 bodů
    TODO: Inicializujte MatrixFactory. Jaké atributy bude potřebovat továrna na matice? Potřebuje nějaké vystavovat?
    """
    def __init__(self, size):
        self._size = size
        self._storage = []
    """
    10 bodů
    TODO:
    Vygeneruje náhodnou matici n*n (n je dimenze matice)  - každý prvek bude číslo 0 až 9 včetně.
    Novou matici potom přidá do skladu matic. Náhodný prvek dostanete pomocí random.radint(dolni_hranice, horni_hranice)
    """
    def create_random_matrix(self):
        matrix = []
        for _ in range(self._size):
            row = []
            for _ in range(self._size):
                row.append(random.randint(0, 9))
            matrix.append(row)
        matrix = Matrix(matrix)
        self._storage.append(matrix)

    """
    5 bodů
    TODO:
    Vypište všechny matice spolu s jejich indexy (využívejte metody print ze třídy Matrix). 
    Index 0 
     — — —
    |1|2|6|
     — — —
    |1|2|3|
     — — —
    |1|2|8|
     — — —
    
    Index 1 
     — — —
    |1|2|6|
    — — —
    |1|2|3|
     — — —
    |1|2|8|
     — — —
    Když je seznam matic prázdný, tak vypíše, že žádná továrna žádnou matici nemá.
    """
    def print_all_matrices(self):
        if self._storage == []:
            print("němame")
            return
        for i in range(len(self._storage)):
            print("Index", i)
            self._storage[i].print()
            print()
    """
    5 bodů
    TODO:
    Vypište poslední vytvořenou matici 
    Když je seznam matic prázdný, tak vypíše, že žádná továrna žádnou matici nemá.
    """
    def print_last(self):
        if self._storage == []:
            print("němame")
            return
        print("last matrix")
        self._storage[-1].print()

    """
    15 bodů
    TODO:
    Na vstup dostanete indexy první matice a druhé matice (které jsou ve vašem seznamu matic).
    Vytvoří a přidá do seznamu matic novou matici, která bude součtem dvou předchozích matic.
    Můžete předpokládat, že matice na indexech existují nebo vypsat hlášku, že matice na takových indexech nejsou
    """
    def create_by_sum(self, first_matrix_index, second_matrix_index):
        if first_matrix_index >= len(self._storage) or second_matrix_index >= len(self._storage):
            print("němame")
            return
        sum_matrix = []
        for i in range(self._size):
            row = []
            for j in range(self._size):
                row.append(self._storage[first_matrix_index].matrix[i][j] + self._storage[second_matrix_index].matrix[i][j])
            sum_matrix.append(row)
            
        sum_matrix = Matrix(sum_matrix)
        self._storage.append(sum_matrix)


    """
    15 bodů
    TODO:
    Na vstup dostane index první a druhé matice (které jsou ve vašem seznamu matic).
    Vytvoří a přidá do seznamu matic novou matici, která bude vynásobením dvou předchozích matic.
    Násobení matic je o něco složitější než sčítání. Zkuste nastuovat a napsat. Může pomoct například https://www.youtube.com/watch?v=9BGxMrrQkgk

    Doporučuji využít separátní funkci, která bude dostane řádek první matice a sloupec druhé matice a vrátí prvek, který vznikne součtem součinů.
    """
    def create_by_multiplication(self, first_matrix_index, second_matrix_index):
        if first_matrix_index >= len(self._storage) or second_matrix_index >= len(self._storage):
            print("němame")
            return
        mul_matrix = []
        matrix1 = self._storage[first_matrix_index].matrix
        matrix2 = self._storage[second_matrix_index].matrix
        for i in range(self._size):
            row = []
            for j in range(self._size):
                number = 0
                for k in range(self._size):
                    number += matrix1[i][k] * matrix2[k][j]
                row.append(number)
            mul_matrix.append(row)
        mul_matrix = Matrix(mul_matrix)
        self._storage.append(mul_matrix)

if __name__ == "__main__":
    tovarna = MatrixFactory(2)
    
    tovarna._storage.append(Matrix([[1,2],[3,4]]))
    tovarna._storage.append(Matrix([[5,6],[7,8]]))
    tovarna.create_by_multiplication(0,1)
    
    
    print(tovarna._storage)
    tovarna.print_all_matrices()