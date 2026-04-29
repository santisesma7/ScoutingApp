"""
Utility functions for accent-insensitive text matching and filtering.
Allows "Málaga" to match "Malaga", "José" to match "Jose", etc.
"""

import unicodedata
from typing import List, Dict, Any


def remove_accents(text: str) -> str:
    """
    Remove accents from text.
    Example: "Málaga" → "Malaga", "José" → "Jose"
    """
    if not isinstance(text, str):
        return text
    
    nfkd_form = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


def filter_by_accent_insensitive(
    df,
    column: str,
    search_value: str,
) -> Any:
    """
    Filter dataframe by column value, ignoring accents.
    
    Args:
        df: pandas DataFrame
        column: column name to filter on
        search_value: value to search for (accents ignored)
    
    Returns:
        Filtered DataFrame
    """
    if search_value is None or search_value == "":
        return df
    
    # Create a normalized version of the column for comparison
    normalized_column = df[column].apply(remove_accents)
    normalized_search = remove_accents(search_value)
    
    return df[normalized_column == normalized_search]


def normalize_selectbox_options(options: List[str]) -> tuple:
    """
    Create mapping from normalized (no accents) to original values.
    Displays original names but accepts input without accents.
    
    Args:
        options: List of options (may contain accents)
    
    Returns:
        Tuple of (normalized_list, mapping_dict) where:
        - normalized_list: options without accents (for input)
        - mapping_dict: {normalized: original} for reverse lookup
    """
    mapping = {remove_accents(opt): opt for opt in options}
    normalized_options = list(mapping.keys())
    return normalized_options, mapping


def get_accent_insensitive_selectbox(
    label: str,
    options: List[str],
    key: str = None,
    index: int = 0,
) -> str:
    """
    Selectbox that shows original names but accepts input without accents.
    User types "Malaga" → matches "Málaga" → returns original "Málaga"
    
    Args:
        label: Label for the selectbox
        options: List of options (with or without accents)
        key: Streamlit key
        index: Default index
    
    Returns:
        The original selected value (with accents preserved)
    """
    import streamlit as st
    
    # Create normalized versions for input, keep mapping to originals
    normalized_options, mapping = normalize_selectbox_options(options)
    
    # Show selectbox with normalized options (no accents for input)
    selected_normalized = st.selectbox(
        label,
        normalized_options,
        index=index,
        key=key
    )
    
    # Return the original value with accents preserved
    return mapping[selected_normalized]
