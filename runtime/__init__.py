"""CRE Runtime v0 - generated, disposable, read-only execution layer.

The repository remains the canonical source of truth. This package projects the
canonical release exports (``exports/*.csv``) into a generated SQLite runtime
database that is safe to delete and regenerate at any time.
"""

from .config import SCHEMA_VERSION

__all__ = ["SCHEMA_VERSION"]
