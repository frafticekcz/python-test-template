# -*- coding: utf-8 -*-
"""
Main program - Message Encoder
Interactive console application for encoding and decoding messages.

Check ASSIGNMENT.md for your specific cipher configuration!
"""

from message import Message
from encoder import Encoder


def display_menu(cipher_info: str):
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("       ŠIFROVAČ ZPRÁV (Message Encoder)")
    print("=" * 50)
    print(f"Typ šifry: {cipher_info}")
    print("-" * 50)
    print("1. Zadat novou zprávu")
    print("2. Zašifrovat zprávu")
    print("3. Dešifrovat zprávu")
    print("4. Zobrazit statistiky")
    print("5. Historie zpráv")
    print("6. Konec")
    print("-" * 50)


def input_message() -> Message:
    """
    Get a new message from user input.
    
    Returns:
        New Message object with user's text
    """
    # TODO: Implement message input
    # 1. Prompt user for text
    # 2. Create and return Message object
    pass


def encode_message(encoder: Encoder, message: Message) -> Message:
    """
    Encode a message and display results.
    
    Args:
        encoder: Encoder instance
        message: Message to encode
        
    Returns:
        Encoded Message object
    """
    # TODO: Implement encoding
    # 1. Check if message exists
    # 2. Call encoder.encode()
    # 3. Display original and encoded text
    # 4. Return encoded message
    pass


def decode_message(encoder: Encoder, message: Message) -> Message:
    """
    Decode a message and display results.
    
    Args:
        encoder: Encoder instance  
        message: Message to decode
        
    Returns:
        Decoded Message object
    """
    # TODO: Implement decoding
    # Similar to encode_message but with decode
    pass


def show_statistics(message: Message):
    """
    Display message statistics.
    
    Args:
        message: Message to analyze
    """
    # TODO: Implement statistics display
    # 1. Check if message exists
    # 2. Call message.get_stats() and print result
    pass


def show_history(history: list):
    """
    Display message history.
    
    Args:
        history: List of Message objects
    """
    # TODO: Implement history display
    # 1. Check if history is empty
    # 2. Iterate and print each message
    pass


def main_loop():
    """Main program loop."""
    
    # TODO: Initialize your encoder with correct parameters from ASSIGNMENT.md
    # Examples:
    # encoder = Encoder(shift=3)          # For Caesar +3
    # encoder = Encoder(shift=-5)         # For Caesar -5
    # encoder = Encoder()                 # For Atbash
    # encoder = Encoder(key="KOD")        # For Vigenere
    
    encoder = Encoder()  # CHANGE THIS according to your assignment!
    
    current_message = None
    history = []  # Bonus: store message history
    
    while True:
        display_menu(encoder.get_cipher_info())
        
        choice = input("Volba: ").strip()
        
        if choice == "1":
            current_message = input_message()
            if current_message:
                history.append(current_message)
                print("\n✓ Zpráva uložena.")
                
        elif choice == "2":
            if current_message is None:
                print("\n⚠ Nejprve zadejte zprávu!")
            else:
                encoded = encode_message(encoder, current_message)
                if encoded:
                    history.append(encoded)
                    current_message = encoded
                    
        elif choice == "3":
            if current_message is None:
                print("\n⚠ Nejprve zadejte zprávu!")
            else:
                decoded = decode_message(encoder, current_message)
                if decoded:
                    history.append(decoded)
                    current_message = decoded
                    
        elif choice == "4":
            if current_message is None:
                print("\n⚠ Nejprve zadejte zprávu!")
            else:
                show_statistics(current_message)
                
        elif choice == "5":
            show_history(history)
            
        elif choice == "6":
            print("\nDěkujeme za použití aplikace. Nashledanou!")
            break
            
        else:
            print("\n⚠ Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main_loop()
