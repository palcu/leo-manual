import csv

info = ["Nume", "Obiective", "Grup țintă", "Numar de persoane", "Materiale necesare", "Resurse financiare", "Organizator", "Info Suplimentare", "Categorie", "Translator", "Data"]

content = []

page = "# Manual Leo\n\n"

with open('orig.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i += 1
        if i != 1:
            content.append([])
            for j in range(1, 12):
                content[-1].append(row[j])
            content[-1].append(row[0])

            page += '<h2 id=project"{0}">{1}</h2>\n'.format(i, row[1])
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

print(page)
