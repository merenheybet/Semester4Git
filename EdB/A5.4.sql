-- 5.4.3
SELECT DISTINCT vn.Geburtsdatum FROM Versicherungsnehmer vn
WHERE EXISTS(SELECT * FROM Abteilung ab
			 WHERE ab.Ort = vn.Ort)
ORDER BY Geburtsdatum ASC;


-- 5.4.8
select vv.Vertragsnummer, vv.Abschlussdatum, vv.Art, mi.Name as Mi_Name, mi.Vorname as Mi_Vorname, fz.Kennzeichen, vn.Name as Vn_Name, vn.Vorname as Vn_Vorname
from versicherungsvertrag vv join versicherungsnehmer vn on vv.Versicherungsnehmer_ID = vn.ID 
join fahrzeug fz on vv.Fahrzeug_ID = fz.ID
join mitarbeiter mi on vv.Mitarbeiter_ID = mi.ID
where (	vn.Eigener_Kunde = 'J'
		and (fz.Kennzeichen like 'RE%' or vv.Art = 'VK') -- begins with
        or (vv.Art = 'TK' and vv.Abschlussdatum > 1990-12-31)
        or (vv.Art = 'HP' and vv.Abschlussdatum > 1985-12-31));

-- 5.4.15
SELECT lt.Name AS Leiter_Name, lt.Vorname AS Leiter_Vorname, lt.Abteilung_ID as Abteilung
FROM Mitarbeiter mt JOIN Mitarbeiter lt ON mt.Abteilung_ID = lt.Abteilung_ID
WHERE mt.Ist_Leiter = 'N' AND lt.Ist_Leiter = 'J';

-- 5.4.16
SELECT *
FROM Versicherungsnehmer v1 JOIN Versicherungsnehmer v2
	ON (v1.Name = v2.Name AND v1.Vorname = v2.Vorname 
		AND v1.ID < v2.ID AND v1.PLZ = v2.PLZ 
        AND v1.Strasse = v2.Strasse)
