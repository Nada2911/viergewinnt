 # Facade
### Beschreibung:
Das Fassaden-Muster ist ein Struktur-Design-Muster, welches eine vereinfachte 
Schnittstelle zu komplexen Klassensätzen,
wie Bibliotheken oder Rahmen bietet.

### Problem:
Beim Arbeiten mit einer breiten Palette von Objekten einer anspruchsvollen 
Bibliothek oder eines Rahmens ist es notwendig, alle Objekte zu initialisieren, 
Abhängigkeiten zu verfolgen und Methoden in der richtigen Reihenfolge auszuführen. 
Dies kann dazu führen, dass die Geschäftslogik der Klassen eng an die Implementierungsdetails 
von Drittanbieterklassen gebunden ist und somit schwer zu verstehen und zu warten ist.

### Lösung:
Eine Fassade ist eine Klasse, die eine vereinfachte Schnittstelle für ein komplexes Unter-System bereitstellt,
indem nur die Funktionen bereitgestellt werden, die für den Kunden wichtig sind. 
Dies ist praktisch, wenn man eine App mit einer komplexen Bibliothek integrieren muss, 
aber nur einen kleinen Teil ihrer Funktionalität benötigt. 
Ein Beispiel dafür ist eine App, die Videos hochlädt und dafür eine Video-Konvertierungsbibliothek nutzen kann. 
Eine Fassade, die nur die Methode encode(filename, format) bereitstellt, kann erstellt werden, 
um das Integrieren zu erleichtern. 