import re

with open('temp_parser_all.py', 'r', encoding='utf-8') as f:
    content = f.read()
    match = re.search(r'text = """(.+?)"""', content, re.DOTALL)
    if match:
        text = match.group(1)
        # Find league markers and show context
        print('=== SEARCHING FOR LEAGUE MARKERS ===')
        lines = text.split('\n')
        
        # Find where each league section starts
        league_markers = ['bundesliga', 'serie a', 'ligue 1', 'la liga']
        for i, line in enumerate(lines):
            line_lower = line.lower().strip()
            for marker in league_markers:
                if marker in line_lower:
                    print(f'\nLine {i}: {line[:80]}')
