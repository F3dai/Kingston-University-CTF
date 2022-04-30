import random
from pytimedinput import timedInput
import hashlib

answer = None

def generate_sentence():
	adj = ("Depressed", "Stinky", "Dirty", "Sexy", "Stupid")
	nouns = ("chimpanzee", "orangutan", "gorilla", "ape", "monkey")
	verbs = ("runs", "smokes", "screams", "drives", "dies")
	adv = ("suspiciously.", "seductively.", "quitely.", "happily.", "intimidatingly.")

	return f"{adj[random.randrange(0,5)]} {nouns[random.randrange(0,5)]} {verbs[random.randrange(0,5)]} {adv[random.randrange(0,5)]}"

def generate_hash(plaintext):
	hash = hashlib.sha512( plaintext.encode("utf-8") ).hexdigest()
	return hash


plaintext = generate_sentence()
ciphertext = generate_hash(plaintext)

userText, timedOut = timedInput(plaintext + "\n", timeout=2)
if(timedOut):
    print("I haven't got all day.")
else:
    if userText == ciphertext:
    	print("kucss{m0nkey_lik3s_haSh}")
    else:
    	print("wrong")
