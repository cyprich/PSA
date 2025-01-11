import urllib.request  # stahovanie
import xml.etree.ElementTree as ET  # parsovanie xml
import tkinter as tk


def get_rss(paURL: str):
    returnText = ""
    page = urllib.request.urlopen(paURL).read()
    root = ET.fromstring(page)

    for channel in root:
        for item in channel:
            if item.tag == "title":
                returnText += f"Nadpis kanala: {item.text}\n"
            elif item.tag == "description":
                returnText += f"Popis kanala: {item.text}\n"
            elif item.tag == "item":
                for i in item:
                    if i.tag == "title":
                        returnText += f"\tNadpis itemu: {i.text}\n"
                    if i.tag == "description":
                        returnText += f"\tPopis itemu: {i.text}\n"
                    if i.tag == "pubDate":
                        # returnText += f"\tDatum itemu: {i.text}\n"
                        pass
                    if i.tag == "link":
                        returnText += f"\tLink: {i.text}\n"
                returnText += "\n\n"

    return returnText


def nastavOkno(okno: tk.Tk):
    okno.title("RSS citacka")
    okno.geometry("800x600")
    okno.resizable(True, True)

    labelURL = tk.Label(okno, text="URL: ")
    labelURL.grid(row=0, column=0, padx=20, sticky="w")  # sticky=west = dolava

    entryURL = tk.Entry(okno)
    entryURL.grid(row=1, column=0, padx=20, ipadx=240)

    outputText = tk.Text(okno)
    outputText.grid(row=2, column=0)

    gombik = tk.Button(
        okno,
        text="Davaj!",
        command=lambda: outputText.insert(tk.END, get_rss(entryURL.get())),
    )
    gombik.grid(row=1, column=1)

    entryURL.insert(0, "https://www.bazos.sk/rss.php")

    return True


# print(get_rss("https://www.bazos.sk/rss.php"))


if __name__ == "__main__":
    okno = tk.Tk()
    nastavOkno(okno)
    okno.mainloop()
