import os

import openai
import time
import random

openai.api_key = '...'
conversazione = []

def genera_risposta(conversazione):
    # Invio richiesta
    response = openai.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=conversazione,
        max_tokens=500,
        n=1,
        temperature=0.7
    )
    # Risposta di chatGPT
    risposta = response.choices[0].message.content
    return risposta

def save_to_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w", encoding="utf-8") as f:
        for entry in conversazione:
            f.write(f"{entry['role']}: {entry['content']}\n")

def log_conversation(sender, message):
    entry= ({
        "role": sender,
        "content": message
    })
    conversazione.append(entry)
    save_to_file("conversazione.txt")

def comunica():

    print("Benvenuto! Ora puoi iniziare la conversazione. Digita 'esci' per terminare la conversazione.")

    while True:
        messaggio_utente = input(" ")+" comportati e rispondi come se fossi un terapeuta umano. le risposte non devono superare 5 righe"

        if messaggio_utente.lower() == "esci":
            print("Conversazione terminata.")
            break

        # Aggiungi il messaggio dell'utente alla conversazione (lista)
        log_conversation("user", messaggio_utente)

        time.sleep(random.randint(45, 60))

        risposta = genera_risposta(conversazione)

        # Aggiungi la risposta di ChatGPT alla conversazione
        log_conversation("assistant", risposta)

        print("Messaggio Ricevuto:", risposta)

comunica()