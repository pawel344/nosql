Skrypt pobiera pięć ostatnich statusów w formacie json z serwisu blip.pl, zapisuje je do bazy w systemie Mongodb następnie z wykorzystanie języka JavaScript wykonywane jest MapReduce na tych danych i następuje wyświetlenie wyników.
Kolejnym etapem działania skryptu jest przeniesienie tych danych do Couchdb i znowu wykonanie  MapReduce dla tej bazy i wyświetlenie wyników.
Wynikiem działania MapReduce dla obydwóch baz jest statystyka takich samych wyrazów znajdujących się w statusach.

Do poprawnego działania skryptu niezbędny jest interpreter języka Python w wersji 2.6-2.7 oraz najnowsze wersje modułów pymongo i couchdb.
Wszystkie niezbędne moduły znajdują się w repozytorium, więc w przypadku ich braku
nie trzeba ich doinstalowywać, wystarczy sklonować całe repozytorium.
Skrypt uruchamia się poleceniem:

'
python nosql.py
'
Po nawiązaniu połączenia z serwerami automatycznie tworzone są odpowiednie bazy i kolekcje.
Parametry do połączenia z serwerem dla obydwóch systemów takie jak port i adres są ustawione  do testowania lokalnie i można je zmienić na początku kodu. 



