from bs4 import BeautifulSoup
import os

# Define the static part of the TEI document including the header
tei_header_content = """
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>श्रीमद्भगवद्गीता</title>
      <editor role="Digital Editor">
        <persName>Shikha Thakur</persName>
      </editor>
    </titleStmt>
    <publicationStmt>
      <p string="Published electronically by Open Source"/>
    </publicationStmt>
    <sourceDesc>
      <p string="Derived from https://sanskritdocuments.org/doc_giitaa/bhagvadnew.html"/>
    </sourceDesc>
  </fileDesc>
</teiHeader>
"""
# Start building the TEI document
tei = f'<?xml version="1.0" encoding="utf-8"?>\n<TEI xmlns="http://www.tei-c.org/ns/1.0">{tei_header_content}<text xml:lang="sa-Deva"><body>'

# Directory containing the XML files
directory = '/Users/shikha/Desktop/Bhagvat Gita/BhagvatGita'

# Filter and sort the XML files
files = [f for f in os.listdir(directory) if f.startswith('chapter') and f.endswith('.xml')]
files.sort(key=lambda x: int(x.replace('chapter', '').replace('.xml', '')))

# Append each chapter to the TEI body
for filename in files:
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        chapter_content = file.read()
    # Create a soup object for each chapter and extract the <div>
    chapter_soup = BeautifulSoup(chapter_content, "xml")
    chapter_div = chapter_soup.find('div', {'type': 'chapter'})
    if chapter_div:
        tei += chapter_div.prettify()

# Close the TEI body and text tags
tei += '</body></text></TEI>'

# Parse the final TEI string to prettify and save
soup = BeautifulSoup(tei, "xml")
with open('combined_BhagavadGita.xml', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
