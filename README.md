# Tekstualna avantura

Mala igra u terminalu napisana u Python-u. Istražuješ kuću, skupljaš predmete
i tražiš blago u zaključanom podrumu.

## Pokretanje

```
python avantura.py
```

## Komande

| Komanda | Šta radi |
|---|---|
| `sever`, `jug`, `istok`, `zapad`, `gore`, `dole` | kretanje |
| `uzmi <predmet>` | uzima predmet iz sobe |
| `inventar` | prikazuje šta nosiš |
| `kraj` | izlaz iz igre |

## Kako je napravljeno

- Mapa je rečnik soba, a svaka soba je rečnik (ime, opis, izlazi, predmeti).
- Zaključavanje je podatak (`"treba": "ključ"`), pa se nova zaključana soba
  dodaje bez menjanja koda.
- Inventar je skup (`set`).

Projekat iz prvog meseca učenja Python-a.