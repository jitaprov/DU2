from matrix_factory import MatrixFactory

"""
Maximum je 110 b
+ max 20 bodů za přehlednost kódu
+ max 10 bodů za uživatelskou přívětivost aplikace - jak hezky se používá
+ max 10 bodů za hezkost metody print u matice - jak hezky vypisuje stav matice

V tomto domácím úkolu budeme vytvářet továrny na matice (vnořené seznamy).
Všechny funkce a třídy (kromě __init__), které se po vás budou chtít implementovat jsou již nadepsané a okomentované.
Rozmyslete si, jaké atributy daná třída potřebuje mít a jaké potřebuje ukazovat i ostatním třídám - a jak zajistit, aby nějaké atributy ostatní třídy nevyužívaly.

Snažte se dodržovat zadání a přemýšlet, jak program udělat, aby se s ním uživateli dobře pracovalo - někam přidat výpis o tom co se děje, někam přidat volný řádek.

Budeme pracovat se třídami:

1. MatrixApp - Má na starosti komunikaci s uživatelem a vznik a zánik továrny na matice

2. MatrixFactory - Vytváří, vypisuje a ukládá si matice. Všechny matice jedné továrny jsou čtvercové a stejně velké. 
   Továrna má i tzv. dimenzi - jak velké matice vytváří. Továrna dimenze 3 má matice velikosti 3x3. Dimenze 2 má matice velikosti 2x2

3. Matice - Vnořený seznam, v tomto úkolu bude vždy čtvercová - stejný počet řádků a sloupců. Vnořený seznam obalujeme do třídy abychom nad ním mohli definovat metody např. print

"""


class MatrixApp:

    """
    10 bodů
    Inicializujte MatrixApp, zamyslete, jaké atributy bude potřebovat. Jak budete reprezentovat neexistující továrnu?
    """
    def __init__(self):
        self._factory = None
        
    """
    10 bodů
    TODO:
    1. Vypíše možnosti a nechá uživatele nějakou zvolit.
    Zvolenou možnost vrátí. 
    Když bude chtít uživatel např. Vytvořit novou matici sečtením dvou matic tak metoda vrátí číslo 3.

    Možnosti:
        1: Vypsat matice
        2: Vytvořit novou náhodnout matici
        3: Vytvořit novou matici sečtením dvou matic
        4: Vytvořit novou matici vynásobením dvou matic
        5: Zničit současnou továrnu
        6: Ukončit program
    """
    def choose_option(self):
        print("co pro Vás mohu udělat?")
        option = int(input("zvolte mžnost: "))
        if 0 < option < 7:
            print("jistě, provedu!")
            return option
        print("si naozaj chorý? němame")
        return self.choose_option()

   
    """
    10 bodů
    TODO:
    Nekonečný cyklus zpostředkovájící komunikaci s uživatelem. Nejdříve zkontrolujte zda existuje nějaká továrna a případně ji vytvořte.
    Pokud potřebujete nějaké další informace - dimenze nové továrny, indexy matic, která se mají sčítat, tak vždy vypište prompt uživateli a požadovaná čísla načtěte.
    """
    def _get_index(self):
        print("pokud jste chtěl vědet, jaké matice jsou v nabídce, měl jste zvolit možnost 1, teď Vám zbývá jen hádat ")
        return int(input("první matice: ")), int(input("druhá matice: ")) 

    def start_app(self):
        print("vítejte v továrně na matice")
        while(True):
            if self._factory == None:
                self._factory = MatrixFactory(int(input("aktuálně nemáte žádnou továrnu, matice jakého rozměru byste si přál/a vytvářet? ")))
            option = self.choose_option()
            if option == 1:
                self._factory.print_all_matrices()
            elif option == 2:
                self._factory.create_random_matrix()
                print("vytvořil jsem novou náhodnou matici")
            elif option == 3:
                index = self._get_index()
                self._factory.create_by_sum(index[0], index[1])
                print("vytvořil jsem novou matici pomocí součtu")
            elif option == 4:
                index = self._get_index()
                self._factory.create_by_multiplication(index[0], index[1])
                print("vytvořil jsem novou matici pomocí součinu")
            elif option == 5:
                self._factory = None
                print("zrušil jsem starou továrnu")
            elif option == 6:
                print("tak zdar:) ")
                exit()

                
# Automaticky se zavolá při spuštění souboru
if __name__=="__main__":
    m = MatrixApp()
    m.start_app()