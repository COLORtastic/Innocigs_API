# InnoCigs Dropship-API Dokumentation

**Vapor Innovations**  
**InnoCigs**

**Revision:** 28.04.2022

---

## Inhaltsverzeichnis

|API-Authentifizierung|2|
|---|---|
|Test-Modus onTheFly|3|
|REST-Api:| |
|Bei Verwendung der Rest-Api wird der Parameter modus mit dem Wert test im Header mitgegeben.|3|
|Bestand eines Artikels abfragen|4|
|Alle Bestände abfragen|6|
|Preis eines Artikels abfragen|8|
|Alle Preise abfragen|10|
|Dropship Auftrag übermitteln|12|
|Bestellung ohne Dropship|18|
|Trackingdaten abfragen (TAG)|22|
|Trackingdaten abfrage (Order)|26|
|Lieferscheine abfragen|29|
|Ausstehende Artikel abfragen|33|
|Produkte und EANS abfragen|35|
|Erweiterte Produktabfrage|39|
|Produktabfrage Master Produkte (Nur REST API)|43|
|Fehlermeldungen:|45|
|Kontakt|48|

---

## API-Authentifizierung

### API Aufrufe über URL-Parameter (alte Methode im weiteren XML-Api genannt)

Generell gibt es zwei Wege die API aufzurufen, zum einen gibt es die Methode, die API über URL-Parameter anzusteuern.

Für die Authentifizierung müssen bei jedem API-Aufruf Kundennummer und API-Passwort im Request entweder als GET oder Post-Parameter mitgegeben werden.

https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=quantity_all

Die bisherige URL “https://www.innocigs.com/xmlapi/api.php” kann weiterhin verwendet werden, es wird jedoch empfohlen die apiv2.php anzusteuern.

HINWEIS: Die neue apiv2.php liefert einen verbesserten Kategoriebaum zurück und gibt zudem bei Preisen erweiterte Informationen zu Staffelpreisen zurück.

### Parameter:

|cid|Wird durch Innocigs Technik mitgeteilt|
|---|---|
|auth|Wird durch Innocigs Technik mitgeteilt|

### API Aufrufe über die REST-Api:

Diese neue Methode wird angesteuert indem die Kundenummer und das Passwort über den Header Parameter Auth mitgegeben werden, die Befehle selber werden in der URL angegeben.

Der Auth Parameter setzt sich dabei zusammen aus Kundennummer und Passwort getrennt durch einen Doppelpunkt: cid:passwort

Die Antwort der REST-Api erfolgt im Gegensatz zur XML-Api nicht als XML sondern im JSON-Format.

Die generelle Struktur bei Aufrufen ergibt sich wie folgt:

```
https://www.innocigs.com/restapi/BEFEHL
```

---

## Test-Modus onTheFly

Um nach Freischaltung etwas zu testen kann als Parameter modus=test übergeben werden. So wird dann keine Bestellung oder Dropship ausgelöst.

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=quantity_all&modus=test
```

### Parameter:

|modus|Wert|
|---|---|
|test|Testmodus aktiv|

### REST-Api:

Bei Verwendung der Rest-Api wird der Parameter modus mit dem Wert test im Header mitgegeben.


---

## Bestand eines Artikels abfragen

### Parameter:

- **cid:** Kundennummer
- **auth:** API-Passwort
- **model:** Artikelnummer des Artikels

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=quantity&model=[ARTIKELNUMMER]
```

##### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
<QUANTITIES>
<PRODUCT>
<PRODUCTS_MODEL>IC10000AIO-10</PRODUCTS_MODEL>
<QUANTITY>155</QUANTITY>
</PRODUCT>
</QUANTITIES>
</INNOCIGS_API_RESPONSE>
```

##### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/quantity/[ARTIKELNUMMER]
```

### Rückgabe REST-Api:

```json
{
  "QUANTITIES": {
    "PRODUCT": [
      {
        "PRODUCTS_MODEL": "12M100L10-BG-0",
        "QUANTITY": 220,
        "SHIPPING_STATUS": "Sofort lieferbar"
      }
    ]
  }
}
```


---

##### Felder:

| Feld | Beschreibung |
|---|---|
| **PRODUCT** | Container für Artikel |
| **PRODUCTS_MODEL** | Artikelnummer |
| **QUANTITY** | Bestand des Artikels |
| **SHIPPING_STATUS** | Lieferstatus |



---

## Alle Bestände abfragen

### Parameter:

| Parameter | Beschreibung |
|---|---|
| **cid** | Kundennummer |
| **auth** | API-Passwort |

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=quantity_all
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <QUANTITIES>
    <PRODUCT>
      <PRODUCTS_MODEL>12M100L10-HB-0</PRODUCTS_MODEL>
      <QUANTITY>44</QUANTITY>
      <SHIPPING_STATUS>Sofort lieferbar</SHIPPING_STATUS>
    </PRODUCT>
    <PRODUCT>
      <PRODUCTS_MODEL>12M100L10-HB-3</PRODUCTS_MODEL>
      <QUANTITY>0</QUANTITY>
      <SHIPPING_STATUS>Sofort lieferbar</SHIPPING_STATUS>
    </PRODUCT>
    <PRODUCT>
      <PRODUCTS_MODEL>12M100L10-HB-6</PRODUCTS_MODEL>
      <QUANTITY>66</QUANTITY>
      <SHIPPING_STATUS>Sofort lieferbar</SHIPPING_STATUS>
    </PRODUCT>
    <PRODUCT>
      <PRODUCTS_MODEL>A-2216-001</PRODUCTS_MODEL>
      <QUANTITY>131</QUANTITY>
      <SHIPPING_STATUS>Sofort lieferbar</SHIPPING_STATUS>
    </PRODUCT>
    ….
  </QUANTITIES>
</INNOCIGS_API_RESPONSE>
```

---

### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/quantity_all
```

### Rückgabe REST-Api:

```json
{
  "QUANTITIES": {
    "PRODUCT": [
      {
        "PRODUCTS_MODEL": "12M100L10-BG-0",
        "QUANTITY": 220,
        "SHIPPING_STATUS": "Sofort lieferbar"
      },
      {
        "PRODUCTS_MODEL": "12M100L10-BN-20",
        "QUANTITY": 114,
        "SHIPPING_STATUS": "Sofort lieferbar"
      },
      {
        "PRODUCTS_MODEL": "12M100L10-BN-20-H",
        "QUANTITY": 11,
        "SHIPPING_STATUS": "Sofort lieferbar"
      },
      …
    ]
  }
}
```

### Felder:

| Feld | Beschreibung |
|---|---|
| **PRODUCT** | Container für Artikel |
| **PRODUCTS_MODEL** | Artikelnummer |
| **QUANTITY** | Bestand des Artikels |
| **SHIPPING_STATUS** | Lieferstatus |



---
## Preis eines Artikels abfragen

### Parameter:

- **cid:** Kundennummer
- **auth:** API-Passwort
- **model:** Artikelnummer des Artikels

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=price&model=[ARTIKELNUMMER]
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <PRICES>
    <PRODUCT>
      <PRODUCTS_MODEL>ACK100L10-AM-12-H</PRODUCTS_MODEL>
      <PRODUCTS_PRICE>23,63</PRODUCTS_PRICE>
      <PRODUCTS_PRICE_RECOMMENDED>49,58</PRODUCTS_PRICE_RECOMMENDED>
      <GRADUATED_PRICES>
        <GRADUATED_PRICE>
          <QUANTITY>10</QUANTITY>
          <PRODUCTS_PRICE>22,50</PRODUCTS_PRICE>
        </GRADUATED_PRICE>
        <GRADUATED_PRICE>
          <QUANTITY>20</QUANTITY>
          <PRODUCTS_PRICE>21,50</PRODUCTS_PRICE>
        </GRADUATED_PRICE>
      </GRADUATED_PRICES>
      <OTHER_UNITS>
      </OTHER_UNITS>
    </PRODUCT>
  </PRICES>
</INNOCIGS_API_RESPONSE>
```



---

### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/price/[ARTIKELNUMMER]
```

### Rückgabe REST-Api:

```json
{
  "PRICES": {
    "PRODUCT": [
      {
        "PRODUCTS_MODEL": "12M100L10-BG-0",
        "PRODUCTS_PRICE": "7,52",
        "PRODUCTS_PRICE_RECOMMENDED": "16,95",
        "GRADUATED_PRICES": {
          "GRADUATED_PRICE": [
            {
              "QUANTITY": 5,
              "PRODUCTS_PRICE": "6.998400"
            }
          ]
        },
        "OTHER_UNITS": {
          "OTHER_UNIT": [
            {
              "MODEL": "12M100L10-BG-0-H",
              "PACKUNG": "10",
              "PRODUCTS_PRICE": "70.000000",
              "PRODUCTS_PRICE_SINGLE_UNIT": "0.700000"
            }
          ]
        }
      }
    ]
  }
}
```

