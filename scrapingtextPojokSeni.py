import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.pojokseni.com/search/label/Estetika?&max-results=10"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

Artikel_Estetika = soup.find_all("h2", class_="post-title entry-title")

with open("Artikel_Estetika.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Judul", "Tanggal", "Jenis "])

    for analisis in Artikel_Estetika:
        title = analisis.a.text

        tanggal_rilis = analisis.find_next("span", class_="date-header")
        date = tanggal_rilis.script.text if tanggal_rilis.script else "N/A"

        Jenis_Artikel= analisis.find_next("span", class_="post-labels")
        Jenis = Jenis_Artikel.span.text if Jenis_Artikel.span else "N/A"


        writer.writerow([title, date, Jenis])

print("Data Tersimpan di CSV")