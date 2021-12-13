## Obecně
- Celkem je zadáno 5 úkolů. Neočekáváme, že je stihnete vypracovat všechny.
- Na vypracování úkolů je 90 minut.
- Během vypracování bude možné zadání i částečná řešení konzultovat se zástupci f. Mergado.
- Úkoly budou vypracovány formou Python scriptů.
- Internet je možné používat k čemukoliv, kromě živé konzultace s jinými osobami.
- Hodnocen bude váš přístup k zadání (zejm. analýza), splnění požadavků, robustnost programu a čistota kódu

## Zadání
### Úkol 1 - Morseova abeceda
- Připravte program, který bude umět kódovat / dekódovat text do / z Morseovy abecedy.
- Uživatel nejdříve bude vyzván k zadání toho, jakou operaci si přeje provést (kódování / dekódování).
- Poté bude zadán textový řetězec (validními znaky jsou číslice, písmena, tečka, pomlčka a lomítko).
 - V Morseově abecedě jsou znaky oddělovány lomítkem a slova dvěma lomítky.
- Podle operace bude text zakódován nebo dekódován, případně bude vypsána hláška, že text je nevalidní.

#### Příklady vstupů a očekávané výstupy
| Vstup                                                            | Výstup                                      |
| ---------------------------------------------------------------- | ------------------------------------------- |
| Ahoj kamarade                                                    | .-/..../---/.---//-.-/.-/--/.-/.-./.-/-../. |
| --/---/.-./..././---/...-/-.-/.-//.---/.//-.-./---/---/.-..      | Morseovka je cool                           |
| Ahoj kamaráde!                                                   | Invalid input!                              |
| -_/--                                                            | Invalid input!                              |


### Úkol 2 - Prvočísla a palindromy
- Připravte program, který vypíše první prvočíslo, které je větší než uživatelem zadaná hodnota a které je zároveň palindromem.

#### Příklady vstupů a očekávané výstupy
| Vstup    | Výstup          |
| -------- | --------------- |
| 100      | 101             |
| 100000   | 1003001         |
| xy       | Invalid input!  |

### Úkol 3 - Hokej
- Z webu https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089 vyscrapujte výsledky všechny zápasů
- Vyfiltrujte zápasy, které vyhrál Váš oblíbený tým
- Vypište datum a jméno poraženého týmu
- Doporučení: využít knihovny `BeautifulSoup` a `requests`

#### Příklad výstupu
```
13. 3. jsme porazili Vítkovice
14. 3. jsme porazili Vítkovice
17. 3. jsme porazili Vítkovice
18. 3. jsme porazili Vítkovice
31. 3. jsme porazili Plzeň
1. 4. jsme porazili Plzeň
4. 4. jsme porazili Plzeň
7. 4. jsme porazili Plzeň
15. 4. jsme porazili Třinec
18. 4. jsme porazili Třinec
19. 4. jsme porazili Třinec
22. 4. jsme porazili Třinec
```

### Úkol 4 - Validace textového souboru
- Připravte script pro validaci [tohoto](https://pastebin.com/tNmieVFn) CSV souboru ve formátu:
    - Jméno knihy; Jméno autora; ISBN; cena
- Validujte, že všechny hodnoty jsou zadané, že ISBN je ve správném formátu a že cena je kladné číslo
    - cena je zadána jako desetinné číslo oddělené tečkou nebo čárkou, doplněné o měnu (Kč nebo €)
- Pokud narazíte na nevalidní řádek, vypište číslo řádku a jaký nastal problém

#### Příklad výstupu
```
Invalid ISBN on line: 21
Missing title on line: 67
Invalid price on line: 90
Missing author on line: 149
Error! 3 column(s) on line 185!
Invalid price on line: 224
```

### Úkol 5 - Flappy Bird
- vytvořte klon hry [Flappy Bird](https://cs.wikipedia.org/wiki/Flappy_Bird)
- hra poběží v terminálu, případně můžete použít libovolnou knihovnu, např. [pygame](https://www.pygame.org/news.html)
- očekávaná doba vypracování je okolo __8 hodin__ (ověřit)
- po stránce grafiky se fantazii meze nekladou

#### Princip hry
- hráč se ujímá role ptáka, který musí proletět mezi překážkami
    - překážky jsou vertikálně orientované "trubky", mezi kterými je relativně úzká mezera
- herní plocha je grid, např. o 10 x 50 polích
    - pták zabírá např. 1x1 pole
    - překážky zabírají např. 4x1 pole (v x š)
- hráč stisknutím klávesy _mezerník_ vyvolá "mávnutí křídly" ptáka
    - pták začne konstantní rychlostí stoupat
    - po uplynutí nějaké doby, např. 2 s, začne pták konstantní rychlostí klesat
    - minimální doba mezi mávnutí křídly je např 0.5 s
- skóre odpovídá počtu sekund do kolize
- hru je možné ukončit stisknutím klávesy _Esc_

#### Nutné vyřešit
- vygenerování gridu před zahájením
- posouvání gridu / ptáka
- kolize ptáka s překážkou
- setrvání ptáka uvnitř gridu
- klesání / stoupání ptáka

#### Možná vylepšení
- fyzika letu (nekonstantní zrychlení)
- pickupy - např. jídlo, které může pták sbírat, zvyšují skóre
- různé stupně obtížnosti
- validace, že je možné překážkami proletět (tedy validace vygenerování)