### Felder:

| Feld | Beschreibung |
|---|---|
| **PRODUCT** | Container für Artikel |
| **PRODUCTS_MODEL** | Artikelnummer |
| **PRODUCTS_PRICE** | Preis |
| **PRODUCTS_PRICE_RECOMMENDED** | UVP |
| **GRADUATED_PRICES** | Staffelpreise welche ab der jeweils angegebenen Menge (QUANTITY) gelten (Rückgabe ab apiv2 und in der REST-Api) |
| **OTHER_UNITS** | Größere Verpackungseinheiten mit Preisinformationen zu Gesamtpreis und Einzelpreis |



---
## Alle Preise abfragen

### Parameter:

- **cid:** Kundennummer
- **auth:** API-Passwort

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=prices
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <PRICES>
    <PRODUCT>
      <PRODUCTS_MODEL>ACK100L10-AM-3</PRODUCTS_MODEL>
      <PRODUCTS_PRICE>2,36</PRODUCTS_PRICE>
      <PRODUCTS_PRICE_RECOMMENDED>4,96</PRODUCTS_PRICE_RECOMMENDED>
      <GRADUATED_PRICES></GRADUATED_PRICES>
      <OTHER_UNITS>
        <OTHER_UNIT>
          <MODEL>ACK100L10-AM-3-H</MODEL>
          <PACKUNG>50</PACKUNG>
          <PRODUCTS_PRICE>300.000000</PRODUCTS_PRICE>
          <PRODUCTS_PRICE_SINGLE_UNIT>6.000000</PRODUCTS_PRICE_SINGLE_UNIT>
        </OTHER_UNIT>
      </OTHER_UNITS>
    </PRODUCT>
    <PRODUCT>
      <PRODUCTS_MODEL>ACK100L10-AM-3-H</PRODUCTS_MODEL>
      <PRODUCTS_PRICE>23,63</PRODUCTS_PRICE>
      <PRODUCTS_PRICE_RECOMMENDED>49,58</PRODUCTS_PRICE_RECOMMENDED>
      <GRADUATED_PRICES>
        <GRADUATED_PRICE>
          <QUANTITY>10</QUANTITY>
          <PRODUCTS_PRICE>22,50</PRODUCTS_PRICE>
        </GRADUATED_PRICE>
        <GRADUATED_PRICE>
          <QUANTITY>20</QUANTITY>
          <PRODUCTS_PRICE>21,50</PRODUCTS_PRICE>
        </GRADUATED_PRICE>
      </GRADUATED_PRICES>
      <OTHER_UNITS></OTHER_UNITS>
    </PRODUCT>
  </PRICES>
</INNOCIGS_API_RESPONSE>
```



---

### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/prices
```

### Rückgabe REST-Api:

```json
{
  "PRICES": {
    "PRODUCT": [
      {
        "PRODUCTS_MODEL": "12M100L10-BG-0",
        "PRODUCTS_PRICE": "7,52",
        "PRODUCTS_PRICE_RECOMMENDED": "16,95",
        "GRADUATED_PRICES": {
          "GRADUATED_PRICE": [
            {
              "QUANTITY": 5,
              "PRODUCTS_PRICE": "6.998400"
            }
          ]
        },
        "OTHER_UNITS": {
          "OTHER_UNIT": [
            {
              "MODEL": "12M100L10-BG-0-H",
              "PACKUNG": "10",
              "PRODUCTS_PRICE": "70.000000",
              "PRODUCTS_PRICE_SINGLE_UNIT": "0.700000"
            }
          ]
        }
      },
      {
        "PRODUCTS_MODEL": "12M100L10-BN-20",
        "PRODUCTS_PRICE": "2,30",
        "PRODUCTS_PRICE_RECOMMENDED": "5,90",
        "GRADUATED_PRICES": "",
        "OTHER_UNITS": ""
      },
      {
        "PRODUCTS_MODEL": "12M100L10-BN-20-H",
        "PRODUCTS_PRICE": "22,95",
        "PRODUCTS_PRICE_RECOMMENDED": "59,00",
        "GRADUATED_PRICES": "",
        "OTHER_UNITS": ""
      }
    ]
  }
}
```



---

### Felder:

| Feld | Beschreibung |
|---|---|
| **PRICES** | Container für Artikel |
| **PRODUCTS_MODEL** | Artikelnummer |
| **PRODUCTS_PRICE** | Preis |
| **PRODUCTS_PRICE_RECOMMENDED** | UVP |
| **GRADUATED_PRICES** | Staffelpreise welche ab der jeweils angegebenen Menge (QUANTITY) gelten |
| **OTHER_UNITS** | Größere Verpackungseinheiten mit Preisinformationen zu Gesamtpreis und Einzelpreis |

## Dropship Auftrag übermitteln

### Post-Parameter:

| Parameter | Beschreibung |
|---|---|
| **cid** | Kundennummer |
| **auth** | API-Passwort |
| **xml** | XML mit Dropship-Request |

### Aufruf als POST-Request über die XML-Api:

```
XML-Api: https://www.innocigs.com/xmlapi/apiv2.php
```

Bei einem erfolgreichen Aufruf wird eine Bestellung in unser System eingetragen. Als Rechnungsadresse wird ihre momentane Rechnungsadresse wie sie auch in ihrem Account hinterlegt ist verwendet. Sollte sich ihr Account noch im Test-Modus befinden wird die Bestellung nicht eingetragen sondern nur ihr Request auf Gültigkeit überprüft.

### Felder im Dropship-Request-XML:

