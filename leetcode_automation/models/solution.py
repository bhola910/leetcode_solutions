"""
solution.py

Represents a LeetCode solution.
"""

from dataclasses import dataclass


@dataclass
class Solution:
    """Represents a LeetCode solution."""

    number: int
    title: str
    language: str
    path: str