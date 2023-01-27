json_data = {
    "medtronicII-WS01_02_fe_01_22-05-05_08-24-57.xls": {
        "Praeparat": "WS01",
        "Datum": "22-05-05",
        "Uhrzeit": "08-24-57",
        "Bewegung": "fe",
        "Zustandsnummer_IST": "1",
        "Zustand_IST": "Fusion_Th6-S1__CR",
        "use": "yes",
        "problem?": "no!",
        "Kommentar": "",
        "Sonstiges": ""
    },
}

print(json_data["medtronicII-WS01_02_fe_01_22-05-05_08-24-57.xls"]["Praeparat"])