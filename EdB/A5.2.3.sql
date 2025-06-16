INSERT INTO Versicherungsgesellschaft (Bezeichnung, Ort)
VALUES ('AH Versicherung', 'Musterstadt');

-- LAST_INSERT-ID() greift zuletzt erstellte ID zu.
-- Der Kunde mit der neuen erstellten Versicherungsgesellschaft
INSERT INTO Versicherungsnehmer (Name, Vorname, Geburtsdatum, Fuehrerschein, Ort, PLZ, Strasse, Hausnummer, Eigener_Kunde, Versicherungsgesellschaft_ID, Geschlecht)
VALUES ('Fremdmann', 'Erster', '2000-01-01', '2018-01-01', 'Musterstadt', '90000', 'Hauptstraße', '8', 'N', LAST_INSERT_ID(), 'M');

INSERT INTO Versicherungsnehmer (Name, Vorname, Geburtsdatum, Fuehrerschein, Ort, PLZ, Strasse, Hausnummer, Eigener_Kunde, Versicherungsgesellschaft_ID, Geschlecht)
VALUES ('Fremdmann', 'Zweiter', '1999-12-31', '2018-01-02', 'Frankfurt a.M.', '60314', 'Musterstraße', '12', 'N', 1, 'M');

INSERT INTO Versicherungsnehmer (Name, Vorname, Geburtsdatum, Fuehrerschein, Ort, PLZ, Strasse, Hausnummer, Eigener_Kunde,  Geschlecht)
VALUES ('Kraeutle', 'Mathe', '1976-03-12', '2000-01-01', 'Hamburg', '20144', 'Haferstraße', '3', 'J', 'M');

-- Fahrzeuge
-- Erster Fremdmann
INSERT INTO Fahrzeug (Kennzeichen, Farbe, Fahrzeugtyp_ID)
VALUES ('XX-XY 321', 'schwarz', 13);

-- Zweiter Fremdmann
INSERT INTO Fahrzeug (Kennzeichen, Farbe, Fahrzeugtyp_ID)
VALUES ('F-AB 654', 'rot', 2);

-- Mathe Kraeutle
INSERT INTO Fahrzeug (Kennzeichen, Farbe, Fahrzeugtyp_ID)
VALUES ('HH-CD 987', 'schwarz', 23);

-- Schadensfall
INSERT INTO Schadensfall (Datum, Ort, Beschreibung, Schadenshoehe, Verletzte, Mitarbeiter_ID)
VALUES ('2025-06-04', 'Erlangen, Paul Gossen Str. 12', 'Auffahrunfall mit drei Beteiligten', 5000.00, 'N', 1);

-- Zuordnung
INSERT INTO Zuordnung_SF_FZ (Schadensfall_ID, Fahrzeug_ID, Schadenshoehe, Schuldanteil)
VALUES  (LAST_INSERT_ID(), 26, 2000.00, 50),
		(LAST_INSERT_ID(), 27, 1500.00, 30),
        (LAST_INSERT_ID(), 28, 1500.00, 20);

-- Versicherungsverträge


