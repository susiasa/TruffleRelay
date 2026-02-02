# test_trufflerelay.py
"""
Tests for TruffleRelay module.
"""

import unittest
from trufflerelay import TruffleRelay

class TestTruffleRelay(unittest.TestCase):
    """Test cases for TruffleRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TruffleRelay()
        self.assertIsInstance(instance, TruffleRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TruffleRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
