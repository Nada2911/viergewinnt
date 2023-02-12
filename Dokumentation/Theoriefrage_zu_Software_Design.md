# Theoriefrage zu Software Design

Sie beginnen als Entwickler*in in einem neuen Unternehmen und bekommen die Verantwortung für
ein Modul. Das Modul ist über eine lange Zeit hinweg gewachsen und besteht nur aus sehr wenigen
Klassen. Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder länger, und sie sind auch eher spärlich dokumentiert. Was für Nachteile ergeben sich für Sie durch
diesen Code? Welche grundlegenden Software Design Prinzipien werden evtl. nicht eingehalten?

## Antwort
Je länger eine Methode ist und je mehr Funktionen sie erfüllt, desto schwieriger wird es den Code zu verstehen.
Wenn es zudem wenig oder keine Dokumentation gibt, ist es schwer nachvollziehbar warum die Funktionen auf eine bestimmte Art und
Weise umgesetzt wurden. Auch Erweiterungen und Anpassungen im Falle eines Fehlers werden erschwert.  
Der Hinweis auf mehrere hundert Zeilen pro Methode legt nahe, dass das Single-Responsibility-Prinzip nicht eingehalten wurde.
Single-Responsibility heißt, dass jede Funktion genau eine bestimmte Aufgabe erfüllen sollte. Auch das Open-Closed Prinzip
könnte unzureichend eingehalten worden sein. Sehr umfangreiche Methoden die verschiedene Aufgaben erledigen könnten sich 
auch als schwer erweiterbar herausstellen, ohne dabei bestehenden Code anzugreifen.