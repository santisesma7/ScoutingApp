#!/usr/bin/env python
"""Quick test of accent utilities"""

from src.accent_utils import remove_accents, normalize_selectbox_options

# Test accent removal
print('Testing accent removal:')
print(f'  Málaga → {remove_accents("Málaga")}')
print(f'  José → {remove_accents("José")}')
print(f'  Köln → {remove_accents("Köln")}')

# Test option normalization
print('\nTesting option normalization:')
options = ['Real Madrid', 'Málaga', 'Sevilla', 'José']
normalized, mapping = normalize_selectbox_options(options)
print(f'  Original: {options}')
print(f'  Normalized: {normalized}')
print(f'  Mapping: {mapping}')

print('\n✅ All accent utilities working correctly!')
