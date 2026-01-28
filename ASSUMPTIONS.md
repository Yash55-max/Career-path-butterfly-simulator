# Assumptions: Plain English Explanations

> **Why the model works the way it does**

This document explains the core assumptions behind the Career Path Butterfly Simulator in plain English. No equations. Think policy paper tone.

---

## Core Modeling Assumptions

### 1. Careers as Probabilistic State Transitions

**Assumption:** Career progression can be modeled as moving between discrete states (Entry Level, Junior, Mid-Level, etc.) with probability-weighted transitions.

**Why this makes sense:**
- Real careers have recognizable stages and titles
- Promotions, lateral moves, and demotions happen with varying likelihoods
- Not everyone gets promoted every year—there's inherent randomness in who moves up

**What this ignores:**
- Continuous skill development (we use discrete states)
- Individual merit (everyone has the same base probabilities)
- Strategic planning (people don't optimize, they just follow probabilities)

**Real-world parallel:** Labor economists use similar models to study career mobility. The simplification allows us to isolate path dependence from individual differences.

---

### 2. Why Risk Increases Upside AND Volatility

**Assumption:** High risk tolerance leads to faster unemployment recovery to higher positions, but also more career volatility.

**The mechanism:**
- **Aggressive recovery:** Risk-takers don't settle for "safe" re-entry jobs. When unemployed, they hold out for Mid-Level positions instead of dropping back to Entry Level (+50% probability of Mid-Level recovery).
- **Higher variance:** This strategy works sometimes (reaching Director+ more often) but fails sometimes (longer unemployment periods).
- **Trade-off:** +1.93% Director+ rate, but more unemployment episodes and wider outcome distribution.

**Why this is realistic:**
- Entrepreneurs and risk-takers do reach higher peaks more often
- But they also experience more failures and volatility
- Conservative career paths have lower ceilings but more stability

**What this captures:** The fundamental risk-return trade-off in careers. You can't get higher upside without accepting more downside risk.

---

### 3. Why Early Specialization Plateaus

**Assumption:** Early specialization (+30% promotion probability years 0-10) creates a mid-career ceiling (+20% plateau probability years 15-30).

**The mechanism:**
- **Early acceleration:** Specialists gain deep expertise quickly, leading to faster early promotions (Junior → Mid-Level → Senior).
- **Mid-career trap:** Deep specialization makes lateral moves harder. When the specialist track narrows (fewer Director positions for specialists), they get stuck.
- **Generalists catch up:** Generalists move slower early but have more flexibility to pivot into management, cross-functional roles, and leadership positions.

**Why this is realistic:**
- Real-world specialists (e.g., deep technical experts) often hit "principal engineer" ceilings
- Generalists with broad experience become managers and executives
- Early career speed ≠ long-term ceiling

**Real-world examples:**
- PhD specialists vs. MBA generalists
- Deep technical ICs vs. people managers
- Domain experts vs. strategic leaders

**What the numbers show:** Early specialization results in −2.21% Director+ rate despite faster early career progression.

---

### 4. Why Retirement is Path-Dependent

**Assumption:** Retirement timing depends on burnout, momentum, career position, and unemployment—not just age.

**The mechanism:**

**Burnout accumulation:**
- High-stress roles (C-Suite, VP, Director) accumulate burnout faster
- Burnout increases retirement probability (up to +30%)
- Result: Executives retire ~2 years earlier than mid-level employees

**Momentum effects:**
- Recent promotions create momentum (delays retirement up to −20%)
- Successful people work longer because they're still climbing
- Plateaued people retire earlier because there's no upside

**Position effects:**
- Low-level positions at age 60+ trigger early retirement (+15%)
- Reason: Skill obsolescence and lack of advancement opportunities
- High-level positions delay retirement (−10%) due to influence and compensation

**Unemployment effects:**
- Unemployed at age 55+ face forced retirement (+20%)
- Reason: Age discrimination and difficulty re-entering the workforce

**Why this is realistic:**
- Real-world data shows executives retire earlier due to stress
- Successful people (high momentum) work into their 70s
- Unemployment after 55 often leads to permanent exit from workforce

**What this captures:** Retirement isn't just about hitting 65. It's the culmination of your entire career path—burnout, success, and circumstances all matter.

---

## Structural Assumptions

### 5. The Markov Property (History Doesn't Matter)

**Assumption:** Transitions depend only on your current state, not your full history.

**What this means:**
- If you're currently a Manager, your promotion probability to Director is the same whether you got there in 10 years or 20 years
- Your past demotions don't directly affect future transitions (except through burnout/momentum)

**Why this is a simplification:**
- Real careers have "scarring effects" (e.g., unemployment history affects future hiring)
- Real hiring managers look at your full resume, not just current title

**Why we use it anyway:**
- Makes the model tractable and interpretable
- Captures the key mechanism (path dependence through state transitions)
- Burnout and momentum partially compensate by tracking recent history

---

### 6. Time-Homogeneous Probabilities (No Economic Cycles)

**Assumption:** Transition probabilities don't change over time. The probability of promotion in year 5 is the same as in year 25.

**What this ignores:**
- Economic recessions (higher unemployment, lower promotions)
- Industry booms (faster advancement)
- Technological disruptions (skill obsolescence)

**Why we use it anyway:**
- Isolates the effect of individual decisions from external shocks
- Shows what happens in a "neutral" economic environment
- Real-world applications would layer economic cycles on top

---

### 7. Homogeneous Population (Everyone Starts Equal)

**Assumption:** Everyone has the same base transition probabilities. No individual differences in talent, education, or demographics.

**What this ignores:**
- Skills and talent (some people are better at their jobs)
- Education (MBA vs. no degree)
- Demographics (gender, race, age discrimination)
- Networking (who you know matters)

**Why we use it anyway:**
- Isolates the effect of decisions from individual differences
- Shows what happens when ONLY the decision differs
- Real-world studies would stratify by demographics and skills

**What this means for interpretation:**
- Results show the "pure effect" of decisions in a controlled environment
- Real-world effects would be modulated by individual differences
- Use this to understand mechanisms, not to predict individual outcomes

---

## Calibration and Realism

### 8. Where Do the Probabilities Come From?

**Honest answer:** They're illustrative, not empirically fitted.

**How they were chosen:**
- **Stagnation rates (40-70%):** Most people don't get promoted every year. This matches intuition and rough labor market data.
- **Promotion rates (15-30%):** Promotions happen, but they're competitive. Higher rates would make everyone reach C-Suite.
- **Unemployment rates (10-20%):** Reflects modern career volatility. Almost everyone faces unemployment at some point.
- **Demotion rates (5-15%):** Demotions happen (restructuring, performance issues) but are less common than stagnation.

**Validation approach:**
- Run simulations and check if outcomes "feel right" (e.g., ~35% Director+ matches real-world executive scarcity)
- Ensure structural realism (pyramid narrows, unemployment is common, retirement is path-dependent)

**What this means:**
- Numbers are plausible but not precise
- Use for understanding dynamics, not forecasting
- Real-world applications would fit probabilities to actual labor market data

---

## What the Model Gets Right

Despite simplifications, the model captures key career realities:

1. **Structural scarcity:** Not everyone can be a Director (pyramid narrows)
2. **Unemployment is universal:** Almost no one avoids it entirely
3. **Path dependence:** Early decisions compound over time
4. **Risk-return trade-offs:** Higher upside requires accepting more volatility
5. **Specialization trade-offs:** Early speed vs. long-term flexibility
6. **Retirement as outcome:** When you retire reveals your career trajectory

---

## How to Interpret Results

### ✅ Valid Interpretations:
- "In this model, early specialization decreases Director+ achievement by 2.21 percentage points"
- "The butterfly effect is quantifiable: small early changes → measurable long-term differences"
- "Path-dependent retirement reveals career trajectory differences"
- "These results demonstrate theoretical mechanisms of path dependence"

### ❌ Invalid Interpretations:
- "Everyone should avoid early specialization"
- "This proves causation in actual careers"
- "These exact numbers apply to real people"
- "This model predicts my career outcome"

### 🎯 Bottom Line:
This model shows **how path dependence works**, not **what you should do**. Use it to understand mechanisms, not to make career decisions.

---

## Extensions for Real-World Applications

To make this model more realistic, you would need to:

1. **Fit probabilities to real data:** Use labor market panel data (e.g., NLSY, PSID) to estimate actual transition probabilities
2. **Add individual heterogeneity:** Stratify by education, skills, demographics
3. **Include economic cycles:** Model recessions and booms
4. **Add strategic decision-making:** Let agents optimize, not just follow probabilities
5. **Network effects:** Model mentorship, referrals, and social capital
6. **Industry-specific models:** Tech vs. finance vs. healthcare have different dynamics

**But even without these extensions, the current model is valuable for:**
- Teaching stochastic simulation
- Demonstrating causal inference methods
- Understanding path dependence conceptually
- Portfolio projects showcasing technical rigor

---

## Final Thoughts

**The value of simplicity:**

This model is intentionally "stupid" (ignores skills, networking, economics) because:
- Simplicity isolates the mechanism we care about (path dependence)
- Complexity would obscure the core insight
- Real-world confounds make causal inference impossible

**The insight:**

Even in a simplified world where everyone is identical and only decisions differ, **small early choices create measurable long-term divergence**. This is the butterfly effect in action.

If path dependence works in this simple model, it definitely works in the real world—where individual differences, networking, and luck amplify the effect even further.

---

**Questions or feedback?** Open an issue on GitHub.
