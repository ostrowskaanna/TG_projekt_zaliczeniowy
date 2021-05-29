# TEORIA GRAFÓW - projekt zaliczeniowy 

**Część programistyczna:**

-> w projekcie zostały umieszczony plik input.json, z którego program wczytuje graf w następujący sposób:
mamy podaną listę list czytaną jak macierz, czyli kolejne wiersze to kolejne wierzchołki, a każda z mniejszych list ma tyle elementów ile jest wierzchołków i wartość stojąca na danej pozycji odpowiada wadze krawędzi łączącej wierzchołek o indeksie wiersza z wierzchołkiem o indeksie "kolumny"

-> program pyta użytkownika, z którego wierzchołka ma zacząć

-> program zwraca tabelę algorytmu w postaci macierzy (-1 w ostatnim wierszu oznacza brak poprzednika czyli nie możemy dojść do tego wierzchołka)

-> program wypisuje również ścieżki z wybranego wierzchołka do wszystkich pozostałych 
