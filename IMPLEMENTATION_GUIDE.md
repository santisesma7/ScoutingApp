# Implementation Summary: New Features

This document explains the three new features added to your Scouting App:

## 1. ⚡ Match Predictions Page (NEW)

**File**: `pages/5_Predicciones_Partidos.py`

### Features:
- **Automatic model fitting**: Uses the Poisson model with per-league home advantage
- **Time decay enabled**: Recent matches weighted more heavily (90-day half-life)
- **Weekly predictions**: Shows odds for upcoming matches
- **Interactive interface**:
  - Select league from dropdown
  - Choose home and away teams
  - View probabilities and European odds (1/probability format)
  - See expected goals (xG) for both teams

### How It Works:
1. Loads match history from `event_data/processed/top5_events_current.parquet`
2. Fits a Poisson model with:
   - Separate home advantage parameter per league
   - Time decay weighting (exponential)
   - Attack and defense strength parameters for each team
3. For each match prediction, calculates:
   - P(Home Win), P(Draw), P(Away Win) 
   - European odds format
   - Expected goals for both teams
4. Updates automatically when match data is refreshed

### Usage:
```
Navigate to: Predictions → Select League → Select Teams → View Odds
```

### Future Enhancement:
To fully automate:
1. Connect to a league calendar API (e.g., ESPN, official league API)
2. Schedule weekly model retraining
3. Auto-update predictions with latest match results

---

## 2. 🔗 Interactive Navigation Buttons (UPDATED Home.py)

**File**: `Home.py`

### Changes:
- All section cards are now **clickable links** that navigate to their respective pages
- Added **hover effects** with animations:
  - Smooth lift-up effect
  - Blue highlight on border
  - Icon changes color
- New **Predictions block** added with distinctive blue styling
- Module cards are now arranged horizontally (5 columns)

### New Styling:
```css
.section-card:hover {
    transform: translateY(-4px);              /* Lift up on hover */
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.15);
    border-color: #3b82f6;                    /* Blue border */
    background: linear-gradient(...)          /* Subtle gradient */
}
```

### Navigation Links:
- 🛡️ Estilos de Equipos → `/Estilos_Equipos`
- 🧠 Estilos de Jugadores → `/Estilos_Jugadores`
- 📊 Análisis de Métricas → `/Análisis_Métricas`
- 👤 Informe del Jugador → `/Informe_Jugador`
- ⚡ **Predicciones** (NEW) → `/Predicciones_Partidos`

---

## 3. 🌐 Accent-Insensitive Filters

**File**: `src/accent_utils.py`

### Functions:

#### `remove_accents(text)`
Removes accents from text:
```python
"Málaga" → "Malaga"
"José" → "Jose"
"Köln" → "Koln"
```

#### `get_accent_insensitive_selectbox(label, options, key)`
Drop-in replacement for `st.selectbox()` that handles accents:
```python
# Before (problematic with accents):
selected = st.selectbox("Team", ["Málaga", "Sevilla", "Bilbao"])

# After (handles accents):
selected = get_accent_insensitive_selectbox("Team", ["Málaga", "Sevilla", "Bilbao"])
# User can type "Malaga" and still match "Málaga"
```

### Pages Updated:
1. **Estilos_Equipos.py** (2 selectors):
   - Team selector (MCB section)
   - Team selector (MSB section)

2. **Informe_Jugador.py** (1 selector):
   - Player selector

### Usage:
```python
from src.accent_utils import get_accent_insensitive_selectbox

selected = get_accent_insensitive_selectbox(
    "Select a player",
    ["José", "Müller", "François"],
    key="unique_key"
)
```

### How It Works:
1. **Normalization**: User input and options are normalized (accents removed)
2. **Matching**: Comparison is done on normalized versions
3. **Return**: Original value with accents is returned to preserve data integrity

### Benefits:
- Users can search "Madrid" and still find "Málaga"
- Handles: Spanish (á, é, í, ó, ú, ñ), German (ä, ö, ü), French (é, è, ê, ç), etc.
- Transparent to user - behaves like normal selectbox
- No data modification - original accents preserved

---

## Installation & Testing

### 1. Test the New Pages:
```bash
streamlit run Home.py
# Click on "Predicciones" button (new 5th card)
```

### 2. Test Accent-Insensitive Filters:
```
Go to: Estilos de Equipos
- Filters now match "Real Madrid" ↔ "Real Madrid"
- Filters now match "Málaga" ↔ "Malaga"
- Filters now match "José" ↔ "Jose"
```

### 3. Test Interactive Buttons:
```
From Home page:
- Hover over any section card (lift-up effect, color change)
- Click on any card to navigate
- Click on Predictions card (blue highlighting)
```

---

## Configuration for Weekly Updates

To automate the predictions for each week:

### Option A: Use Streamlit Cloud Scheduler
```python
# In pages/5_Predicciones_Partidos.py
# Add scheduled task to refresh model every week
```

### Option B: Local Cron Job
```bash
# Update model weekly
0 22 * * 7 cd /path/to/app && python -c "from src.build_top5_events import build_top5_events; build_top5_events()"
```

### Option C: External API Integration
```python
# Connect to official league calendars
from espn_api import get_upcoming_matches  # or similar

upcoming = get_upcoming_matches(league="LaLiga")
for match in upcoming:
    pred = predict_match_odds(match['home'], match['away'], ...)
```

---

## Files Created/Modified

### New Files:
- ✅ `src/accent_utils.py` - Accent normalization utilities
- ✅ `pages/5_Predicciones_Partidos.py` - Predictions interface

### Modified Files:
- ✅ `Home.py` - Interactive buttons + Predictions card
- ✅ `pages/1_Estilos_Equipos.py` - Accent-insensitive team selectors
- ✅ `pages/4_Informe_Jugador.py` - Accent-insensitive player selector

---

## Troubleshooting

### Issue: Predictions page shows errors
**Solution**: Make sure `event_data/processed/top5_events_current.parquet` exists with recent data

### Issue: Team names not found in predictions
**Solution**: The model only predicts for teams in the historical data. Add more recent matches first.

### Issue: Accent filter not working
**Solution**: Restart streamlit app - changes to `accent_utils.py` require reload

### Issue: Slow predictions
**Solution**: Model fitting runs once per session. For faster performance with many predictions, cache the model fitting result.
