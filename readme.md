Skrypt pobiera piêæ ostatnich statusów w formacie json z serwisu blip.pl, zapisuje je do bazy w systemie Mongodb nastêpnie z wykorzystanie jêzyka JavaScript wykonywane jest MapReduce na tych danych i nastêpuje wyœwietlenie wyników.
Kolejnym etapem dzia³ania skryptu jest przeniesienie tych danych do Couchdb i znowu wykonanie  MapReduce dla tej bazy i wyœwietlenie wyników.
Wynikiem dzia³ania MapReduce dla obydwóch baz jest statystyka takich samych wyrazów znajduj¹cych siê w statusach.

Do poprawnego dzia³ania skryptu niezbêdny jest interpreter jêzyka Python w wersji 2.5-2.7 oraz najnowsze wersje modu³ów pymongo i couchdb.
Parametry do po³¹czenia z serwerem dla obydwóch systemów takie jak port i adres s¹ ustawione  do testowania lokalnie i mo¿na je zmieniæ na pocz¹tku kodu. 
Po nawi¹zaniu po³¹czenia z serwerami automatycznie tworzone s¹ odpowiednie bazy i kolekcje.
 


