# Repository Structure

```
career-butterfly-simulator/
│
├── src/
│   └── simulator.py              # Main simulation code (formerly stupid_simulator.py)
│
├── figures/
│   ├── butterfly_effect_ci.png   # Publication-quality single figure
│   └── uncertainty_analysis.png  # Full 6-panel analysis
│
├── README.md                      # Clean, professional README
├── ASSUMPTIONS.md                 # Plain English explanations
├── 60_SECOND_EXPLANATION.md       # Your elevator pitch
├── requirements.txt               # Dependencies
└── .gitignore                     # Excludes old/deprecated files
```

## Clean Structure Achieved ✅

### What Changed:
1. **Organized code:** Moved `stupid_simulator.py` → `src/simulator.py`
2. **Organized outputs:** Moved figures to `figures/` directory
3. **Removed clutter:** Deleted `PROJECT_SUMMARY.md`, `QUICK_REFERENCE.md`, `description.txt`, `run_simulator.py`
4. **Updated paths:** Simulator now outputs to `figures/` directory
5. **Added to .gitignore:** Old files won't clutter git status

### Files You Can Delete (Already in .gitignore):
- `stupid_simulator.py` (copied to `src/simulator.py`)
- `output.txt` (gitignored)
- `results.txt` (gitignored)

## How to Run

```bash
# From repository root
python src/simulator.py
```

**Output:**
- `figures/butterfly_effect_ci.png`
- `figures/uncertainty_analysis.png`
- Console statistics with confidence intervals

## Repository Status

**Professional ✅**  
**Boring ✅** (in a good way)  
**Clean ✅**  
**Ready for GitHub ✅**
