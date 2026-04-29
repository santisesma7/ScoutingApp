"""
Parse upcoming matches from temporary parser data.
Extracts matches with dates that haven't been played yet.
"""

import re
import pandas as pd
from datetime import datetime
from pathlib import Path


def split_text_by_leagues(text: str) -> dict:
    """
    Split the full text into sections by league.
    Looks for patterns like 'bundesliga', 'serie a', 'ligue 1', 'la liga', 'premier league' at start of lines.
    """
    leagues_sections = {
        'Bundesliga': '',
        'Serie A': '',
        'Ligue 1': '',
        'La Liga': '',
        'Premier League': ''
    }
    
    current_league = None
    for line in text.split('\n'):
        line_lower = line.lower().strip()
        
        # Detect league changes
        if line_lower.startswith('bundesliga'):
            current_league = 'Bundesliga'
        elif 'serie a' in line_lower and 'ahora' in line_lower:
            current_league = 'Serie A'
        elif 'ligue 1' in line_lower and 'ahora' in line_lower:
            current_league = 'Ligue 1'
        elif ('la liga' in line_lower or 'y por ultimo' in line_lower) and 'liga' in line_lower:
            current_league = 'La Liga'
        elif 'premier league' in line_lower or line_lower.startswith('premier'):
            current_league = 'Premier League'
        
        if current_league:
            leagues_sections[current_league] += line + '\n'
    
    return leagues_sections


def parse_upcoming_matches(text: str) -> pd.DataFrame:
    """
    Parse upcoming matches from raw text.
    Structure for upcoming matches:
    Jornada X
    Equipo local
    Resultado
    Equipo visitante
    Home Team
    Home Team (duplicate)
    DD/MM (date)
    HH:MM (time)
    Away Team
    Away Team (duplicate)
    ...
    """
    matches = []
    
    # Split by league first
    leagues_sections = split_text_by_leagues(text)
    
    for league_name, league_text in leagues_sections.items():
        if not league_text.strip():
            continue
            
        lines = league_text.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        
        current_jornada = None
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Detect jornada
            if line.startswith('Jornada'):
                match = re.search(r'Jornada (\d+)', line)
                if match:
                    current_jornada = int(match.group(1))
            
            # Look for date pattern (DD/MM) - this indicates an upcoming match
            if re.match(r'^\d{2}/\d{2}$', line):
                date_str = line
                
                # Expected structure around the date:
                # i-3: Home team name (duplicate)
                # i-2: Home team name (original)
                # i-1: Date (this line, so actually looking back: i-2 is the line BEFORE this date)
                # i: Date (current)
                # i+1: Time
                # i+2: Away team name (original)
                # i+3: Away team name (duplicate)
                
                # Get the time (should be next line)
                time_str = lines[i+1] if i+1 < len(lines) and re.match(r'^\d{2}:\d{2}$', lines[i+1]) else "20:00"
                
                # Get teams by going back to find the home team
                # The structure is: Team, Team (duplicate), Date, Time, Team, Team (duplicate)
                # So home team is at i-2, away team is at i+2 (after time at i+1)
                home_idx = i - 2
                away_idx = i + 2  # Assuming format: date(i), time(i+1), away team(i+2), away dup(i+3)
                
                home_team = lines[home_idx] if home_idx >= 0 else None
                away_team = lines[away_idx] if away_idx < len(lines) else None
                
                # Validate that they're not header lines
                header_lines = ['Equipo local', 'Resultado', 'Equipo visitante', 'Ir arriba', 'bundesliga', 'serie a', 'ligue 1', 'la liga']
                
                if home_team and away_team and current_jornada:
                    if (home_team not in header_lines and 
                        away_team not in header_lines and
                        'jornada' not in home_team.lower() and
                        'jornada' not in away_team.lower()):
                        
                        matches.append({
                            'league': league_name,
                            'jornada': current_jornada,
                            'home_team': home_team,
                            'away_team': away_team,
                            'date': date_str,
                            'time': time_str
                        })
            
            i += 1
    
    return pd.DataFrame(matches)


def get_upcoming_matches_from_file(file_path: str = "temp_parser_all.py") -> pd.DataFrame:
    """
    Load upcoming matches from the temporary parser file.
    Extracts the 'text' variable from the Python file.
    
    Args:
        file_path: Path to the parser file
    
    Returns:
        DataFrame with upcoming matches
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the text variable content
        match = re.search(r'text = """(.+?)"""', content, re.DOTALL)
        if match:
            text = match.group(1)
            result = parse_upcoming_matches(text)
            return result
        else:
            print("Could not find text variable in file")
            return pd.DataFrame()
    
    except Exception as e:
        print(f"Error parsing file: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame()


def format_match_date(date_str: str) -> str:
    """
    Convert DD/MM to full date format.
    
    Args:
        date_str: Date in DD/MM format
    
    Returns:
        Formatted date string
    """
    try:
        day, month = date_str.split('/')
        date = datetime(2026, int(month), int(day))
        return date.strftime('%a, %d %b')
    except:
        return date_str
