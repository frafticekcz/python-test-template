# Návod pro učitele: GitHub Classroom setup

## Přehled projektu

Projekt **Šifrovač zpráv** obsahuje 4 varianty zadání s různými šifrovacími algoritmy:

| Varianta | Šifra | Parametr | Obtížnost |
|----------|-------|----------|-----------|
| A | Caesarova | posun +3 | ⭐ Nejsnazší |
| B | Caesarova | posun -5 | ⭐ Snazší |
| C | Atbaš | zrcadlová | ⭐⭐ Střední |
| D | Vigenerova | klíč "KOD" | ⭐⭐⭐ Nejtěžší |

---

## Rychlý start (3 kroky)

### 1. Vytvořte template repozitář

```bash
# Klonujte projekt
git clone <tento-repozitar> message-encoder-template

# Odstraňte učitelské soubory
cd message-encoder-template
rm -rf solutions/ teacher_tools/

# Inicializujte Git
git init
git add .
git commit -m "Initial commit"
```

### 2. Nahrajte na GitHub jako template

1. Vytvořte nový repozitář na GitHubu
2. Zaškrtněte "Template repository"
3. Pushněte kód

### 3. Vytvořte assignment v GitHub Classroom

1. Jděte do GitHub Classroom
2. Vytvořte nový assignment
3. Vyberte váš template repozitář
4. Povolte autograding (importuje se z `.github/classroom/`)

---

## Ruční přiřazení variant

Pokud chcete ručně přiřadit varianty studentům:

### Možnost A: Jednotná varianta pro všechny

Před vytvořením template zkopírujte příslušné soubory:

```bash
# Pro variantu A (Caesar +3):
cp variants/ASSIGNMENT_A.md ASSIGNMENT.md
cp tests/configs/config_A.json tests/config.json
```

### Možnost B: Různé varianty pro studenty

1. Vytvořte 4 různé template repozitáře (pro každou variantu)
2. Vytvořte 4 různé assignments v GitHub Classroom
3. Přiřaďte studenty do správných assignments

### Možnost C: Automatické přiřazení pomocí skriptu

```bash
# Připravte seznam studentů (students.csv):
# github_username,full_name
# novakj,Jan Novák
# svobodam,Marie Svobodová

# Spusťte skript:
cd teacher_tools
python assign_variants.py students.csv

# Výstup:
# - student_assignments.md (mapování studentů na varianty)
# - .github/classroom_config.json (konfigurace pro GitHub Actions)
```

---

## Struktura souborů

```
message-encoder/
├── README.md              # Obecné zadání (pro všechny studenty)
├── ASSIGNMENT.md          # ← Specifické zadání (kopíruje se z variants/)
├── message.py             # Kostra třídy Message
├── encoder.py             # Kostra třídy Encoder
├── main.py                # Kostra hlavního programu
│
├── variants/              # ← ODSTRAŇTE před distribucí studentům
│   ├── ASSIGNMENT_A.md    # Caesar +3
│   ├── ASSIGNMENT_B.md    # Caesar -5
│   ├── ASSIGNMENT_C.md    # Atbaš
│   └── ASSIGNMENT_D.md    # Vigenère
│
├── tests/
│   ├── test_encoder.py    # Automatické testy
│   ├── config.json        # ← Konfigurace testů (kopíruje se z configs/)
│   └── configs/
│       ├── config_A.json
│       ├── config_B.json
│       ├── config_C.json
│       └── config_D.json
│
├── solutions/             # ← ODSTRAŇTE před distribucí studentům
│   └── solution_A.py      # Vzorové řešení varianty A
│
├── teacher_tools/         # ← ODSTRAŇTE před distribucí studentům
│   └── assign_variants.py # Skript pro přiřazení variant
│
└── .github/
    ├── classroom/
    │   └── autograding.json  # Konfigurace hodnocení
    └── workflows/
        └── classroom.yml     # GitHub Actions workflow
```

---

## Hodnocení

Automatické testy přidělují body takto:

| Test | Body |
|------|------|
| Message - vytvoření | 3 |
| Message - __str__ | 2 |
| Message - statistiky (znaky) | 3 |
| Message - statistiky (slova) | 3 |
| Message - statistiky (písmeno) | 4 |
| Encoder - odstranění diakritiky | 5 |
| Encoder - základní šifrování | 5 |
| Encoder - malá písmena | 3 |
| Encoder - smíšený text | 5 |
| Encoder - text s diakritikou | 5 |
| Encoder - dešifrování | 10 |
| Encoder - zachování čísel | 2 |
| Encoder - zachování interpunkce | 3 |
| Encoder - symetrie | 7 |
| **Celkem** | **60** |

Zbývajících 15 bodů (do 75) lze přidělit ručně za:
- Funkční menu (10 b)
- Čistý kód (5 b)

---

## Časový odhad

Pro běžného studenta střední školy:
- Třída Message: 30-40 minut
- Třída Encoder: 45-60 minut  
- Hlavní program: 20-30 minut
- **Celkem: 1.5-2 hodiny**

---

## Tipy pro výuku

1. **Před zadáním** proberte:
   - Základy OOP (třídy, metody, atributy)
   - Práci s řetězci a ASCII hodnotami
   - Modulo operátor pro cyklické posuny

2. **Během práce**:
   - Nechte studenty nejprve implementovat Message
   - Encoder nechte až po otestování Message
   - Menu nakonec

3. **Konzultace**:
   - Připravte si "debug" verzi s print statementy
   - Ukazujte postupně na ASCII tabulce

---

## Kontakt

V případě problémů vytvořte issue v repozitáři nebo kontaktujte autora.
