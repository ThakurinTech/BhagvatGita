from bs4 import BeautifulSoup
import os

def combine_xml_files(directory, output_file):
    # Initialize a new BeautifulSoup object for the combined XML with a header
    soup = BeautifulSoup('<?xml version="1.0" encoding="UTF-8"?><TEI xmlns="http://www.tei-c.org/ns/1.0"></TEI>', 'xml')
    tei = soup.find('TEI')

    # Create TEI Header
    tei_header = soup.new_tag('teiHeader')
    tei.append(tei_header)

    # File description
    file_desc = soup.new_tag('fileDesc')
    tei_header.append(file_desc)

    # Title statement with editor name
    title_stmt = soup.new_tag('titleStmt')
    file_desc.append(title_stmt)
    
    title = soup.new_tag('title')
    title['string'] = "Bhagavad Gita"
    title_stmt.append(title)
    
    editor = soup.new_tag('editor')
    editor['string'] = "Your Editor's Name"  # Replace with the actual editor's name
    title_stmt.append(editor)

    # Publication statement
    publication_stmt = soup.new_tag('publicationStmt')
    p_pub = soup.new_tag('p')
    p_pub['string'] = "Published electronically"
    publication_stmt.append(p_pub)
    file_desc.append(publication_stmt)

    # Source description
    source_desc = soup.new_tag('sourceDesc')
    p_source = soup.new_tag('p')
    p_source['string'] = "Derived from historical sources"
    source_desc.append(p_source)
    file_desc.append(source_desc)

    # Text and body elements to contain the chapters
    text = soup.new_tag('text', attrs={"xml:lang": "sa-Deva"})
    tei.append(text)
    body = soup.new_tag('body')
    text.append(body)

    # List all XML files, filtering non-XML and incorrect files
    files = [f for f in os.listdir(directory) if f.startswith('chapter') and f.endswith('.xml')]
    files.sort(key=lambda x: int(x.replace('chapter', '').replace('.xml', '')))

    # Loop through all XML files in the sorted list
    for filename in files:
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Open and read each XML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            chapter_soup = BeautifulSoup(content, 'xml')

            # Find the <div> tag representing the chapter
            chapter = chapter_soup.find('div', {'type': 'chapter'})

            # Append the chapter to the body element of the main soup object
            body.append(chapter)

    # Write the combined XML to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

# Specify the directory containing your XML files and the name of the output file
combine_xml_files('/Users/shikha/Desktop/Bhagvat Gita/BhagvatGita', 'combined_BhagavadGita2.xml')
