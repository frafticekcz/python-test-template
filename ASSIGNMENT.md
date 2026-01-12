# Vaše individuální zadání

## Typ šifry: Caesarova šifra

### Parametr: posun +3

---

## Popis algoritmu

**Caesarova šifra** je substituční šifra, kde každé písmeno v textu nahradíte písmenem, které je v abecedě o určitý počet pozic dále.

### Váš posun: **+3** (doprava)

| Původní | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Šifrované | D | E | F | G | H | I | J | K | L | M | N | O | P |

| Původní | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Šifrované | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

### Příklady

| Operace | Vstup | Výstup |
|---------|-------|--------|
| Šifrování | `AHOJ` | `DKRM` |
| Šifrování | `Python 3.12` | `Sbwkrq 3.12` |
| Dešifrování | `DKRM` | `AHOJ` |

---

## Speciální pravidla pro vaše zadání

1. **Diakritika**: Před šifrováním převeďte znaky s diakritikou na základní tvar (á→a, č→c, ř→r, atd.)
2. **Velikost písmen**: Zachovejte původní velikost
3. **Ostatní znaky**: Mezery, čísla a interpunkce zůstávají beze změny

### Převod diakritiky
```python
DIACRITICS_MAP = {
    'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i',
    'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u',
    'ů': 'u', 'ý': 'y', 'ž': 'z'
}
```

---

## Testovací případy

Vaše implementace musí správně zpracovat tyto vstupy:

```python
# Test 1: Základní šifrování
assert encoder.encode("AHOJ").processed_text == "DKRM"

# Test 2: Malá písmena
assert encoder.encode("ahoj").processed_text == "dkrm"

# Test 3: Smíšený text
assert encoder.encode("Ahoj Svete!").processed_text == "Dkrm Vyhwh!"

# Test 4: S diakritikou
assert encoder.encode("Příliš").processed_text == "Sulolv"

# Test 5: Dešifrování
assert encoder.decode("Dkrm").processed_text == "AHOJ"
```

---

## Inicializace vaší třídy Encoder

```python
# Váš Encoder se inicializuje takto:
encoder = Encoder(shift=3)
```

---

*Nezapomeňte, že váš kód musí projít automatickými testy!*
