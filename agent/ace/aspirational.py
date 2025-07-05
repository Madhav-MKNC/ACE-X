"""
Aspirational Layer: Defines the agent's highest-level goals, values, and moral constitution.
Loads the constitution from a text file and exposes core principles.
"""

import os

class AspirationalLayer:
    def __init__(self, constitution_path=None):
        """
        Initialize the Aspirational Layer.
        :param constitution_path: Path to the constitution file (default: data/config/constitution.txt)
        """
        if constitution_path is None:
            constitution_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'config', 'constitution.txt')
        self.constitution_path = os.path.abspath(constitution_path)
        self.core_principles = []
        self._load_constitution()

    def _load_constitution(self):
        """Load the constitution and core principles from file."""
        if not os.path.exists(self.constitution_path):
            self.core_principles = []
            return
        with open(self.constitution_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Filter out comments and blank lines
        self.core_principles = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]

    def get_principles(self):
        """Return the list of core principles."""
        return self.core_principles

    def __repr__(self):
        return f"<AspirationalLayer: {len(self.core_principles)} principles loaded>"
