# Decorators

## Einordnung
Decorators sind ein strukturelles Design Pattern. Ein Design Pattern in der Softwareentwicklung
ist ein methodischer Ansatz zur Lösung von wiederkehrenden Softwareproblemen.   
Im Gegensatz zu einem Algorithmus beschreiben sie Problemlösungen eine Abstraktionsebene darüber.
Design Patterns beschreiben nur einen allgemeinen Rahmen und Methodik, während Algorithmen 
die Problemlösung Schritt für Schritt beschreiben.  
Strukturelle Design Patterns sind 'Frameworks', um Klassen und Objekte zu organisieren. 
Bei größeren Strukturen soll möglichst wenig Flexibilität verloren gehen.
## Problem
Eine Klassenmethode muss um eine neue Funktionalität erweitert werden, die ursprünglich
nicht vorgesehen war. Um die neuen Anforderungen umzusetzten können mehrere Subklassen nötig sein.
Für jede neue Erweiterung muss eine neue Subklasse erstellt werden.
Einzelne Subklassen stellen eine Kombination anderer Subklassen dar.  
Ein Beispiel für eine mögliche Klassenexplosion ist, wenn verschiedene Heißgetränke für ein Kassasystem angelegt werden sollen.
Es gibt drei Grundgetränke, Tee, Kaffee und Kakao mit vielen verschiedenen optionalen Zutaten, Milch, Hafermilch, 
Sojamilch, Pumpkinsirup und Karamellsirup. Alleine alle Kombinationen mit nur einer optionalen Zutat würden schon 15 zusätzliche 
Klassen ergeben.
## Lösung
Gelöst wird das Problem mit Decorators. Die optionalen Zutaten werden so implementiert, dass sie
wie eine Hülle um das Grundgetränk gelegt werden können. Das Grundgetränk und die optionalen Zutaten
leiten sich von derselben Basisklasse (Getränk) ab. Die Decorator sind zusätzlich über eine sogenannte
Aggregation mit der Basisklasse verbunden. Zusätzlich ist es üblich noch eine abstrakte Basisklasse zwischen
Getränk und den optionalen Zutaten einzufügen. Der Decorator bekommt eine Instanz der Klasse Getränk mit übergeben
und kann der betreffenden Instanz von Getränk weitere Funktionalitäten geben.  
Pseudocode: `kunden1_trinkt = Kramellsirup(Sojamilch(Tee))`  
In Python können auch Funktionen dekoriert werden, da Funktionen auch Objekte sind.