| Feld | Verwendung | Beschreibung |
|---|---|---|
| **DROPSHIP** | Container für Dropship | |
| **DATA** | Container für Stammdaten Dropship | |
| **SHIPPER** | Container für Absender | |
| **RECEIVER** | Container für Empfänger | |
| **ORDERS_NUMBER** | eigene Bestellnummer | |
| **COMPANY** | Firma Absender/Empfänger(Bei | Max. 30 Zeichen, Versender-Firma min. 3 Zeichen |
| **COMPANY2** | Adresszeile2 Absender/Empfänger (optional) | Max. 30 Zeichen. Firma und Adresszeile 2 zusammen max 34 Zeichen, Wenn an eine Packstation gesendet wird |
| **FIRSTNAME** | Vorname Absender/Empfänger | Min. 2 Zeichen, Vorname und Nachname zusammen max. 34 Zeichen |
| **LASTNAME** | Nachname Absender/Empfänger | Min. 2 Zeichen, Vorname und Nachname zusammen max. 34 Zeichen |
| **STREET_ADDRESS** | Strasse Hausnummer Absender/Empfänger | Straße mit Hausnummer, Min. 5 und max. 35 Zeichen |
| **POSTCODE** | PLZ Absender/Empfänger | Min. 4 Zeichen |
| **CITY** | Stadt Absender/Empfänger | Min. 3 Zeichen |
| **COUNTRY_CODE** | Land als Absender/Empfänger | ISO-3166-1-Alpha-2-CODE |
| **EMAIL** | E-Mail-Adresse des Absenders/ (Empfängers) optional für | gültiges e-Mail Format, min. 6 Zeichen, Empfänger Sendungsbenachrichtigung |
| **TELEPHONE** | Telefonnummer des | Absenders(optional) |
| **BIRTHDAY** | Geburtsdatum des Dropship-Empfängers | Deutsches Format, z.b. 23.6.1989 |
| **PRODUCTS** | Container für Produkte Dropship | |
| **PRODUCT** | Container für Produkt | |
| **PRODUCTS_MODEL** | Artikelnummer | |
| **QUANTITY** | Anzahl | |



---

```
cid=[Kundennummer]&auth=[API-PASSWORT]&command=dropship&xml=<INNOCIGS_API_REQUEST>
<DROPSHIPPING>
<DROPSHIP>
<DATA>
<ORDERS_NUMBER>ORDER321</ORDERS_NUMBER>
<SHIPPER>
<COMPANY>Absender-Firma</COMPANY>
<COMPANY2>Adresszeile2</COMPANY2>
<FIRSTNAME>Vorname Anpsrechpartner</FIRSTNAME>
<LASTNAME>Nachname Anpsrechpartner</LASTNAME>
<STREET_ADDRESS>Teststrasse 10</STREET_ADDRESS>
<POSTCODE>22761</POSTCODE>
<CITY>Hamburg</CITY>
<COUNTRY_CODE>DE</COUNTRY_CODE>
<EMAIL>absender@dropship.com</EMAIL>
<TELEPHONE>040 123456</TELEPHONE>
</SHIPPER>
<RECEIVER>
<COMPANY>Empfänger-Firma</COMPANY>
<COMPANY2>Adressezeile2</COMPANY2>
<FIRSTNAME>Vorname Empfänger</FIRSTNAME>
<LASTNAME>Nachname Empfänger</LASTNAME>
<STREET_ADDRESS>Teststrasse 23</STREET_ADDRESS>
<POSTCODE>22761</POSTCODE>
<CITY>Hamburg</CITY>
```



---

### Rückgabe XML-Api:

```xml
<?xml version="1.0" encoding="utf-8"?>
<INNOCIGS_API_RESPONSE>
  <DROPSHIPPING>
    <DROPSHIP>
      <ORDERS_NUMBER>ORDER321</ORDERS_NUMBER>
      <STATUS>OK</STATUS>
      <MESSAGE>Dropship erfolgreich eingetragen</MESSAGE>
      <DROPSHIP_ID>243</DROPSHIP_ID>
      <ORDERS_ID>1126708</ORDERS_ID>
    </DROPSHIP>
    <DROPSHIP>
      <ORDERS_NUMBER>ORDER324</ORDERS_NUMBER>
      <STATUS>NOK</STATUS>
      <MESSAGE>Dropship fehlgeschlagen</MESSAGE>
      <ERRORS>
        <ERROR>
          <CODE>30001</CODE>
          <MESSAGE>AS100AMZ nicht lieferbar</MESSAGE>
        </ERROR>
      </ERRORS>
      <DROPSHIP_ID>-1</DROPSHIP_ID>
      <ORDERS_ID>-1</ORDERS_ID>
    </DROPSHIP>
    ...
  </DROPSHIPPING>
</INNOCIGS_API_RESPONSE>
```

### Beispiel Response-Tabellen:

**DROPSHIP:**

| ORDERS_NUMBER | STATUS | MESSAGE | DROPSHIP_ID | ORDERS_ID |
|---|---|---|---|---|
| ORDER321 | OK | Dropship erfolgreich eingetragen | 243 | 1126708 |
| ORDER324 | NOK | Dropship fehlgeschlagen | -1 | -1 |

**ERRORS:**

| CODE | MESSAGE |
|---|---|
| 30001 | AS100AMZ nicht lieferbar |



---

Im Fehlerfall wird für den jeweiligen Dropship-Auftrag der Status NOK mit einer detaillierten Fehlermeldung zurückgegeben.

### Aufruf als POST-Request über die REST-Api:

Es ist ebenso möglich einen Dropship-Auftrag über die REST-Api zu übergeben. Hierbei wird die Bestellung im Gegensatz zur XML-Api als JSON-Objekt im Request-Body als raw übergeben. Es gelten hier dieselben Feldnamen wie bei der XML-Api.

### REST-Api (Als POST-Request):

```
https://www.innocigs.com/restapi/dropship
```

### Beispiel: Inhalt des JSON-Objektes welches als raw im Request-Body übergeben wird:

```json
{
  "DROPSHIPPING": {
    "DROPSHIP": {
      "DATA": {
        "ORDERS_NUMBER": "ORDER1234",
        "RECEIVER": {
          "BIRTHDAY": "23.6.1969",
          "CITY": "Hamburg",
          "COMPANY": "Empfänger Firma",
          "COMPANY2": "Adresszeile2",
          "COUNTRY_CODE": "DE",
          "EMAIL": "kunde@test.abc",
          "FIRSTNAME": "Vorname Empfänger",
          "LASTNAME": "Nachname Empfänger",
          "POSTCODE": "22761",
          "STREET_ADDRESS": "Teststrasse 23"
        },
        "SHIPPER": {
          "CITY": "Hamburg",
          "COMPANY": "Firma ABC",
          "COMPANY2": "Adresszeile2",
          "COUNTRY_CODE": "DE",
          "EMAIL": "absender@test.abc",
          "FIRSTNAME": "Vorname Ansprechpartner",
          "LASTNAME": "Nachname Ansprechpartner",
          "POSTCODE": "22761",
          "STREET_ADDRESS": "Teststrasse 10",
          "TELEPHONE": "555 123456"
        }
      },
      "PRODUCTS": [
        {
          "PRODUCTS_MODEL": "IC10000L10-TE-3",
          "QUANTITY": 2
        },
        {
          "PRODUCTS_MODEL": "IC10000AIO-10",
          "QUANTITY": 1
        }
      ]
    }
  }
}
```



---

### Rückgabe REST-Api:

```json
{
  "DROPSHIPPING": {
    "DROPSHIP": {
      "ORDERS_NUMBER": "ORDER1234",
      "STATUS": "OK",
      "MESSAGE": "Dropship erfolgreich eingetragen",
      "DROPSHIP_ID": 68,
      "ORDERS_ID": 77
    }
  }
}
```



---

### Felder:

| Feld | Beschreibung |
|---|---|
| **DROPSHIP** | Container für Dropship |
| **ORDERS_NUMBER** | übergebene Bestellnummer Dropship |
| **STATUS** | Status(OK/NOK) |
| **MESSAGE** | Status-Nachricht |
| **DROPSHIP_ID** | DropShip-ID Innocigs |
| **ORDERS_ID** | Orders-ID Innocigs |
| **ERRORS** | Container für Fehlermeldungen |
| **ERROR** | Container für Fehler |
| **CODE** | Fehler-Code |
| **MESSAGE** | Fehler-Meldung |

## Bestellung ohne Dropship

Die Api bietet die Möglichkeit, normale Bestellungen ohne Dropships anlegen zu lassen. Diese werden dann so behandelt, als würde direkt im Onlineshop eingekauft.

**Hinweis:** Es kann nur eine Bestellung pro Request übermittelt werden.

Informationen zur Bestellungen von Dropships stehen im Kapitel Dropship Auftrag übermitteln.

### Post-Parameter:

| Parameter | Beschreibung |
|---|---|
| **cid** | Kundennummer |
| **auth** | API-Passwort |
| **xml** | XML mit Order-Request |
| **shipping** | Optional. Die Angabe, ob mit DHL oder UPS geliefert werden soll. Wenn es weggelassen wird, wird DHL verwendet. |

Bei einem erfolgreichen Aufruf wird eine Bestellung in unser System eingetragen. Als Rechnungsadresse wird ihre momentane Rechnungsadresse wie sie auch in ihrem Account hinterlegt ist verwendet. Als Lieferadresse wird die im Request.


---
Angegebene verwendet. Wenn diese Lieferadresse noch nicht in Ihrem Account eingetragen sein, wird diese dort hinterlegt. Sollte sich ihr Account noch im Test-Modus befinden wird die Bestellung nicht eingetragen sondern nur ihr Request auf Gültigkeit überprüft.

### Felder im Order-Request:

| Feld | Beschreibung |
|---|---|
| **DATA** | Container für Stammdaten |
|---|---|
|RECEIVER|Container für Empfänger|
|ORDERS_NUMBER|eigene Bestellnummer|
|COMPANY|Firma (optional)|
| |Max. 30 Zeichen, Versender-Firma min. 3 Zeichen|
|COMPANY2|Adresszeile2 (optional)|
| |Max. 30 Zeichen. Firma und Adresszeile 2 zusammen max 34 Zeichen, Wenn an eine Packstation gesendet wird|
|FIRSTNAME|Vorname|
| |Min. 2 Zeichen, Vorname und Nachname zusammen max. 34 Zeichen|
|LASTNAME|Nachname|
| |Min. 2 Zeichen, Vorname und Nachname zusammen max. 34 Zeichen|
|STREET_ADDRESS|Strasse Hausnummer|
| |Straße mit Hausnummer, Min. 5 und max. 35 Zeichen|
|POSTCODE|PLZ|
| |Min. 4 Zeichen|
|CITY|Stadt|
| |Min. 3 Zeichen|
|COUNTRY_CODE|Land als ISO-3166-1-Alpha-2-CODE|
|PRODUCTS|Container für Produkte|
|PRODUCT|Ein Produkt|
|PRODUCTS_MODEL|Artikelnummer|
|QUANTITY|Anzahl|

### Aufruf als POST-Request über die XML-Api:


---

### XML-Api URL:

```
https://www.innocigs.com/xmlapi/apiv2.php
```

### Beispiel: Inhalt von einem Post-Request:

```
cid=[Kundennummer]&auth=[API-PASSWORT]&command=order&shipping=DHL&xml=<INNOCIGS_API_REQUEST>
<ORDER>
  <DATA>
    <ORDERS_NUMBER>12345</ORDERS_NUMBER>
    <RECEIVER>
      <COMPANY>[Firma]</COMPANY>
      <FIRSTNAME>[Vorname]</FIRSTNAME>
      <LASTNAME>[Nachname]</LASTNAME>
      <STREET_ADDRESS>[Straße/Nr.]</STREET_ADDRESS>
      <POSTCODE>[PLZ]</POSTCODE>
      <CITY>[Ort]</CITY>
      <COUNTRY_CODE>DE</COUNTRY_CODE>
    </RECEIVER>
  </DATA>
  <PRODUCTS>
    <PRODUCT>
      <PRODUCTS_MODEL>IC100T-11</PRODUCTS_MODEL>
      <QUANTITY>6</QUANTITY>
    </PRODUCT>
    <PRODUCT>
      <PRODUCTS_MODEL>IC10000L10-DD-6</PRODUCTS_MODEL>
      <QUANTITY>10</QUANTITY>
    </PRODUCT>
    ...
  </PRODUCTS>
</ORDER>
</INNOCIGS_API_REQUEST>
```

### Rückgabe:

```xml
<?xml version="1.0" encoding="utf-8"?>
<INNOCIGS_API_RESPONSE>
  <ORDER>
    <ORDERS_NUMBER>12345</ORDERS_NUMBER>
    <STATUS>OK</STATUS>
    <MESSAGE>Bestellung erfolgreich eingetragen</MESSAGE>
    <ORDERS_ID>1151607</ORDERS_ID>
  </ORDER>
</INNOCIGS_API_RESPONSE>
```

**- oder -**

```xml
<?xml version="1.0" encoding="utf-8"?>
<INNOCIGS_API_RESPONSE>
  <ORDER>
    <ORDERS_NUMBER>ORDER324</ORDERS_NUMBER>
    <STATUS>NOK</STATUS>
    <MESSAGE>Eintragen der Bestellung fehlgeschlagen</MESSAGE>
    <ORDERS_ID>-1</ORDERS_ID>
    <ERRORS>
      <ERROR>
        <CODE>30001</CODE>
        <MESSAGE>AS100AMZ nicht lieferbar</MESSAGE>
      </ERROR>
    </ERRORS>
  </ORDER>
</INNOCIGS_API_RESPONSE>
```



---

Im Fehlerfall wird für den jeweiligen Request der Status NOK mit einer detaillierten Fehlermeldung zurückgegeben.

### Felder:

- **ORDERS_NUMBER** - übergebene Bestellnummer
- **STATUS** - Status(OK/NOK)
- **MESSAGE** - Status-Nachricht
- **ORDERS_ID** - Orders-ID Innocigs
- **ERRORS** - Container für Fehlermeldungen
- **ERROR** - Container für Fehler
- **CODE** - Fehler-Code
- **MESSAGE** - Fehler-Meldung

Es lässt sich ebenso die Bestellung über die REST-Api eintragen. Auch hier gelten wieder dieselben Feldnamen wie bei dem XML-Request, die Bestellung wird jedoch über einen POST-Request im raw-Header wieder als JSON-Objekt übergeben.

### REST-Api (Als POST-Request):

```
https://www.innocigs.com/restapi/order
```

### Beispiel: Inhalt von einem Post-Request im JSON-Format:

```json
{
  "ORDER": {
    "DATA": {
      "ORDERS_NUMBER": "ORDER1234",
      "RECEIVER": {
        "FIRSTNAME": "Vorname Empfänger",
        "LASTNAME": "Nachname Empfänger",
        "BIRTHDAY": "23.6.1969",
        "CITY": "Hamburg",
        "POSTCODE": "22761",
        "STREET_ADDRESS": "Teststrasse 23",
        "COUNTRY_CODE": "DE",
        "COMPANY": "Empfänger Firma",
        "COMPANY2": "Adresszeile2",
        "EMAIL": "kunde@test.abc"
      }
    },
    "PRODUCTS": [
      {
        "PRODUCTS_MODEL": "IC10000L10-TE-3",
        "QUANTITY": 2
      },
      {
        "PRODUCTS_MODEL": "IC10000AIO-10",
        "QUANTITY": 1
      }
    ]
  }
}
```



---

### Rückgabe REST-Api:

```json
{
  "ORDER": {
    "ORDERS_NUMBER": "ORDER12345",
    "STATUS": "OK",
    "MESSAGE": "Bestellung erfolgreich eingetragen",
    "ORDERS_ID": 78
  }
}
```

**- oder -**

```json
{
  "ORDER": {
    "ORDERS_NUMBER": "ORDER123456",
    "STATUS": "NOK",
    "MESSAGE": "Eintragen der Bestellung fehlgeschlagen",
    "ORDERS_ID": -1,
    "ERRORS": [
      {
        "CODE": 30001,
        "MESSAGE": "AS100AMZ nicht lieferbar"
      }
    ]
  }
}
```



---

## Trackingdaten abfragen (TAG)

### Parameter:

- **cid**: Kundennummer
- **auth**: API-Passwort
- **day**: Tag als Timestamp (2018-05-01)

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=tracking&day=[TAG]
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <TRACKING>
    <DROPSHIP>
      <DROPSHIP_ID>112</DROPSHIP_ID>
      <ORDERS_NUMBER>001234</ORDERS_NUMBER>
      <DELIVERY_NUMBER>S0000001</DELIVERY_NUMBER>
      <TRACKINGS>
        <TRACKINGINFO>
          <CARRIER>DHL</CARRIER>
          <CODE>TR000001</CODE>
          <RECEIVER>
            <COMPANY>Musterfirma</COMPANY>
            <COMPANY2 />
            <FIRSTNAME>Hans</FIRSTNAME>
            <LASTNAME>Muster</LASTNAME>
            <STREET_ADDRESS>Musterweg 99</STREET_ADDRESS>
            <POSTCODE>22761</POSTCODE>
            <CITY>Hamburg</CITY>
            <COUNTRY_CODE>DE</COUNTRY_CODE>
          </RECEIVER>
        </TRACKINGINFO>
      </TRACKINGS>
    </DROPSHIP>
  </TRACKING>
</INNOCIGS_API_RESPONSE>
```



---

### Beispiel Tracking-Response:

**DROPSHIP:**

| Feld | Wert |
|---|---|
| **DROPSHIP_ID** | 113 |
| **ORDERS_NUMBER** | 001235 |
| **DELIVERY_NUMBER** | S0000002 |
| **CARRIER** | DHL |
| **CODE** | TR000002 |

**RECEIVER:**

| Feld | Wert |
|---|---|
| **FIRSTNAME** | Karl |
| **LASTNAME** | Muster |
| **STREET_ADDRESS** | Musterstr. 12 |
| **POSTCODE** | 24103 |
| **CITY** | Kiel |
| **COUNTRY_CODE** | DE |

**CANCELLATION:**

| Feld | Wert |
|---|---|
| **DROPSHIP_ID** | 114 |
| **ORDERS_NUMBER** | 001236 |
| **MESSAGE** | Der Auftrag wurde storniert |

### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/tracking/[TAG]
```

### Rückgabe REST-Api:

```json
{
  "TRACKING": {
    "DROPSHIP": [
      {
        "DROPSHIP_ID": "6",
        "ORDERS_NUMBER": "DS24",
        "DELIVERY_NUMBER": "S0447631",
        "TRACKINGS": [
          {
            "TRACKINGINFO": {
              "CARRIER": "DHL",
              "CODE": "0034012345",
              "RECEIVER": {
                "COMPANY": "",
                "COMPANY2": "",
                "FIRSTNAME": "Max",
                "LASTNAME": "Mustermann",
                "STREET_ADDRESS": "Str.7",
                "POSTCODE": "12345",
                "CITY": "Teststadt",
                "COUNTRY_CODE": "DE"
              }
            }
          }
        ]
      }
    ]
  }
}
```



---

### Weitere Beispiel-Daten:

**DROPSHIP:**

| DROPSHIP_ID | ORDERS_NUMBER | DELIVERY_NUMBER | CARRIER | CODE |
|---|---|---|---|---|
| 1 | DS25 | S0447585 | DHL | 0034012344 |

**RECEIVER:**

| FIRSTNAME | LASTNAME | STREET_ADDRESS | POSTCODE | CITY | COUNTRY_CODE |
|---|---|---|---|---|---|
| Thomas | Muster | Hauptstr.81 | 12345 | Teststadt | DE |

**CANCELLATION:**

| DROPSHIP_ID | ORDERS_NUMBER | MESSAGE |
|---|---|---|
| 8 | DSX1 | Der Auftrag wurde storniert |


---

### Felder:

- **TRACKINGINFO** - Container für Tracking-infos des Pakets
- **CARRIER** - Versender (DHL)
- **CODE** - Trackingcode
- **RECEIVER** - Adressdaten des Empfängers
- **CANCELLATION** - Container für Stornofälle



---

## Trackingdaten abfrage (Order)

### Parameter:

- **cid**: Kundennummer
- **auth**: API-Passwort
- **order**: Orders Number

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=tracking&order=[ORDERS NUMBER]
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <TRACKING>
    <DROPSHIP>
      <DROPSHIP_ID>112</DROPSHIP_ID>
      <ORDERS_NUMBER>001234</ORDERS_NUMBER>
      <DELIVERY_NUMBER>S0000001</DELIVERY_NUMBER>
      <TRACKINGS>
        <TRACKINGINFO>
          <CARRIER>DHL</CARRIER>
          <CODE>TR000001</CODE>
          <RECEIVER>
            <COMPANY>Musterfirma</COMPANY>
            <COMPANY2 />
            <FIRSTNAME>Hans</FIRSTNAME>
            <LASTNAME>Muster</LASTNAME>
            <STREET_ADDRESS>Musterweg 99</STREET_ADDRESS>
            <POSTCODE>22761</POSTCODE>
            <CITY>Hamburg</CITY>
            <COUNTRY_CODE>DE</COUNTRY_CODE>
          </RECEIVER>
        </TRACKINGINFO>
      </TRACKINGS>
    </DROPSHIP>
    <DROPSHIP>
      <DROPSHIP_ID>113</DROPSHIP_ID>
      <ORDERS_NUMBER>001235</ORDERS_NUMBER>
      <DELIVERY_NUMBER>S0000002</DELIVERY_NUMBER>
      <TRACKINGS>
        <TRACKINGINFO>
          <CARRIER>DHL</CARRIER>
          <CODE>TR000002</CODE>
          <RECEIVER>
            <COMPANY />
            <COMPANY2 />
            <FIRSTNAME>Karl</FIRSTNAME>
```



---

```xml
            <LASTNAME>Muster</LASTNAME>
            <STREET_ADDRESS>Musterstr. 12</STREET_ADDRESS>
            <POSTCODE>24103</POSTCODE>
            <CITY>Kiel</CITY>
            <COUNTRY_CODE>DE</COUNTRY_CODE>
          </RECEIVER>
        </TRACKINGINFO>
      </TRACKINGS>
    </DROPSHIP>
    <CANCELLATION>
      <DROPSHIP_ID>114</DROPSHIP_ID>
      <ORDERS_NUMBER>001236</ORDERS_NUMBER>
      <MESSAGE>Der Auftrag wurde storniert</MESSAGE>
    </CANCELLATION>
  </TRACKING>
</INNOCIGS_API_RESPONSE>
```



---

### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/tracking-order/[ORDERS NUMBER]
```

### Rückgabe REST-Api:

```json
{
  "TRACKING": {
    "DROPSHIP": [
      {
        "DROPSHIP_ID": "6",
        "ORDERS_NUMBER": "DS24",
        "DELIVERY_NUMBER": "S0447631",
        "TRACKINGS": [
          {
            "TRACKINGINFO": {
              "CARRIER": "DHL",
              "CODE": "0034012345",
              "RECEIVER": {
                "COMPANY": "",
                "COMPANY2": "",
                "FIRSTNAME": "Max",
                "LASTNAME": "Mustermann",
                "STREET_ADDRESS": "Str.7",
                "POSTCODE": "12345",
                "CITY": "Teststadt",
                "COUNTRY_CODE": "DE"
              }
            }
          }
        ]
      },
      {
        "DROPSHIP_ID": "1",
        "ORDERS_NUMBER": "DS25",
        "DELIVERY_NUMBER": "S0447585",
        "TRACKINGS": [
          {
            "TRACKINGINFO": {
              "CARRIER": "DHL",
              "CODE": "0034012344",
              "RECEIVER": {
                "FIRSTNAME": "Thomas",
                "LASTNAME": "Muster",
                "STREET_ADDRESS": "Hauptstr.81",
                "POSTCODE": "12345",
                "CITY": "Teststadt",
                "COUNTRY_CODE": "DE"
              }
            }
          }
        ]
      }
    ],
    "CANCELLATION": {
      "DROPSHIP_ID": "8",
      "ORDERS_NUMBER": "DSX1",
      "MESSAGE": "Der Auftrag wurde storniert"
    }
  }
}
```



---

### Felder:

| Feld | Beschreibung |
|---|---|
| **DROPSHIP** | Container für Dropship |
| **DROPSHIP_ID** | DropShip-ID Innocigs |
| **ORDERS_NUMBER** | übergebene Bestellnummer Dropship |
| **DELIVERY_NUMBER** | Lieferscheinnummer |
| **TRACKINGS** | Container für Tracking-Codes |
| **TRACKINGINFO** | Container für Tracking-infos des Pakets |
| **CARRIER** | Versender (DHL) |
| **CODE** | Trackingcode |
| **RECEIVER** | Adressdaten des Empfängers |
| **CANCELLATION** | Container für Stornofälle |

---

## Lieferscheine abfragen

Mit dem delivery-Command kann man die Produkte abfragen, die an einem bestimmten Tag versendet wurden. Da eine Bestellung in mehrere Sendungen aufgeteilt sein kann, kann man eine Bestellung nicht direkt abfragen. Diese Funktion dient nur zu der Abfrage von Lieferungen aus Bestellungen. Für Dropships bitte das Kapitel Trackingdaten abfragen beachten.

### Parameter:

- **cid**: Kundennummer
- **auth**: API-Passwort
- **day**: Datum, z.B. 2018-05-01

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=delivery&day=[TAG]
```

### Rückgabe XML-Api:

```xml
<?xml version="1.0" encoding="utf-8"?>
<INNOCIGS_API_RESPONSE>
  <DELIVERIES>
    <DELIVERY>
      <RECEIVER>
        <COMPANY>Musterfirma</COMPANY>
        <COMPANY2 />
        <FIRSTNAME>Max</FIRSTNAME>
        <LASTNAME>Mustermann</LASTNAME>
        <STREET_ADDRESS>Musterstraße 1</STREET_ADDRESS>
        <POSTCODE>12345</POSTCODE>
        <CITY>Musterstadt</CITY>
        <COUNTRY_CODE>DE</COUNTRY_CODE>
      </RECEIVER>
      <DELIVERY_NUMBER>S0000004</DELIVERY_NUMBER>
      <TRACKINGS>
        <TRACKING carrier="TEST" tracking_code="ABCDE123456789" />
        ...
      </TRACKINGS>
      <INCLUDED_ORDERS>
        <ORDER>
          <ORDERS_NUMBER>ABC-123</ORDERS_NUMBER>
          <ORDERS_ID>123456</ORDERS_ID>
          <PRODUCTS>
            <PRODUCT>
              <PRODUCTS_MODEL>IC100TEST-1</PRODUCTS_MODEL>
            </PRODUCT>
          </PRODUCTS>
        </ORDER>
      </INCLUDED_ORDERS>
    </DELIVERY>
  </DELIVERIES>
</INNOCIGS_API_RESPONSE>
```

---

### Aufruf REST-Api (Als GET-Request):

```
https://www.innocigs.com/restapi/delivery/[TAG]
```

### Rückgabe REST-Api:

```json
{
  "DELIVERIES": {
    "DELIVERY": [
      {
        "RECEIVER": {
          "COMPANY": "",
          "COMPANY2": "",
          "FIRSTNAME": "Markus",
          "LASTNAME": "Tester",
          "STREET_ADDRESS": "Teststr. 9",
          "POSTCODE": "12345",
          "CITY": "Teststadt",
          "COUNTRY_CODE": "DE"
        },
        "DELIVERY_NUMBER": "S0448091",
        "TRACKINGS": {
          "TRACKING": [
            {
              "_attributes": {
                "carrier": "DHL",
                "tracking_code": "00340654321"
              }
            }
          ]
        },
        "INCLUDED_ORDERS": [
          {
            "ORDER": {
              "ORDERS_NUMBER": "ORDER15",
              "ORDERS_ID": "9903478-14645",
              "PRODUCTS": {
                "PRODUCT": [
                  {
                    "PRODUCTS_MODEL": "GV100ABP1-10",
                    "QUANTITY": "1"
                  }
                ]
              }
            }
          }
        ]
      }
    ]
  }
}
```


---

### Felder:

| Feld | Beschreibung |
|---|---|
| **DELIVERY** | Eine Lieferung. Es kann mehrere Lieferungen pro Response geben. |
| **RECEIVER** | Adressdaten des Empfängers |

### Beispiel-Daten:

**RECEIVER:**
- FIRSTNAME: Manuell
- LASTNAME: Test
- STREET_ADDRESS: Teststr. 13
- POSTCODE: 12345
- CITY: Teststadt
- COUNTRY_CODE: DE

**DELIVERY_NUMBER:** S0448092

**TRACKINGS:**

| Carrier | Tracking Code |
|---|---|
| DHL | 0034012345 |

**INCLUDED_ORDERS:**

| ORDER NUMBER | ORDER ID | PRODUCTS MODEL | QUANTITY |
|---|---|---|---|
| ORDER12 | 9013478-314643 | IC10000L10-AH-6 | 10 |

### Felddetails:

- **DELIVERY_NUMBER**: Lieferscheinnummer
- **TRACKINGS**: Container für eine Liste von Tracking-Infos
- **TRACKING**: Eine Tracking-Information. Enthält die Tracking-Daten als Attribute. Kann mehrfach pro Lieferung vorhanden sein.
- **TRACKING::carrier**: Lieferant
- **TRACKING::tracking_code**: Trackingcode
- **INCLUDED_ORDERS**: Container für zu der Lieferung gehörenden Bestellungen
- **ORDER**: Eine Bestellung. Kann mehrfach pro Lieferung vorhanden sein, da Produkte aus mehreren Bestellungen zusammen versendet werden können.
- **ORDERS_NUMBER**: Vom Kunden übergebene Bestellnummer. Kann leer sein.
- **ORDERS_ID**: Bestellnummer Innocigs
- **PRODUCTS**: Container für in der Lieferung enthaltene Produkte
- **PRODUCT**: Ein Produkt



---

## Ausstehende Artikel abfragen

### Parameter:

- **cid**: Kundennummer
- **auth**: API-Passwort

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/apiv2.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=pending
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <PENDINGS>
    <PRODUCT>
      <ORDERS_ID>1898808</ORDERS_ID>
      <PRODUCTS_MODEL>GV100ZT-10</PRODUCTS_MODEL>
      <QUANTITY>1</QUANTITY>
      <EAN>6974622800512</EAN>
      <SHIPPING_STATUS>in 1-10 Tagen lieferbar</SHIPPING_STATUS>
    </PRODUCT>
    <PRODUCT>
      <ORDERS_ID>1898808</ORDERS_ID>
      <PRODUCTS_MODEL>GV100ZT-11</PRODUCTS_MODEL>
      <QUANTITY>1</QUANTITY>
      <EAN>6974622800475</EAN>
      <SHIPPING_STATUS>in 1-10 Tagen lieferbar</SHIPPING_STATUS>
    </PRODUCT>
    …
  </PENDINGS>
</INNOCIGS_API_RESPONSE>
```

### Aufruf REST-Api:

```
https://www.innocigs.com/restapi/pending
```

### Rückgabe REST-Api:

```json
{
  "PENDINGS": {
    "PRODUCT": [
      {
        "ORDERS_ID": "53-44",
        "PRODUCTS_MODEL": "AV100A10-SP-A",
        "QUANTITY": "20",
        "EAN": "4260510026129",
        "SHIPPING_STATUS": "in 1-10 Tagen lieferbar"
      }
    ]
  }
}
```



---

### Felder:

| Feld | Beschreibung |
|---|---|
| **PRODUCT** | Container |
| **ORDERS_ID** | Bestellnummer |
| **PRODUCTS_MODEL** | Artikelnummer |
| **QUANTITY** | Anzahl |
| **EAN** | EAN des Artikels |
| **SHIPPING_STATUS** | Versand-Status |



---

## Produkte und EANS abfragen

### Parameter:

- **cid**: Kundennummer
- **auth**: API-Passwort
- **type**: normal=Ohne Produkt-Beschreibung, extended=Mit Produkt-Beschreibung

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/api.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=products
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <PRODUCTS>
    <PRODUCT>
      <CATEGORY>Zubehör</CATEGORY>
      <MASTER>AS10000NAUT</MASTER>
      <MODEL>AS10000A1</MODEL>
      <EAN>4313042776687</EAN>
      <NAME>Aspire Nautilus Clearomizer Set</NAME>
      <PARENT_NAME>Aspire Nautilus Clearomizer Set</PARENT_NAME>
      <PRODUCTS_PRICE>13,11</PRODUCTS_PRICE>
      <PRODUCTS_PRICE_RECOMMENDED>29,95</PRODUCTS_PRICE_RECOMMENDED>
      <PRODUCTS_IMAGE>https://cdn.innocigs.com/(...)</PRODUCTS_IMAGE>
      <PRODUCTS_IMAGE_ADDITIONAL>
        <IMAGE>https://cdn.innocigs.com(...)</IMAGE>
        <IMAGE>https://cdn.innocigs.com(...)</IMAGE>
      </PRODUCTS_IMAGE_ADDITIONAL>
      <MANUFACTURER>Aspire</MANUFACTURER>
      <PRODUCTS_MANUAL>http://www.innocigs.com/(...)</PRODUCTS_MANUAL>
    </PRODUCT>
    <PRODUCT>
      <CATEGORY>Liquids > SC</CATEGORY>
      <MASTER>SC10000L10-AF</MASTER>
      <MODEL>SC10000L10-AF-L-H</MODEL>
      <EAN>4313042643316</EAN>
      <NAME>Americas Finest Tabak E-Zigaretten Liquid 6 mg/ml 10er Packung</NAME>
      <PARENT_NAME>America's Finest Tabak E-Zigaretten Liquid</PARENT_NAME>
      <PRODUCTS_PRICE>8,50</PRODUCTS_PRICE>
      <PRODUCTS_PRICE_RECOMMENDED>39,50</PRODUCTS_PRICE_RECOMMENDED>
      <PRODUCTS_IMAGE>https://cdn.innocigs.com(...)</PRODUCTS_IMAGE>
      <PRODUCTS_IMAGE_ADDITIONAL />
      <MANUFACTURER>SC</MANUFACTURER>
      <PRODUCTS_ATTRIBUTES></PRODUCTS_ATTRIBUTES>
    </PRODUCT>
  </PRODUCTS>
</INNOCIGS_API_RESPONSE>
```



---

### Beispiel-Produkt: Twelve Monkeys - Bonogurt - 50ml - 0mg/ml

- **Category**: Liquids > Shortfills > Twelve Monkeys
- **Model**: 12M100L10-BG-0
- **EAN**: 0827152053568
- **Manufacturer**: Twelve Monkeys
- **Price**: 7,52 €
- **Recommended Price**: 16,95 €

**Product Attributes:**
- Strength: 6 mg/ml

**Volume Packaging:**

| Content | Unit |
|---|---|
| 100 | ml |

**Graduated Prices:**

| Quantity | Price |
|---|---|
| 10 | 8.30 € |
| 20 | 8.10 € |

**Other Units:**

| Model | Packung | Price | Price per Single Unit |
|---|---|---|---|
| AS10000A1-H | 50 | 300.00 € | 6.00 € |

### Aufruf REST-Api:

```
https://www.innocigs.com/restapi/products/[type]
```

### Rückgabe REST-Api:

```json
{
  "PRODUCTS": {
    "PRODUCT": [
      {
        "CATEGORY": "Liquids > Shortfills > Twelve Monkeys",
        "MASTER": "12M100L10-BG",
        "MODEL": "12M100L10-BG-0",
        "EAN": "0827152053568",
        "NAME": "Twelve Monkeys - Bonogurt - 50ml - 0mg/ml",
        "PARENT_NAME": "Twelve Monkeys - Bonogurt - 50ml - 0mg/ml",
        "PRODUCTS_PRICE": "7,52",
        "PRODUCTS_PRICE_RECOMMENDED": "16,95",
        "PRODUCTS_IMAGE": "https://www.innocigs.com/media/b5/45/6d/1618387425/Bonogurt-60mL-Bottle.png",
        "PRODUCTS_IMAGE_ADDITIONAL": [],
        "MANUFACTURER": "Twelve Monkeys",
        "CLP_INFOS": {},
```



---

```json
        "DESCRIPTION": "Das Shake & Vape Liquid Bonogurt von Twelve Monkeys schmeckt nach Beeren und Joghurt. Shake & Vape Liquids eignen sich nicht für das pure Dampfen. Sie erhalten 50ml Liquid in einer 60ml Flasche geliefert.",
        "COMPOSITION": "Pflanzliches Glycerin, Propylenglykol, Natürliche und künstliche Aromastoffe",
        "PRODUCTS_ATTRIBUTES": {
          "Packung": "1er Packung"
        },
        "VPE": {
          "CONTENT": "50",
          "UNIT": "ml"
        },
        "GRADUATED_PRICES": {
          "PRICE": [
            {
              "QUANTITY": "5",
              "VALUE": "6.998400"
            }
          ]
        },
        "OTHER_UNITS": {
          "UNIT": [
            {
              "MODEL": "AS10000A1-H",
              "PACKAGE": "50",
              "PRICE": "300.000000",
              "PRICE_PER_UNIT": "6.000000"
            }
          ]
        }
      }
    ]
  }
}
```

---
## InnoCigs Dropship-API

### Produktinformationen

|PARENT_NAME|PRODUCTS_PRICE|PRODUCTS_PRICE_RECOMMENDED|PRODUCTS_IMAGE|PRODUCTS_IMAGE_ADDITIONAL|MANUFACTURER|PRODUCTS_ATTRIBUTES|VPE|PRODUCTS_MANUAL|GRADUATED_PRICES|OTHER_UNITS|
|---|---|---|---|---|---|---|---|---|---|---|
|Basis-Artikelname ohne Attribute|Artikelpreis in Euro|Empf. Endkundenpreis in Euro|Url zum Produktbild|Weitere URLs zu Produktbilder, jeweils in eigenen “<IMAGE>”-Containern.|Hersteller|Liste der Attribute in der Form: &lt;[Attribut-Name]&gt;[Wert]&lt;/[Attribut-Name&gt;|Angabe zur Abfüllmenge (Nur bei Artikeln mit Abfüllmenge)|Url zur Produktanleitung (PDF)|Staffelpreise welche ab der jeweils angegebenen Menge (QUANTITY) gelten. Ausgabe nur ab apiv2 und über die REST-Api|Größere Verpackungseinheiten mit Preisinformationen zu Gesamtpreis und Einzelpreis|


Seite: 40
---
## Erweiterte Produktabfrage

### Parameter:

- **cid**: Kundennummer
- **auth**: API-Passwort
- **model**: Artikelnummer des Artikels

### Aufruf XML-Api:

```
https://www.innocigs.com/xmlapi/api.php?cid=[Kundennummer]&auth=[API-PASSWORT]&command=product&model=[Artikelnummer]
```

### Rückgabe XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <PRODUCTS>
    <PRODUCT>
      <MASTER>AS10000NAUT</MASTER>
      <MODEL>AS10000A1</MODEL>
      <EAN>4313042776687</EAN>
      <NAME>Aspire Nautilus Clearomizer Set</NAME>
      <PARENT_NAME>Aspire Nautilus Clearomizer Set</PARENT_NAME>
      <PRODUCTS_PRICE>13,11</PRODUCTS_PRICE>
      <PRODUCTS_PRICE_RECOMMENDED>29,95</PRODUCTS_PRICE_RECOMMENDED>
      <PRODUCTS_IMAGE>https://cdn.innocigs.com/(...)</PRODUCTS_IMAGE>
      <PRODUCTS_IMAGE_ADDITIONAL>
        <IMAGE>https://cdn.innocigs.com(...)</IMAGE>
        <IMAGE>https://cdn.innocigs.com(...)</IMAGE>
      </PRODUCTS_IMAGE_ADDITIONAL>
      <MANUFACTURER>Aspire</MANUFACTURER>
      <DESCRIPTION>
        <![CDATA[
          Der Nautilus Clearomizer wird zusammen mit 2 Heads aus der BVC-Serie geliefert.
          Beide Heads sind für das moderate Dampfen geeignet, da der eine Head einen
          Widerstand von 1,6 Ohm und der andere von 1,8 Ohm hat. Der Tank fasst 5
          Milliliter Liquid und der gesamte Clearomizer ist 8,37 cm lang. <br> <br>
          <b>Lieferumfang:</b>
          <li>1x Nautilus Tank</li>
          <li>1x BVC Atomizer Head 1,8 Ohm</li>
          <li>1x BVC Atomizer Head 1,6 Ohm</li>
          <li>1x eGo Cone</li>
          <li>1x Bedienungsanleitung</li> <br> <br>
          <b>Wichtige Merkmale:</b>
          <li>Tankvolumen: 5 ml</li>
          <li>Durchmesser: 2,35 cm</li>
          <li>Länge: 8,37 cm</li>
          <li>510er Gewinde</li> <br> <br>
        ]]>
      </DESCRIPTION>
      <PRODUCTS_ATTRIBUTES>
        <FARBE>Blau</FARBE>
        ...
      </PRODUCTS_ATTRIBUTES>
    </PRODUCT>
  </PRODUCTS>
</INNOCIGS_API_RESPONSE>
```



---

### REST-Api Aufruf:

```
https://www.innocigs.com/restapi/product/[Artikelnummer]
```

### Rückgabe REST-Api:

```json
{
  "PRODUCTS": {
    "PRODUCT": [
      {
        "CATEGORY": "Liquids > Shortfills > Twelve Monkeys",
        "MASTER": "12M100L10-BG",
        "MODEL": "12M100L10-BG-0",
        "EAN": "0827152053568",
        "NAME": "Twelve Monkeys - Bonogurt - 50ml - 0mg/ml",
        "PARENT_NAME": "Twelve Monkeys - Bonogurt - 50ml - 0mg/ml",
        "PRODUCTS_PRICE": "7,52",
        "PRODUCTS_PRICE_RECOMMENDED": "16,95",
        "PRODUCTS_IMAGE": "https://shopware-test.innocigs.com/media/b5/45/6d/1618387425/Bonogurt-60mL-Bottle.png",
        "PRODUCTS_IMAGE_ADDITIONAL": [],
        "MANUFACTURER": "Twelve Monkeys",
        "CLP_INFOS": {
          "MSDS_CODES": null,
          "MSDS_GHS_SYMBOL": null
        },
"DESCRIPTION": {
"_cdata": "Das Shake & Vape Liquid Bonogurt von Twelve Monkeys schmeckt nach Beeren und Joghurt. Shake & Vape Liquids eignen sich nicht für das pure Dampfen. Sie erhalten 50ml Liquid in einer 60ml Flasche geliefert.\n
\n
\n**Inhaltsstoffe**\nPflanzliches
}
}
]
}
}
```

### Beispiel Staffelpreise:

| Quantity | Price |
|---|---|
| 10 | 12.500000 |
| 20 | 11.500000 |

### Beispiel Andere Einheiten:

| Model | Packung | Price | Price per Single Unit |
|---|---|---|---|
| AS10000A1-H | 50 | 300.000000 | 6.000000 |

---

**InnoCigs Dropship-API** | Innocigs GmbH & Co. KG, Barnerstraße 14c, 22765 Hamburg | Seite 42

---

### Felder:

| Feld | Beschreibung |
|---|---|
| **CATEGORY** | Die bei InnoCigs zugewiesene Produktkategorie |
| **MASTER** | Artikelnummer des Masterartikels |
| **MODEL** | Artikelnummer |
| **EAN** | EAN des Artikels |
| **NAME** | Artikelname (incl. Attribute) |
| **PARENT_NAME** | Basis-Artikelname ohne Attribute |
| **PRODUCTS_PRICE** | Artikelpreis in Euro |
| **PRODUCTS_PRICE_RECOMMENDED** | Empf. Endkundenpreis in Euro |
| **PRODUCTS_IMAGE** | Url zum Produktbild |

### Beispiel Produktdetails:

**Inhaltsstoffe:** Glycerin, Propylenglykol, Natürliche und künstliche Aromastoffe

**Produktattribute:** PACKUNG: 1er Packung

**VPE:**

| CONTENT | UNIT |
|---|---|
| 50 | ml |

**Graduierte Preise:**

| QUANTITY | PRODUCTS_PRICE |
|---|---|
| 5 | 6.998400 |

**Andere Einheiten:**

| MODEL | PACKUNG | PRODUCTS_PRICE | PRODUCTS_PRICE_SINGLE_UNIT |
|---|---|---|---|
| 12M100L10-BG-H | 10 | 65.000000 | 6.500000 |

---

**InnoCigs Dropship-API** | Innocigs GmbH & Co. KG, Barnerstraße 14c, 22765 Hamburg | Seite 43

---

### PRODUKTE_IMAGE_ADDITIONAL

Weitere URLs zu Produktbilder, jeweils in eigenen IMAGE-Containern.

### MANUFACTURER

Hersteller

### DESCRIPTION

Artikelbeschreibung

### PRODUCTS_ATTRIBUTES

Liste der Attribute in der Form: &lt;[Attribut-Name]&gt;[Wert]&lt;/[Attribut-Name]&gt;

### VPE

Angabe zur Abfüllmenge (Nur bei Artikeln mit Abfüllmenge)

### PRODUCTS_MANUAL

Url zur Produktanleitung (PDF)

### CLP_INFOS

CLP Infos

### GRADUATED_PRICES

Staffelpreise welche ab der jeweils angegebenen Menge (QUANTITY) gelten (Ausgabe ab apiv2 und über REST-Api)

### OTHER_UNITS

Größere Verpackungseinheiten mit Preisinformationen zu Gesamtpreis und Einzelpreis
---
## Produktabfrage Master Produkte (Nur REST API)

### Aufruf REST-Api:

```
https://www.innocigs.com/restapi/products-by-master
```

### Rückgabe REST-Api:

```json
{
  "PRODUCTS-BY-MASTER": {
    "MASTER": {
      "12M100L10-BG": {
        "NAME": "Twelve Monkeys - Bonogurt - 50ml - 0mg/ml",
        "PRODUCTS": [
          {
            "CATEGORY": "Startseite B2B > Liquids > Shortfills > Twelve Monkeys",
            "MASTER": "12M100L10-BG",
            "MODEL": "12M100L10-BG-0",
            "EAN": "0827152053568",
            "NAME": "Twelve Monkeys - Bonogurt 0 mg/ml 50ml",
            "PARENT_NAME": "Twelve Monkeys - Bonogurt - 50ml - 0mg/ml",
            "PRODUCTS_PRICE": "7,51",
            "PRODUCTS_PRICE_RECOMMENDED": "16,95",
            "PRODUCTS_IMAGE": "https://cdn.innocigs.com/imgproxy/fit/sm/1500/1500/png/media/b5/45/6d/1618387425/Bonogurt-60mL-Bottle.png",
            "PRODUCTS_IMAGE_ADDITIONAL": [],
            "MANUFACTURER": "Twelve Monkeys",
            "CLP_INFOS": {
              "MSDS_CODES": null,
              "MSDS_GHS_SYMBOL": null,
              "EUH208_CONTENT": null
            },
            "PRODUCTS_ATTRIBUTES": {
              "PACKUNG": "1er Packung"
            },
            "VPE": {
              "CONTENT": 50,
              "UNIT": "ml"
            },
            "PRODUCTS_MANUAL": "",
            "GRADUATED_PRICES": {
              "GRADUATED_PRICE": [
                {
                  "QUANTITY": 10,
                  "PRODUCTS_PRICE": "7.210000"
                }
              ]
            },
            "OTHER_UNITS": {
              "OTHER_UNIT": [
                {
                  "MODEL": "12M100L10-BG-0-H",
                  "PACKUNG": "10",
                  "PRODUCTS_PRICE": "70.000000"
                }
              ]
            }
        ]
    }
}
```
---
## InnoCigs Dropship-API

### Felder:

|CATEGORY|Die bei InnoCigs zugewiesene Produktkategorie|
|---|---|
|MASTER|Artikelnummer des Masterartikels|
|MODEL|Artikelnummer|
|EAN|EAN des Artikels|
|NAME|Artikelname (incl. Attribute)|
|PARENT_NAME|Basis-Artikelname ohne Attribute|
|PRODUCTS_PRICE|Artikelpreis in Euro|
|PRODUCTS_PRICE_RECOMMENDED|Empf. Endkundenpreis in Euro|
|PRODUCTS_IMAGE|Url zum Produktbild|
|PRODUCTS_IMAGE_ADDITIONAL|Weitere URLs zu Produktbilder, jeweils in eigenen IMAGE-Containern.|
|MANUFACTURER|Hersteller|
|DESCRIPTION|Artikelbeschreibung|
|PRODUCTS_ATTRIBUTES|Liste der Attribute in der Form: &lt;[Attribut-Name]&gt;[Wert]&lt;/[Attribut-Name&gt;|
|VPE|Angabe zur Abfüllmenge (Nur bei Artikeln mit Abfüllmenge)|
|PRODUCTS_MANUAL|Url zur Produktanleitung (PDF)|
|CLP_INFOS|CLP Infos|
|GRADUATED_PRICES|Staffelpreise welche ab der jeweils angegebenen Menge (QUANTITY) gelten (Ausgabe ab apiv2 und über REST-Api)|


---
### OTHER_UNITS

Größere Verpackungseinheiten mit Preisinformationen zu Gesamtpreis und Einzelpreis

## Fehlermeldungen

Kommt es zu einen kritischen Fehler in der API wie Login fehlerhaft, wird ein XML für Fehlerfälle zurückgegeben, diese enthält alle aufgetretenen Fehler.

### Beispiel Fehlermeldung über die XML-Api:

```xml
<INNOCIGS_API_RESPONSE>
  <ERRORS>
    <ERROR>
      <CODE>10000</CODE>
      <MESSAGE>Login fehlgeschlagen</MESSAGE>
    </ERROR>
  </ERRORS>
</INNOCIGS_API_RESPONSE>
```

### Beispiel Fehlermeldung über die REST-Api:

```json
{
  "ERRORS": {
    "ERROR": [
      {
        "CODE": 10000,
        "MESSAGE": "Login fehlgeschlagen"
      }
    ]
  }
}
```

---

### Fehlercodes:

| ERROR CODE | ERROR | COMMANDS |
|---|---|---|
| 10000 | Login Fehlgeschlagen. | alle |
| 10001 | Ungültiges XML. | dropship,order |
| 10002 | Keine Dropship-Daten gefunden. | dropship |
| 10003 | Dropship-Daten unvollständig. | dropship |
| 10004 | Unbekannter API-Aufruf. | - |
| 10005,10 | Ungültiger Versender. | dropship,order |
| 10007 | Zahlung gesperrt. | dropship,order |
| 10008 | Limit für Zahlung auf Rechnung überschritten. | dropship,order |
| 20000 | XML bereits hochgeladen. | dropship,order |
| 20001 | Dropship-Daten für Dropship #X unvollständig. | dropship |
| 20002 | Absender-Daten für Dropship #X fehlen. | dropship |
| 20003 | Absender-Daten für Dropship #X unvollständig. | dropship |
| 20004 | Empfänger-Daten für Dropship #X fehlen. | dropship |
| 20005 | Empfänger-Daten für Dropship #X unvollständig. | dropship |
| 20006 | Dropship #X ohne Produkte. | dropship |
| 20007-20 | Dropship #X enthält fehlerhafte Produktdefinitionen. | dropship |
| 20010 | Dropship #X keine Bestellnummer angegeben. | dropship |
| 20011 | Dropship #X : Bestellnummer wurde von Ihnen bereits verwendet. | dropship |
| 20012 | Die jeweiligen Adressdaten enthalten Fehler. | dropship,order |
| 30000 | Keine Artikelnummer angegeben. | dropship,order |
| 30001,30 | Produkt nicht lieferbar. | dropship,order |
| 30003-30 | Produkt unbekannt. | dropship,order,quantity,product,price |
| 40001 | Es nicht genau eine Bestellung übermittelt. | order |
| 40002 | Die Kopfdaten zur Bestellung fehlen. | dropship,order |
| 40004 | Lieferadresse nicht richtig angegeben. | dropship,order |
| 40006-40007 | Bestellnummer nicht richtig angegeben | dropship,order |
| 40010-40019 | Fehler in/mit den Artikelpositionen der Bestellung | dropship,order |
| 50000 | Zu viele API-Zugriffe | alle |
| 50001 | Wartung | alle |
| 50003 | IP nicht freigeschaltet | alle |
| 50004 | Zugriff auf API nicht möglich | alle |


---

## Kontakt

**Innocigs GmbH & Co. KG**

Barnerstraße 14c  
22765 Hamburg

**E-Mail:** service@innocigs.com  
**Telefon:** +49 (0) 40 5247102 10

---