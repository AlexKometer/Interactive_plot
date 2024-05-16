# Leistungsanalyse-App mit Streamlit

Diese Streamlit-App bietet eine einfache Möglichkeit zur Analyse von Leistungstestdaten. Sie können Daten aus einer CSV-Datei laden, die Leistung über die Zeit plotten, die Aktivität in verschiedenen Herzfrequenz-Zonen anzeigen und die durchschnittliche Leistung in diesen Zonen berechnen.

## Anforderungen

Um die App auszuführen, benötigen Sie Python und die folgenden Bibliotheken:

- Pandas
- Matplotlib
- Streamlit

Sie können diese Bibliotheken mit `pip` installieren, indem Sie den folgenden Befehl ausführen:
  pip install -r requirements.txt 

## Funktionalitäten

Die App bietet die folgenden Funktionen:

- Laden von Leistungstestdaten aus einer CSV-Datei.
- Anzeige des Mittelwerts und des Maximalwerts der Leistung.
- Interaktiver Plot von Leistung und Herzfrequenz über die Zeit.  In welchem es möglich ist, das EKG über die gesamter Laufzeit zu betrachten.
- Einteilung der Aktivität in fünf Zonen basierend auf der eingegebenen maximalen Herzfrequenz.
- Anzeige der Zeit, die in jeder Herzfrequenzzone verbracht wurde.
- Berechnung der durchschnittlichen Leistung in jeder Zone.
