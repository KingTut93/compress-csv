import csv

# Datei, die gelesen werden soll
file_in = "f_in.csv"
# Datei, in die geschrieben wird
file_out = "output2.csv"

# Lesen der CSV-Datei
with open(file_in, "r", encoding="utf-8") as f_in:
    reader = csv.reader(f_in, delimiter=";")
    data = list(reader)

# Entfernen der leeren Zeilen
data = [row for row in data if row[0] != ""]

# Schreiben in die Ausgabedatei
with open(file_out, "w", encoding="utf-8", newline="") as f_out:
    writer = csv.writer(f_out, delimiter=";")
    for row in data:
        writer.writerow(row)
