# -*- coding: utf-8 -*-
"""
Automated tests for Message Encoder project.

IMPORTANT: These tests are configured based on your ASSIGNMENT.md
The test configuration is loaded from tests/config.json

To run tests locally:
    python -m pytest tests/test_encoder.py -v
"""

import sys
import os
import json
import pytest

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from message import Message
from encoder import Encoder, DIACRITICS_MAP


# Load test configuration (will be set per student in GitHub Classroom)
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def load_config():
    """Load test configuration from config.json."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Default config for local testing (Caesar +3)
    return {
        "cipher_type": "caesar",
        "params": {"shift": 3},
        "test_cases": {
            "encode_basic": {"input": "AHOJ", "expected": "DKRM"},
            "encode_lower": {"input": "ahoj", "expected": "dkrm"},
            "encode_mixed": {"input": "Ahoj Svete!", "expected": "Dkrm Vyhwh!"},
            "encode_diacritics": {"input": "Příliš", "expected": "Sulolv"},
            "decode_basic": {"input": "DKRM", "expected": "AHOJ"}
        }
    }

CONFIG = load_config()


def get_encoder():
    """Create encoder with configured parameters."""
    return Encoder(**CONFIG.get("params", {}))


class TestMessage:
    """Tests for the Message class."""
    
    def test_message_creation(self):
        """Test creating a new message."""
        msg = Message("Test message")
        assert msg.original_text == "Test message"
        assert msg.is_encoded == False
        assert msg.created_at is not None
    
    def test_message_creation_encoded(self):
        """Test creating an encoded message."""
        msg = Message("ENCODED", is_encoded=True)
        assert msg.is_encoded == True
    
    def test_message_str(self):
        """Test string representation."""
        msg = Message("Test")
        text = str(msg)
        assert "Test" in text
    
    def test_message_stats_char_count(self):
        """Test character count in statistics."""
        msg = Message("Hello World")
        stats = msg.get_stats()
        assert "11" in stats  # 11 characters including space
    
    def test_message_stats_word_count(self):
        """Test word count in statistics."""
        msg = Message("Hello World Test")
        stats = msg.get_stats()
        assert "3" in stats  # 3 words
    
    def test_message_stats_most_common(self):
        """Test most common letter detection."""
        msg = Message("aaa bb c")
        stats = msg.get_stats()
        assert "a" in stats.lower()  # 'a' is most common
    
    def test_set_processed(self):
        """Test setting processed text."""
        msg = Message("Original")
        msg.set_processed("Processed", True)
        assert msg.processed_text == "Processed"
        assert msg.is_encoded == True


class TestEncoder:
    """Tests for the Encoder class - configured per assignment."""
    
    def test_diacritics_removal(self):
        """Test Czech diacritics removal."""
        encoder = get_encoder()
        result = encoder._remove_diacritics("Příliš žluťoučký kůň")
        assert result == "Prilis zlutoucky kun"
    
    def test_diacritics_preserve_case(self):
        """Test that diacritics removal preserves case."""
        encoder = get_encoder()
        result = encoder._remove_diacritics("ČLOVĚK člověk")
        assert result == "CLOVEK clovek"
    
    def test_encode_basic(self):
        """Test basic encoding."""
        encoder = get_encoder()
        test_case = CONFIG["test_cases"]["encode_basic"]
        
        msg = Message(test_case["input"])
        result = encoder.encode(msg)
        
        assert result.processed_text == test_case["expected"]
        assert result.is_encoded == True
    
    def test_encode_lowercase(self):
        """Test encoding preserves lowercase."""
        encoder = get_encoder()
        test_case = CONFIG["test_cases"]["encode_lower"]
        
        msg = Message(test_case["input"])
        result = encoder.encode(msg)
        
        assert result.processed_text == test_case["expected"]
    
    def test_encode_mixed_text(self):
        """Test encoding mixed case with spaces and punctuation."""
        encoder = get_encoder()
        test_case = CONFIG["test_cases"]["encode_mixed"]
        
        msg = Message(test_case["input"])
        result = encoder.encode(msg)
        
        assert result.processed_text == test_case["expected"]
    
    def test_encode_with_diacritics(self):
        """Test encoding text with Czech diacritics."""
        encoder = get_encoder()
        test_case = CONFIG["test_cases"]["encode_diacritics"]
        
        msg = Message(test_case["input"])
        result = encoder.encode(msg)
        
        assert result.processed_text == test_case["expected"]
    
    def test_decode_basic(self):
        """Test basic decoding."""
        encoder = get_encoder()
        test_case = CONFIG["test_cases"]["decode_basic"]
        
        msg = Message(test_case["input"], is_encoded=True)
        result = encoder.decode(msg)
        
        assert result.processed_text == test_case["expected"]
        assert result.is_encoded == False
    
    def test_encode_preserves_numbers(self):
        """Test that numbers are not changed."""
        encoder = get_encoder()
        msg = Message("Test 123")
        result = encoder.encode(msg)
        
        assert "123" in result.processed_text
    
    def test_encode_preserves_punctuation(self):
        """Test that punctuation is preserved."""
        encoder = get_encoder()
        msg = Message("Hello, World!")
        result = encoder.encode(msg)
        
        assert "," in result.processed_text
        assert "!" in result.processed_text
    
    def test_cipher_info(self):
        """Test cipher info method returns a string."""
        encoder = get_encoder()
        info = encoder.get_cipher_info()
        
        assert isinstance(info, str)
        assert len(info) > 0


class TestEncoderSymmetry:
    """Test that encode followed by decode returns original (normalized)."""
    
    def test_encode_decode_roundtrip(self):
        """Test encode->decode returns normalized original."""
        encoder = get_encoder()
        
        original = "Hello World"
        msg = Message(original)
        
        encoded = encoder.encode(msg)
        decoded = encoder.decode(encoded)
        
        # After encode->decode, we should get back the normalized text
        normalized = encoder._remove_diacritics(original).upper()
        assert decoded.processed_text.upper() == normalized.upper()
    
    def test_roundtrip_with_diacritics(self):
        """Test roundtrip with Czech diacritics."""
        encoder = get_encoder()
        
        original = "Žluťoučký kůň"
        msg = Message(original)
        
        encoded = encoder.encode(msg)
        decoded = encoder.decode(encoded)
        
        # Diacritics are lost but base text should match
        expected_normalized = "ZLUTOUCKY KUN"
        assert decoded.processed_text.upper() == expected_normalized


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
