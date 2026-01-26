# Career Path Butterfly Simulator

A **"stupid" but insightful** career progression simulator that demonstrates the butterfly effect in career trajectories through pure probability-based modeling.

## 🎯 What This Is

This simulator models 5,000+ career paths over 45 years using:
- **No ML** - Just biased random transitions
- **No fancy libraries** - Pure Python logic with matplotlib
- **Path-dependent decisions** - Early choices have measurable long-term impacts
- **Quantified butterfly effect** - Specific percentage impacts of decisions

## 🚀 Key Features

### 1. **Realistic Career Dynamics**
- 11 career states: Entry Level → Junior → Mid-Level → Senior → Lead → Manager → Director → VP → C-Suite
- High stagnation rates (40-70% plateau probabilities)
- Unemployment and demotion risks
- Most careers plateau at Mid-Level (realistic!)

### 2. **Path-Dependent Retirement**
Retirement is NOT just age-based. It depends on:
- **Burnout score** (accumulates from high-stress positions)
- **Career momentum** (recent success delays retirement)
- **Position level** (executives work longer, low-level forced out)
- **Unemployment** (forced early retirement)

### 3. **Quantified Butterfly Effect**
The simulator runs **intervention studies** to prove causality:
- **Control group** vs **Early Specialization** vs **High Risk Tolerance**
- Measures specific impacts:
  - Director+ achievement rate differences
  - Unemployment timing delays
  - Retirement age variations
  - Peak position distribution shifts

## 📊 Sample Results

From a typical run:

**Early Specialization Impact:**
- Director+ achievement: **+2-4%** increase
- Faster early climb, but higher mid-career plateau
- Trade-off: Speed vs. flexibility

**High Risk Tolerance Impact:**
- Director+ achievement: **+5-8%** increase  
- Faster unemployment recovery
- Higher variance in outcomes

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Yash55-max/Career-path-butterfly-simulator.git
cd Career-path-butterfly-simulator

# Create virtual environment (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate    # Linux/Mac

# Install dependencies
pip install matplotlib numpy
```

## 🎮 Usage

### Basic Run
```bash
python stupid_simulator.py
```

This will:
1. Simulate 7,500 careers (2,500 per intervention group)
2. Print detailed statistics to console
3. Generate `butterfly_effect_proof.png` with 6 comparative plots

### Output Files
- `butterfly_effect_proof.png` - Main visualization with intervention comparisons
- Console output - Detailed statistics and quantified impacts

## 📈 What the Plots Show

1. **Peak Position by Decision** - Bar chart comparing career peaks across interventions
2. **Director+ Achievement Rate** - Quantified butterfly effect (specific percentages)
3. **Retirement Age Distribution** - Path-dependent retirement patterns
4. **Career Trajectories (Control)** - Heatmap of 50 sample careers
5. **Career Trajectories (Specialists)** - Early specialization patterns
6. **Career Trajectories (Risk-Takers)** - High risk tolerance patterns

## 🧠 Key Insights

### The Mid-Level Trap
Most careers plateau at Mid-Level (50% stagnation rate). Breaking through to Senior is the critical barrier.

### Unemployment is Universal
Almost everyone faces job loss. Average: 2-5 unemployment periods per career.

### Early Decisions Matter
A single decision at year 3 (specialization) can change Director+ probability by **2-4 percentage points** across 5,000 careers.

### Retirement Reveals Path
- High burnout → Early retirement
- High momentum → Delayed retirement  
- Low-level positions → Forced retirement at 60+
- Executives → Work into 70s

### Time ≠ Achievement
Years worked doesn't equal career level. Volatility dominates.

## 🔬 Technical Details

### Transition Probabilities
Calibrated for realism:
- **Stagnation**: 40-70% (most people plateau)
- **Promotion**: 15-30% (hard to advance)
- **Demotion**: 5-15% (downward mobility happens)
- **Unemployment**: 10-20% (persistent risk)

### Decision Modifiers
- **Early Specialization**: +30% early promotion, +20% mid-career plateau
- **High Risk**: +50% unemployment recovery, +30% variance
- **Low Risk**: +30% safe recovery, +10% longer unemployment

### Retirement Formula
```python
base_prob = age_factor(age)
+ burnout_factor (up to +30%)
- momentum_factor (up to -20%)
+ position_factor (low-level +15%, high-level -10%)
+ unemployment_factor (age 55+ → +20%)
```

## 📝 Code Structure

- `stupid_simulator.py` - Main simulator with intervention study
- `CareerProfile` class - Tracks decisions, burnout, momentum
- `simulate_career()` - Single career simulation with path-dependent logic
- `run_intervention_study()` - Runs 3 groups for comparison
- `quantify_butterfly_effect()` - Calculates specific percentage impacts
- `plot_intervention_comparison()` - Generates visualizations

## 🎓 Educational Value

This simulator demonstrates:
1. **Emergence** - Complex patterns from simple rules
2. **Path dependence** - History matters
3. **Butterfly effect** - Small changes → large impacts
4. **Stochastic processes** - Randomness with structure
5. **Intervention analysis** - Causal inference without ML

## 🤔 Why "Stupid"?

It's "stupid" because:
- No skills, education, or merit
- No economic cycles or industry trends
- No networking or politics
- Just pure probability

But it's **insightful** because:
- Probabilities calibrated to real career friction
- Path-dependent retirement is realistic
- Butterfly effect is quantified, not just visible
- Shows emergent patterns from simple rules

## 📊 Sample Console Output

```
==================================================================
BUTTERFLY EFFECT ANALYSIS: Early Specialization vs Control
==================================================================

📊 Director+ Achievement Rate:
  Control:       392 / 2500 = 15.68%
  Intervention:  441 / 2500 = 17.64%
  ➜ IMPACT: +1.96 percentage points

⏱️  First Unemployment Timing:
  Control median:      Year 8.0
  Intervention median: Year 6.5
  ➜ IMPACT: -1.5 years delay

🎯 Retirement Age:
  Control avg:      66.3 years old
  Intervention avg: 65.8 years old
  ➜ IMPACT: -0.5 years difference
```

## 🚧 Limitations

- No individual differences (skills, education)
- No external shocks (recessions, industry changes)
- No strategic decision-making (just probabilistic)
- Fixed transition probabilities (no learning)

## 🔮 Future Enhancements

- [ ] Add more decision points (year 10, 20, 30)
- [ ] Industry-specific transition matrices
- [ ] Economic cycle simulation
- [ ] Skill accumulation and depreciation
- [ ] Network effects
- [ ] Gender/demographic disparities

## 📜 License

MIT License - Feel free to use, modify, and learn from this code!

## 🙏 Acknowledgments

Built as a demonstration of:
- Stochastic modeling
- Path dependence
- Butterfly effect quantification
- Intervention study design

No ML. No fancy libraries. Just logic and probability.

---

**Made with Python, probability, and a healthy dose of career realism** 🎲📈
