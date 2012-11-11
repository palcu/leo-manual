import csv

page = '<html><head><meta charset="utf-8"></head><body>\n'
page += "# Manual Leo\n"


with open('orig.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i += 1
        if i != 1:
            page += '<h2 id=project"{0}">{1}</h2>\n'.format(i, row[1])
            page += row[2] + '\n'
            page += '\n'
            page += "### Obiective\n"
            page += row[3] + "\n"
            page += "### Grup tinta\n"
            page += row[4] + "\n"
            page += "### Numar de persoane\n"
            page += row[5] + "\n"
            page += "### Materiale necesare\n"
            page += row[6] + "\n"
            page += "### Resurse financiare\n"
            page += row[7] + "\n"
            page += "### Organizator\n"
            page += row[8] + "\n"
            page += "### Info Suplimentare\n"
            page += row[9] + "\n"
            page += "### Categorie\n"
            page += row[10] + "\n"
            page += "### Translator\n"
            page += row[11] + "\n"
            page += "### Data\n"
            page += row[0] + "\n"
page += '</body></html>'
print(page)
