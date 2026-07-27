# Project 2: Caesar Cipher (Encryption & Decryption)

DecodeLabs Cyber Security Internship, Industrial Training Kit, Batch 2026

## What this does

A simple command line program that takes a message, encrypts it using a Caesar cipher, and then decrypts it back to check everything worked. The Caesar cipher is one of the oldest encryption techniques, it just shifts each letter forward by a certain number of positions.

For example, with a shift of 3, A becomes D, B becomes E, and so on. Once you go past Z it wraps back around to A again (that's what the modulo math is doing).

Decryption is just the same shift applied backwards.

Formulas:
Encrypt: (x + shift) % 26
Decrypt: (x - shift) % 26

## Features

* Encrypts text using any shift key you enter
* Decrypts it right after, so you can confirm it matches the original
* Spaces, punctuation, and numbers are left alone, only letters get shifted
* Works with both uppercase and lowercase
* If you type something that's not a number for the shift key, it asks again instead of crashing
* Prints a quick check at the end confirming the decrypted text matches what you typed in

## How to run it

```
python caesar_cipher.py
```

It'll ask for your text and a shift number, then show you the result.

### Example run

```
Enter the text you want to encrypt: Hello, World!
Enter a shift key (whole number, e.g. 3): 3

Original text  : Hello, World!
Shift key      : 3
Encrypted text : Khoor, Zruog!
Decrypted text : Hello, World!

Verification: decrypted text matches the original. Success!
```

## What I learned / practiced

* Converting letters to numbers and back using ord() and chr()
* Using modulo to handle wraparound at the end of the alphabet
* Basic input validation with try/except
* Why encryption and decryption can use the exact same key (symmetric encryption)

## Note on security

This cipher isn't actually secure, there are only 25 possible shift keys so it can be brute forced almost instantly,and it doesn't hide letter frequency patterns either. It's meant as a stepping stone ,to actually have an idea why it is weak before learning real encryption methods like AES.

## Built with

Python 3, no external libraries.