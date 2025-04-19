import os
import csv
import shutil
import sys
import argparse

# Percorso della cartella contenente i file
cartella_files = r'C:\Work\Lavoro\Start2impact\FileOrganizer\FileOrganizer\files'

# Percorso delle sottocartelle per i diversi tipi di file
sottocartella_documenti = os.path.join(cartella_files, 'docs')
sottocartella_audio = os.path.join(cartella_files, 'audio')
sottocartella_immagini = os.path.join(cartella_files, 'images')

# Crea le sottocartelle se non esistono
os.makedirs(sottocartella_documenti, exist_ok=True)
os.makedirs(sottocartella_audio, exist_ok=True)
os.makedirs(sottocartella_immagini, exist_ok=True)

# Lista delle estensioni di file supportate per ogni tipo di file
estensioni_documenti = {'.txt', '.odt'}
estensioni_audio = {'.mp3', '.wav'}
estensioni_immagini = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

# Funzione per aggiornare il file CSV
def aggiorna_csv(nome_file, tipo_file, dimensione_file):
    # Aggiungi le informazioni al file recap.csv
    with open(os.path.join(cartella_files, 'recap.csv'), 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome_file, f"type:{tipo_file}", f"size:{dimensione_file}B"])


# Funzione principale per spostare il file e aggiornare il recap
def sposta_file(nome_file):
    percorso_completo = os.path.join(cartella_files, nome_file)
    if not os.path.isfile(percorso_completo):
        print(f"Errore: il file '{nome_file}' non esiste nella cartella files.")
        return

    # Ottieni la dimensione del file in byte
    dimensione_file = os.path.getsize(percorso_completo)
    # Ottieni l'estensione del file
    _, estensione_file = os.path.splitext(nome_file)

    # Determina la sottocartella di destinazione
    if estensione_file in estensioni_documenti:
        sottocartella_destinazione = sottocartella_documenti
        tipo_file = "doc"
    elif estensione_file in estensioni_audio:
        sottocartella_destinazione = sottocartella_audio
        tipo_file = "audio"
    elif estensione_file in estensioni_immagini:
        sottocartella_destinazione = sottocartella_immagini
        tipo_file = "image"
    else:
        print(f"Errore: il tipo di file '{estensione_file}' non è supportato.")
        return

    # Sposta il file nella sottocartella di destinazione
    shutil.move(percorso_completo, os.path.join(sottocartella_destinazione, nome_file))

    # Aggiorna il file CSV
    aggiorna_csv(nome_file, tipo_file, dimensione_file)
    print(f"File '{nome_file}' spostato nella cartella '{sottocartella_destinazione}' e CSV aggiornato.")


# Funzione per impostare e parsare gli argomenti della linea di comando
def main():
    parser = argparse.ArgumentParser(
        description="Sposta un file nella sottocartella appropriata e aggiorna il recap.csv.")
    parser.add_argument('nome_file', type=str, help="Il nome del file da spostare (es: 'trump.jpeg')")

    args = parser.parse_args()
    sposta_file(args.nome_file)


if __name__ == "__main__":
    main()
