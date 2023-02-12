# Vier-Gewinnt

## Wie wird gespielt?
### Ein neues Spiel starten
Um diese Version von Vier-Gewinnt zu spielen, muss zunächst das Repository heruntergeladen oder mit dem Befehl `git clone`
geklont werden.  
Es kann entweder in der Bash oder über einen Codeeditor gespielt werden. Voraussetzung ist, dass Python 3 
Skripte ausgeführt werden können. [Hier](https://www.python.org/downloads/) gibt es alle Informationen zur Installation von Python 3.  
Ein neues Spiel kann gestartet werden, indem die Datei projektVierGewinnt.py ausgeführt wird.
Mit dem Befehl `python3 projektVierGewinnt.py` wird das Spiel gestartet. Dazu muss der Ordner geöffnet sein, indem der Quellcode liegt.
### Spielen
Es können entweder zwei Spieler gegeneinander antreten oder es kann gegen einen Computergegner gespielt werden. Bei Spielstart
kann zwischen S für Multiplayer oder C für Singleplayer ausgewählt werden.  
Danach wird die Spielerin/der Spieler aufgefordert ihren/seinen Namen einzugeben und eine Farbe auszuwählen. Als Farbe
kann eine beliebige Zeichenfolge gewählt werden. Wir empfehlen entweder einen Großbuchstaben oder das Wort für die Farbe
in Kleinbuchstaben zu wählen.  
Nachdem alle Angaben gemacht wurden, wird eine beliebige Taste gedrückt und es kann losgehen.  
Wenn das Spiel vorzeitig abgebrochen werden soll, 0 als Spalte wählen.
Um einen Zug zu machen einfach eine Zahl zwischen 1 und 7 nach Aufforderung eingeben. Der Spielstein wird dann in der
ausgewählten Spalte in der tiefsten möglichen Zeile platziert.  
Die Spielerin/der Spieler die/der es geschafft hat als Erste/r vier Steine in nacheinander zu positionieren.
Dabei sind vier aufeinander folgende Steine in vertikaler, horizontaler oder diagonaler Richtung möglich.
## Über das Projekt
Das Projekt wurde im Zuge der Lehrveranstaltung Softwareentwicklungsmodelle erstellt.  
Zur Dokumentation wurden vor der Implementierung Meilensteine erstellt und währenddessen für alle Aufgaben Issues erstellt.
Anpassungen, die im Laufe der Umsetzung gemacht wurden, sind auch dort zu finden. Das Klassendiagramm ist in Issue #6 zu 
finden.