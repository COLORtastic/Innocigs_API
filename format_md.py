#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Formatiert die Dropship-API Dokumentation für bessere Lesbarkeit
"""

import re

def format_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ersetze alte Überschriften (# InnoCigs Dropship-API) mit konsistenten Seitenkopfzeilen
    content = re.sub(
        r'# InnoCigs Dropship-API\n\nInnocigs GmbH & Co\. KG, Barnerstraße 14c, 22765 Hamburg\n\nSeite: (\d+)',
        r'---\n\n**InnoCigs Dropship-API** | Innocigs GmbH & Co. KG, Barnerstraße 14c, 22765 Hamburg | Seite \1\n\n---',
        content
    )
    
    # Ersetze HTML Entities in Code-Blöcken
    # Finde alle Bereiche die mit &lt; beginnen und XML/JSON enthalten
    def replace_xml_entities(match):
        text = match.group(0)
        if '&lt;' in text and '&gt;' in text:
            # Prüfe ob es ein XML-ähnlicher Block ist
            lines = text.split('\n')
            if any('&lt;' in line and '&gt;' in line for line in lines[:5]):
                # Ersetze Entities und füge Code-Block hinzu
                text = text.replace('&lt;', '<')
                text = text.replace('&gt;', '>')
                text = text.replace('&amp;', '&')
                # Wenn noch nicht in Code-Block, füge hinzu
                if not text.startswith('```'):
                    text = '```xml\n' + text + '\n```'
        return text
    
    # Formatiere unformatierte XML-Responses
    content = re.sub(
        r'(# Rückgabe XML-Api:\n\n)(&lt;[^`]+?&lt;/INNOCIGS_API_RESPONSE&gt;)',
        lambda m: m.group(1) + '```xml\n' + m.group(2).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&') + '\n```',
        content,
        flags=re.DOTALL
    )
    
    # Formatiere unformatierte JSON-Responses
    content = re.sub(
        r'(# Rückgabe REST-Api:\n\n)(\{\n"[^`]+?\n\})',
        lambda m: m.group(1) + '```json\n' + m.group(2) + '\n```',
        content,
        flags=re.DOTALL
    )
    
    # Ersetze # Überschriften die keine Hauptüberschriften sind
    # Parameter, Aufruf, Rückgabe, Felder sollten ### sein
    content = re.sub(r'\n# (Parameter|Aufruf|Rückgabe|Felder|Beispiel):', r'\n### \1:', content)
    content = re.sub(r'\n# (Aufruf XML-Api|Aufruf REST-Api|Rückgabe XML-Api|Rückgabe REST-Api):', r'\n### \1:', content)
    
    # URLs in Code-Blöcke wenn sie noch nicht drin sind
    content = re.sub(
        r'\n(https://www\.innocigs\.com/[^\n]+)\n',
        lambda m: '\n```\n' + m.group(1) + '\n```\n' if not re.search(r'```[^`]*' + re.escape(m.group(1)), content[:m.start()]) else m.group(0),
        content
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Formatierung abgeschlossen: {output_file}")

if __name__ == "__main__":
    input_file = "Dropship-API Dokumentation Händler.md"
    output_file = "Dropship-API Dokumentation Händler_formatted.md"
    format_markdown(input_file, output_file)
