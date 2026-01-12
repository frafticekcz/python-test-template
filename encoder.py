# -*- coding: utf-8 -*-
"""
Module containing the Encoder class for encoding/decoding messages.

IMPORTANT: Check your ASSIGNMENT.md file for your specific cipher type and parameters!
"""

from message import Message


# Dictionary for converting Czech diacritics to base letters
DIACRITICS_MAP = {
    'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i',
    'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u',
    'ů': 'u', 'ý': 'y', 'ž': 'z',
    'Á': 'A', 'Č': 'C', 'Ď': 'D', 'É': 'E', 'Ě': 'E', 'Í': 'I',
    'Ň': 'N', 'Ó': 'O', 'Ř': 'R', 'Š': 'S', 'Ť': 'T', 'Ú': 'U',
    'Ů': 'U', 'Ý': 'Y', 'Ž': 'Z'
}


class Encoder:
    """
    Class for encoding and decoding messages using a specific cipher.
    
    The cipher type and parameters are defined in ASSIGNMENT.md.
    Modify __init__ according to your assignment (shift, key, etc.)
    """
    
    def __init__(self, **kwargs):
        """
        Initialize the encoder with cipher parameters.
        
        Depending on your assignment, you might receive:
        - shift (int): For Caesar cipher, e.g., shift=3 or shift=-5
        - key (str): For Vigenere cipher, e.g., key="KOD"
        - cipher_type (str): For Atbash, e.g., cipher_type="atbash"
        
        TODO: Store the parameters you need for your cipher
        Example for Caesar:
            self.shift = kwargs.get('shift', 0)
        Example for Vigenere:
            self.key = kwargs.get('key', '').upper()
        """
        # TODO: Initialize your cipher parameters based on your ASSIGNMENT.md
        pass
    
    def _remove_diacritics(self, text: str) -> str:
        """
        Remove Czech diacritics from text.
        
        Args:
            text: Input text possibly containing diacritics
            
        Returns:
            Text with diacritics replaced by base letters
            
        Example:
            "Příliš žluťoučký" -> "Prilis zlutoucky"
        """
        # TODO: Implement diacritics removal using DIACRITICS_MAP
        # Hint: Iterate through each character and replace if in map
        pass
    
    def _transform_char(self, char: str, reverse: bool = False) -> str:
        """
        Transform a single character using the cipher algorithm.
        
        Args:
            char: Single character to transform
            reverse: If True, decode instead of encode
            
        Returns:
            Transformed character
            
        TODO: Implement according to your specific cipher type!
        
        For Caesar cipher (shift=N):
            - Encoding: shift forward by N
            - Decoding: shift backward by N (or forward by -N)
            
        For Atbash:
            - Both encoding and decoding: mirror the alphabet (A<->Z, B<->Y, ...)
            
        For Vigenere:
            - This method might need additional parameter for key position
            - Consider using a different approach (see encode method)
        """
        # TODO: Implement character transformation for your cipher
        # Remember:
        # - Only transform letters (a-z, A-Z)
        # - Preserve case (lowercase -> lowercase, uppercase -> uppercase)
        # - Return other characters unchanged
        pass
    
    def encode(self, message: Message) -> Message:
        """
        Encode the message using the cipher.
        
        Args:
            message: Message object to encode
            
        Returns:
            New Message object with encoded text
            
        Steps:
        1. Get the original text from message
        2. Remove diacritics
        3. Transform each character
        4. Create and return new Message with encoded text
        """
        # TODO: Implement encoding
        # 1. Get text: text = message.original_text
        # 2. Remove diacritics: text = self._remove_diacritics(text)
        # 3. Transform each character (handle Vigenere's key cycling if needed)
        # 4. Create result message with is_encoded=True
        pass
    
    def decode(self, message: Message) -> Message:
        """
        Decode the message using the cipher.
        
        Args:
            message: Message object to decode
            
        Returns:
            New Message object with decoded text
            
        Note: For Atbash, this is identical to encode (symmetric cipher)
        """
        # TODO: Implement decoding
        # Similar to encode, but with reverse=True for _transform_char
        # Or for Atbash, just call encode
        pass
    
    def get_cipher_info(self) -> str:
        """
        Return information about the cipher configuration.
        
        Returns:
            String describing the cipher type and parameters
            
        Example outputs:
            "Caesarova šifra (posun: +3)"
            "Atbaš (zrcadlová šifra)"
            "Vigenerova šifra (klíč: KOD)"
        """
        # TODO: Return description of your cipher
        pass


# Test code
if __name__ == "__main__":
    # Example for Caesar cipher with shift=3
    # Modify according to your assignment!
    
    encoder = Encoder(shift=3)  # Change parameters based on your ASSIGNMENT.md
    
    # Test encoding
    msg = Message("Ahoj svete!")
    encoded = encoder.encode(msg)
    print(f"Původní: {msg.original_text}")
    print(f"Zakódováno: {encoded.processed_text}")
    
    # Test decoding
    decoded = encoder.decode(encoded)
    print(f"Dekódováno: {decoded.processed_text}")
    
    # Test with diacritics
    msg2 = Message("Příliš žluťoučký kůň")
    encoded2 = encoder.encode(msg2)
    print(f"\nS diakritikou: {msg2.original_text}")
    print(f"Zakódováno: {encoded2.processed_text}")
