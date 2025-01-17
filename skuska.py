import tkinter as tk
from tkinter import ttk
import urllib.request
import xml.etree.ElementTree as et

URL = "https://mikrotik.com/download.rss"
VERSIONS = {}


# zoberie rss z URL a spracuje ho do dictionary {verzia: popis}
def parse():
    resp = urllib.request.urlopen(URL).read()
    rss = et.fromstring(resp)

    # toto je tag ktory je namiesto description
    replace = "{http://purl.org/rss/1.0/modules/content/}encoded"

    # prechadza vsetko kde je tag "item"
    for item in rss.findall("./channel/item"):
        if item.find("title") is not None:
            title = item.find("title").text
        else:
            title = "Not available"

        desc_tag = item.find(replace)

        if desc_tag is not None:
            desc = desc_tag.text
        else:
            desc = "Not available"

        VERSIONS[title] = desc.replace("<br>", "\n")


# ked sa klikne hodnota z comboboxu
def click(e):
    selected = combo.get()
    # print(f"selected version: {selected}")
    text_label.config(text=VERSIONS[selected])


if __name__ == "__main__":
    # vytvorenie okna
    window = tk.Tk()
    window.title("MikroTik")
    window.geometry("720x720")

    # pomocny element
    wrapper = tk.Frame(window)
    wrapper.grid(row=0, column=0)

    title = tk.Label(wrapper, text="Verzia")
    title.grid(row=0, column=0, padx=4, pady=4)

    combo = ttk.Combobox(wrapper, width=64)
    combo.grid(row=0, column=1)
    combo.bind("<<ComboboxSelected>>", click)

    # hlavne textove pole
    text_label = tk.Label(window, wraplength=500)
    text_label.grid(row=1, column=0)
    # TODO scrollovatelne

    parse()
    combo["values"] = list(VERSIONS.keys())

    window.mainloop()
