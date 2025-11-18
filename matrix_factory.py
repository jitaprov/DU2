import random
from matrix import Matrix

# Továrna na matice, má vždy pevně stanovené dimenze maticí - všechny matice čtvercové a jsou stejného rozměru (1x1, 2x2, 3x3, 4x4, ...)
class MatrixFactory:

    """
    10 bodů
    TODO: Inicializujte MatrixFactory. Jaké atributy bude potřebovat továrna na matice? Potřebuje nějaké vystavovat?
    """

    """
    10 bodů
    TODO:
    Vygeneruje náhodnou matici n*n (n je dimenze matice)  - každý prvek bude číslo 0 až 9 včetně.
    Novou matici potom přidá do skladu matic. Náhodný prvek dostanete pomocí random.radint(dolni_hranice, horni_hranice)
    """
    def create_random_matrix(self):
        pass

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
        pass

    """
    5 bodů
    TODO:
    Vypište poslední vytvořenou matici 
    Když je seznam matic prázdný, tak vypíše, že žádná továrna žádnou matici nemá.
    """
    def print_last(self):
        pass


    """
    15 bodů
    TODO:
    Na vstup dostanete indexy první matice a druhé matice (které jsou ve vašem seznamu matic).
    Vytvoří a přidá do seznamu matic novou matici, která bude součtem dvou předchozích matic.
    Můžete předpokládat, že matice na indexech existují nebo vypsat hlášku, že matice na takových indexech nejsou
    """
    def create_by_sum(self, first_matrix_index, second_matrix_index):
        pass


    # Můžete a nemusíte využít, pomocná metoda pro create_by_multiplication. Případně smažte
    def _multiplication_partial_sum(self, first_matrix, second_matrix, first_matrix_row, second_matrix_col):
        pass

    """
    15 bodů
    TODO:
    Na vstup dostane index první a druhé matice (které jsou ve vašem seznamu matic).
    Vytvoří a přidá do seznamu matic novou matici, která bude vynásobením dvou předchozích matic.
    Násobení matic je o něco složitější než sčítání. Zkuste nastuovat a napsat. Může pomoct například https://www.youtube.com/watch?v=9BGxMrrQkgk

    Doporučuji využít separátní funkci, která bude dostane řádek první matice a sloupec druhé matice a vrátí prvek, který vznikne součtem součinů.
    """
    def create_by_multiplication(self, first_matrix_index, second_matrix_index):
        pass