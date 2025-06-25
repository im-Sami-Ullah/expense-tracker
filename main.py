import csv
import os

FILE_SPESE = "spese.csv"

def mostra_menu():
    print("\nGESTIONALE SPESE PERSONALI")
    print("1. Aggiungi spesa")
    print("2. Visualizza spese")
    print("3. Modifica spesa")
    print("4. Elimina spesa")
    print("5. Esci")

def aggiungi_spesa():
    data = input("Inserisci la data (gg/mm/aaaa): ")
    categoria = input("Inserisci la categoria (es. Cibo, Trasporti): ")
    descrizione = input("Descrizione della spesa: ")
    importo = input("Importo (€): ")
    with open(FILE_SPESE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, categoria, descrizione, importo])
    print("✅ Spesa aggiunta correttamente.")

def visualizza_spese():
    if not os.path.exists(FILE_SPESE):
        print("⚠️ Nessuna spesa trovata.")
        return
    with open(FILE_SPESE, mode='r') as file:
        reader = csv.reader(file)
        print("\n--- Elenco Spese ---")
        for idx, riga in enumerate(reader, 1):
            print(f"{idx}. Data: {riga[0]}, Categoria: {riga[1]}, Descrizione: {riga[2]}, Importo: {riga[3]}€")

def modifica_spesa():
    visualizza_spese()
    try:
        num = int(input("\nNumero della spesa da modificare: "))
    except ValueError:
        print("⚠️ Inserisci un numero valido.")
        return
    righe = []
    with open(FILE_SPESE, mode='r') as file:
        righe = list(csv.reader(file))
    if num < 1 or num > len(righe):
        print("⚠️ Numero non valido.")
        return
    print("Inserisci i nuovi dati:")
    data = input("Nuova data: ")
    categoria = input("Nuova categoria: ")
    descrizione = input("Nuova descrizione: ")
    importo = input("Nuovo importo: ")
    righe[num - 1] = [data, categoria, descrizione, importo]
    with open(FILE_SPESE, mode='w', newline='') as file:
        csv.writer(file).writerows(righe)
    print("✅ Spesa modificata con successo.")

def elimina_spesa():
    visualizza_spese()
    try:
        num = int(input("\nNumero della spesa da eliminare: "))
    except ValueError:
        print("⚠️ Inserisci un numero valido.")
        return
    righe = []
    with open(FILE_SPESE, mode='r') as file:
        righe = list(csv.reader(file))
    if num < 1 or num > len(righe):
        print("⚠️ Numero non valido.")
        return
    righe.pop(num - 1)
    with open(FILE_SPESE, mode='w', newline='') as file:
        csv.writer(file).writerows(righe)
    print("🗑️ Spesa eliminata.")

def main():
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-5): ")
        if scelta == '1':
            aggiungi_spesa()
        elif scelta == '2':
            visualizza_spese()
        elif scelta == '3':
            modifica_spesa()
        elif scelta == '4':
            elimina_spesa()
        elif scelta == '5':
            print("👋 Uscita dal programma.")
            break
        else:
            print("⚠️ Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
