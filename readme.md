Skrypt pobiera pi�� ostatnich status�w w formacie json z serwisu blip.pl, zapisuje je do bazy w systemie Mongodb nast�pnie z wykorzystanie j�zyka JavaScript wykonywane jest MapReduce na tych danych i nast�puje wy�wietlenie wynik�w.
Kolejnym etapem dzia�ania skryptu jest przeniesienie tych danych do Couchdb i znowu wykonanie  MapReduce dla tej bazy i wy�wietlenie wynik�w.
Wynikiem dzia�ania MapReduce dla obydw�ch baz jest statystyka takich samych wyraz�w znajduj�cych si� w statusach.

Do poprawnego dzia�ania skryptu niezb�dny jest interpreter j�zyka Python w wersji 2.5-2.7 oraz najnowsze wersje modu��w pymongo i couchdb.
Parametry do po��czenia z serwerem dla obydw�ch system�w takie jak port i adres s� ustawione  do testowania lokalnie i mo�na je zmieni� na pocz�tku kodu. 
Po nawi�zaniu po��czenia z serwerami automatycznie tworzone s� odpowiednie bazy i kolekcje.
 


