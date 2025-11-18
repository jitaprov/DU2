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
        pass
   
    """
    10 bodů
    TODO:
    Nekonečný cyklus zpostředkovájící komunikaci s uživatelem. Nejdříve zkontrolujte zda existuje nějaká továrna a případně ji vytvořte.
    Pokud potřebujete nějaké další informace - dimenze nové továrny, indexy matic, která se mají sčítat, tak vždy vypište prompt uživateli a požadovaná čísla načtěte.
    """
    def start_app(self):
        #while(True):
        pass
        
# Automaticky se zavolá při spuštění souboru
if __name__=="__main__":
    m = MatrixApp()
    m.start_app()