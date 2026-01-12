# Praktický projekt: Šifrovač zpráv (Message Encoder)

## Cíl projektu

Vytvořte konzolovou aplikaci pro šifrování a dešifrování textových zpráv. Program využívá objektově orientovaný přístup a implementuje specifický šifrovací algoritmus podle vašeho zadání.

**⚠️ Vaše konkrétní zadání (typ šifry a parametry) najdete v souboru `ASSIGNMENT.md`**

---

## Obecné požadavky

### 1. Třída `Message`

Vytvořte třídu reprezentující zprávu s následujícími atributy a metodami:

| Atribut/Metoda | Typ | Popis |
|----------------|-----|-------|
| `original_text` | str | Původní text zprávy |
| `processed_text` | str | Zašifrovaný/dešifrovaný text |
| `is_encoded` | bool | True pokud je zpráva zašifrovaná |
| `__init__(text)` | | Inicializace s původním textem |
| `__str__()` | str | Vrátí informace o zprávě |
| `get_stats()` | str | Vrátí statistiky (počet znaků, slov, nejčastější písmeno) |

### 2. Třída `Encoder`

Vytvořte třídu pro šifrování a dešifrování s metodami:

| Metoda | Popis |
|--------|-------|
| `__init__(parameter)` | Inicializace s parametrem šifry (posun, klíč, ...) |
| `encode(message)` | Zašifruje zprávu a vrátí objekt Message |
| `decode(message)` | Dešifruje zprávu a vrátí objekt Message |
| `_transform_char(char, reverse)` | Pomocná metoda pro transformaci jednoho znaku |

### 3. Hlavní program (`main.py`)

Interaktivní menu s volbami:
1. Zadat novou zprávu
2. Zašifrovat zprávu
3. Dešifrovat zprávu
4. Zobrazit statistiky
5. Zobrazit historii zpráv
6. Konec

---

## Pravidla šifrování

- Šifrujte **pouze písmena české abecedy** (a-z, A-Z, á-ž, Á-Ž)
- **Zachovejte velikost písmen** (malé → malé, velké → velké)
- **Mezery, čísla a speciální znaky zůstávají nezměněny**
- Diakritiku zpracujte podle vašeho zadání

---

## Ukázka interakce

```
========================================
      ŠIFROVAČ ZPRÁV (Message Encoder)
========================================
Typ šifry: Caesarova (posun: +3)
----------------------------------------
1. Zadat novou zprávu
2. Zašifrovat zprávu
3. Dešifrovat zprávu
4. Zobrazit statistiky
5. Historie zpráv
6. Konec
----------------------------------------
Volba: 1

Zadejte zprávu: Ahoj svete!

✓ Zpráva uložena.

----------------------------------------
Volba: 2

Původní text: Ahoj svete!
Zašifrovaný text: Dkrm vyhwh!

----------------------------------------
Volba: 4

=== STATISTIKY ===
Počet znaků: 11
Počet slov: 2
Nejčastější písmeno: e (2x)
```

---

## Struktura projektu

```
message-encoder/
├── README.md           # Tento soubor
├── ASSIGNMENT.md       # Vaše konkrétní zadání
├── message.py          # Třída Message
├── encoder.py          # Třída Encoder
├── main.py             # Hlavní program
└── tests/
    └── test_encoder.py # Automatické testy
```

---

## Hodnocení

| Kritérium | Body |
|-----------|------|
| Třída `Message` správně implementována | 10 |
| Třída `Encoder` – šifrování funguje správně | 15 |
| Třída `Encoder` – dešifrování funguje správně | 10 |
| Metoda `get_stats()` vrací správné statistiky | 10 |
| Funkční interaktivní menu | 10 |
| Zachování velikosti písmen a speciálních znaků | 5 |
| Čistý kód v angličtině a komentáře | 5 |
| **Bonus:** Historie zpráv s časovými razítky | 5 |
| **Bonus:** Ošetření chybových vstupů | 5 |
| **Celkem** | **75** |

---

## Požadavky na kód

- **Názvy tříd, metod a proměnných v angličtině**
- **Uživatelské texty (menu, hlášky) mohou být česky**
- Kód musí být spustitelný příkazem `python main.py`
- Automatické testy musí projít

---

## Nápověda

### Práce s ASCII hodnotami
```python
# Převod znaku na číslo a zpět
cislo = ord('A')  # 65
znak = chr(65)    # 'A'
```

### Cyklický posun v abecedě
```python
# Posun písmena o N pozic (pro základní latinku)
def shift_char(char, shift):
    if char.isalpha():
        base = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - base + shift) % 26 + base)
    return char
```

### Statistiky textu
```python
from collections import Counter
letters = [c.lower() for c in text if c.isalpha()]
most_common = Counter(letters).most_common(1)
```

---

## Termín odevzdání

Viz zadání v GitHub Classroom.

---

*Hodně štěstí!* 🔐
