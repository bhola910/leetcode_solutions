"""
change.py

Represents a Git file change.
"""

from dataclasses import dataclass


@dataclass
class Change:
    """Represents a Git change."""

    status: str
    path: str