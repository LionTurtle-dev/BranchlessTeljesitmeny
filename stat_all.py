import json
import time as t
from test_all import elag_all, tern_all, elnel_all #100`000-szer fut le egy algoritmus


a: int = 400
b: int = 50
c: int = 0
bl = a > b
i = int(a > b)


def tolt_all(a: int, b: int, ind: int) -> list[tuple[float, str]]:
    elagazassal = elag_all(a, b, ind)
    ternaryval = tern_all(a, b, ind)
    elagazasnelkul = elnel_all(a, b, ind)

    e: tuple[float, str] = (float(f"{elagazassal:.3f}"), "Elágazással")
    t: tuple[float, str] = (float(f"{ternaryval:.3f}"), "Ternary-val")
    n: tuple[float, str] = (float(f"{elagazasnelkul:.3f}"), "Elágazás nélkül")

    v: list[tuple[float, str]] = [e, t, n]
    v.sort(key=lambda x: x[0])
    return v

db = []
for i in range(100):
    m: int = i * (i % 10 == 0)
    eredmeny = {
        "Elágazással": 0.0,
        "Ternary-val": 0.0,
        "Elágazás nélkül": 0.0
    }
    t.sleep(25 * (i % 25 == 0))
    ered = tolt_all(a, b, i)
    for r in ered:
        eredmeny[r[1]] = r[0]
    db.append(eredmeny) # type: ignore


print("Kész!")

stat:dict[str, list[dict[str, float]]] = {"Futasi eredmenyek": db}

with open('eredmenyek(osszes).json', 'w', encoding='utf-8') as f:
    json.dump(stat, f, indent=4)
