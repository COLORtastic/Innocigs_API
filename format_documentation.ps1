# PowerShell Script to format the Dropship API documentation
$inputFile = "e:\00001_SELLX\02_Fimpler\Dropship-API Dokumentation Händler.md"
$outputFile = "e:\00001_SELLX\02_Fimpler\Dropship-API Dokumentation Händler_neu.md"

# Read the entire file
$content = Get-Content -Path $inputFile -Raw -Encoding UTF8

# Replace old page headers
$content = $content -replace '# InnoCigs Dropship-API\r?\n\r?\nInnocigs GmbH & Co\. KG, Barnerstraße 14c, 22765 Hamburg\r?\n\r?\nSeite: (\d+)', "`n---`n`n**InnoCigs Dropship-API** | Innocigs GmbH & Co. KG, Barnerstraße 14c, 22765 Hamburg | Seite `$1`n`n---"

# Replace # Headers that should be ###
$content = $content -replace '\r?\n# (Parameter|Aufruf|Rückgabe|Felder|Beispiel):', "`n### `$1:"
$content = $content -replace '\r?\n# (REST-Api|XML-Api)', "`n### `$1"

# Replace HTML entities in XML code blocks
$content = $content -replace '&lt;', '<'
$content = $content -replace '&gt;', '>'
$content = $content -replace '&amp;', '&'

# Wrap URLs in code blocks if not already
$content = $content -replace '(?<!```)\r?\n(https://www\.innocigs\.com/[^\r\n]+)\r?\n(?!```)', "`n``````n`$1`n``````n"

# Write the formatted content
Set-Content -Path $outputFile -Value $content -Encoding UTF8 -NoNewline

Write-Host "Formatierung abgeschlossen! Neue Datei: $outputFile"
Write-Host "Bitte überprüfen und dann die alte Datei ersetzen falls OK."
