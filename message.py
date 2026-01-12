# -*- coding: utf-8 -*-
"""
Module containing the Message class for representing text messages.
"""

from datetime import datetime
from collections import Counter


class Message:
    """
    Class representing a text message with encoding capabilities.
    
    Attributes:
        original_text (str): The original input text
        processed_text (str): The encoded/decoded text
        is_encoded (bool): True if the message is currently encoded
        created_at (str): Timestamp of message creation
    """
    
    def __init__(self, text: str, is_encoded: bool = False):
        """
        Initialize a new message.
        
        Args:
            text: The message text
            is_encoded: Whether the text is already encoded
        """
        # TODO: Initialize the attributes
        # - original_text: store the input text
        # - processed_text: initially empty string or same as original
        # - is_encoded: store the encoded status
        # - created_at: current timestamp in format "DD.MM.YYYY HH:MM"
        pass
    
    def __str__(self) -> str:
        """
        Return a string representation of the message.
        
        Returns:
            Formatted string with message info
            
        Example output:
            "[Zašifrováno] Text: DKRM VYHWH | Vytvořeno: 12.01.2026 14:30"
            "[Originál] Text: Ahoj svete | Vytvořeno: 12.01.2026 14:30"
        """
        # TODO: Implement string representation
        # - Show status [Zašifrováno] or [Originál]
        # - Show the processed_text (or original_text if not processed)
        # - Show creation timestamp
        pass
    
    def get_stats(self) -> str:
        """
        Return statistics about the message text.
        
        Analyzes the original_text and returns:
        - Total character count
        - Word count
        - Most frequent letter (case-insensitive)
        
        Returns:
            Formatted string with statistics
            
        Example output:
            "=== STATISTIKY ===
            Počet znaků: 11
            Počet slov: 2
            Nejčastější písmeno: e (3x)"
        """
        # TODO: Implement statistics calculation
        # Hints:
        # - Use len() for character count
        # - Use split() for word count
        # - Use collections.Counter for letter frequency
        pass
    
    def set_processed(self, text: str, encoded: bool):
        """
        Set the processed text and encoding status.
        
        Args:
            text: The processed (encoded/decoded) text
            encoded: Whether the text is now encoded
        """
        # TODO: Update processed_text and is_encoded
        pass


# Test code - runs only when this file is executed directly
if __name__ == "__main__":
    # Test message creation
    msg = Message("Ahoj svete!")
    print(msg)
    print(msg.get_stats())
    
    # Test processed text
    msg.set_processed("DKRM VYHWH!", True)
    print(msg)
