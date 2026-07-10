"""
collection.py — Single source of truth for the ChromaDB collection name.

Both the MCP server and the CLI/search paths must write to and read from the
SAME collection. Previously several modules hardcoded "brain_drawers" while
AilawfirmEuConfig().collection_name defaulted to "ailawfirm_eu_drawers", which
meant drawers filed via the MCP server were invisible to search/cli and vice
versa.

Use ``get_collection_name()`` anywhere a collection name is needed so that the
config-driven name is honoured uniformly.
"""

from ailawfirm_eu.config import AilawfirmEuConfig


def get_collection_name() -> str:
    """Return the canonical ChromaDB collection name from config.

    Instantiating ``AilawfirmEuConfig()`` once here means callers don't each
    re-read ``config.json`` and can't drift from the canonical name.
    """
    return AilawfirmEuConfig().collection_name
