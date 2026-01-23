**Programok Elágazásmentesen**
Ez a project leteszteli, hogy az elágazásmentes programkód tényleg gyorsabb e, mint az egyszerű if-else szerkezet vagy a ternary operátor.

*Elágazásmentesség*
Pythonban háromféleképpen alkalmazhatunk kétirányú elágazásokat. 


***A sima if-else szerkezettel:***

*/  a = 100                     /*
*/  b = 50                      /*
*/  c = 0                       /*
*/  if a > b:                   /*
*/     c = a                    /*
/*  else:                       /*
/*     c = b                    /*


***Az úgynevezett Ternary utasítással:***

*/  a = 100                     /*
*/  b = 50                      /*
*/  c = a if (a > b) else b     /*

Ennél az utasításnál azt mondjuk, hogy *a* változó vegye fel az *érték_1* értékét, ha az állítás igaz, különben *a* az *érték_2* értékét veszi fel.


***Elágazásmentes parancs***

*/  a = 100                     /*
*/  b = 50                      /*
*/  c = a * (a>b) + b * (a<b)   /*
*/  print(c)                    /*
*/  output: 100                 /*



*Alapfeltevés*
Az alapfeltevés, hogy az elágazásmentes parancs gyorsabban végrehajtódik, mint a másik kettő. Ezt az állítást megerősítendő, vagy megcáfolandó. A vizsgálatot 3 féleképpen is elvégeztem. Az első esetben értékadó utasítások teljesítményét mértem, a második esetben print utasításokat vizsgáltam, a harmadik esetben pedig azt néztem meg, hogy milyen futási idő, ha mindkettő előbbi eset egyszerre fut le.

*A mérés technikája*
Az alapötlet, hogy a futásiidőt mérem milliszekundumban mérem. Tekintve, hogy a jupyter notebook csak tized másodperces pontossággal méri a futási időt, komolyabb tesztprogramot kellett írnom.

A méréshez a time modult használtam, hogy a főprogram futása előtt és utána rözítsem az aktuális időt. Ehhez létrehoztam a */start/* és a */stop/* változókat, melyeknek különbsége adja majd meg a futási idő értékét. A time modul */perf_counter()/* metódusa egy tizedes törttel tér vissza, melynek egyes helyiértéke a másodpercet mutatja. Íly módon lehetségessé vált az idő mérése százezred másodperc pontossággal.



*A program felépítése*
Egy mérés nem mérés. Éppen ezért mindhárom esetet 100-szor mértem meg. Minden mérésnél az alap programot 100 ezerszer futtattam le, hogy látható eredményt kapjak. Egy mérés során rögzíti a program, hogy 100 ezerszeres futás mennyi időbe telik.

Minden futás után a kapott eredményt eltárolom egy tuple változóba, ami tartalmazza a mért százezredmásodpercek értékét és a mért utasítás-formát("Elágazással", "Ternary-val", "Elágazás nélkül").

A három utasítás-formához tartozó tuple változót egy listába összefűzöm és a float értékek szerint növekvő sorrendbe rendezem. (Később hasznos lesz, ha külön a legjobb eredményeket is el akarom tárolni.)

A főprogramban a kapott lista értékeit átrendeztem egy szótárba, amit hozzáfűztem egy listához. Ezt a műveletet 100-szor hajttattam végre a programmal.

Az eredményt egy jupyter notebookban értékeltem ki. jelenleg egy átlagoló függvényt tartalmaz, amivel megvizsgáltam a három utasítás-forma átlag idejét.


*A kapott eredmények*
A mérések eredményeit egy-egy jSON file, az átlagokat mindhárom esettel a stat.txt file tartalmazza.
**FONTOS**
A PROGRAM EGY ASUS TUF GAMING A15 LAPTOPON FUTOTT, UBUNTU LTS OPERÁCIÓS RENDSZER ALATT. A MÉRÉS NEM REPREZENTATÍV, DE BÁRKI FUTTATHATJA AZ OTTHONI GÉPÉN.


*Konklúzió*
A mérés során arra a megállapításra jutottam, hogy python nyelven a kiinduló állítás, miszerint az elágazásmentes utasítások hamarabb lefutnak, mint az if-else szerkezet, nem állja meg a helyét. Az általam mért eredményeket lásd a txt file-ban és a jSON file-okban.
