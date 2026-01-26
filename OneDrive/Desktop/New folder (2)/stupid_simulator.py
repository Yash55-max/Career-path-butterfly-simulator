import random
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import numpy as np

# Career states
STATES = [
    "Entry Level",
    "Junior",
    "Mid-Level",
    "Senior",
    "Lead",
    "Manager",
    "Director",
    "VP",
    "C-Suite",
    "Retired",
    "Unemployed"
]

# Base transition probabilities
TRANSITIONS = {
    "Entry Level": {
        "Entry Level": 0.45,
        "Junior": 0.30,
        "Mid-Level": 0.05,
        "Unemployed": 0.20
    },
    "Junior": {
        "Junior": 0.40,
        "Mid-Level": 0.30,
        "Senior": 0.05,
        "Entry Level": 0.10,
        "Unemployed": 0.15
    },
    "Mid-Level": {
        "Mid-Level": 0.50,
        "Senior": 0.20,
        "Lead": 0.05,
        "Junior": 0.10,
        "Unemployed": 0.15
    },
    "Senior": {
        "Senior": 0.55,
        "Lead": 0.15,
        "Manager": 0.10,
        "Mid-Level": 0.10,
        "Unemployed": 0.10
    },
    "Lead": {
        "Lead": 0.50,
        "Manager": 0.20,
        "Director": 0.05,
        "Senior": 0.15,
        "Unemployed": 0.10
    },
    "Manager": {
        "Manager": 0.55,
        "Director": 0.15,
        "Lead": 0.15,
        "Senior": 0.05,
        "Unemployed": 0.10
    },
    "Director": {
        "Director": 0.60,
        "VP": 0.10,
        "Manager": 0.15,
        "Unemployed": 0.15
    },
    "VP": {
        "VP": 0.65,
        "C-Suite": 0.08,
        "Director": 0.15,
        "Unemployed": 0.12
    },
    "C-Suite": {
        "C-Suite": 0.70,
        "VP": 0.10,
        "Unemployed": 0.10,
        "Retired": 0.10
    },
    "Retired": {
        "Retired": 1.0
    },
    "Unemployed": {
        "Unemployed": 0.50,
        "Entry Level": 0.25,
        "Junior": 0.15,
        "Mid-Level": 0.08,
        "Retired": 0.02
    }
}


class CareerProfile:
    """Track career decisions and their impacts"""
    def __init__(self, early_specialization=False, risk_tolerance="medium"):
        self.early_specialization = early_specialization  # Decision at year 3
        self.risk_tolerance = risk_tolerance  # low, medium, high
        self.unemployment_history = []
        self.peak_achieved = "Entry Level"
        self.years_at_peak = 0
        self.total_demotions = 0
        self.total_promotions = 0
        self.burnout_score = 0  # Accumulates over time
        self.momentum_score = 0  # Recent success
        
    def update_burnout(self, current_state, years_worked):
        """Calculate burnout based on career stress"""
        stress_levels = {
            "C-Suite": 5, "VP": 4, "Director": 3,
            "Manager": 2, "Lead": 2, "Senior": 1,
            "Mid-Level": 0, "Junior": 0, "Entry Level": 0,
            "Unemployed": -2  # Recovery
        }
        self.burnout_score += stress_levels.get(current_state, 0)
        # Burnout decays slowly
        self.burnout_score = max(0, self.burnout_score - 0.5)
        
    def update_momentum(self, old_state, new_state):
        """Track recent career momentum"""
        state_ranks = {
            "Entry Level": 1, "Junior": 2, "Mid-Level": 3,
            "Senior": 4, "Lead": 5, "Manager": 6,
            "Director": 7, "VP": 8, "C-Suite": 9,
            "Unemployed": 0, "Retired": 0
        }
        
        old_rank = state_ranks.get(old_state, 0)
        new_rank = state_ranks.get(new_state, 0)
        
        if new_rank > old_rank:
            self.momentum_score += 2
            self.total_promotions += 1
        elif new_rank < old_rank:
            self.momentum_score = max(0, self.momentum_score - 3)
            self.total_demotions += 1
        
        # Momentum decays
        self.momentum_score = max(0, self.momentum_score * 0.9)


def get_retirement_probability(profile, current_state, years_worked, age):
    """
    PATH-DEPENDENT retirement probability
    Based on: age, burnout, momentum, career level
    """
    if current_state == "Retired":
        return 1.0
    
    base_prob = 0.0
    
    # Age factor
    if age < 50:
        base_prob = 0.0
    elif age < 60:
        base_prob = 0.01
    elif age < 65:
        base_prob = 0.08
    elif age < 70:
        base_prob = 0.25
    else:
        base_prob = 0.50
    
    # BURNOUT increases early retirement
    burnout_factor = min(profile.burnout_score / 100, 0.3)  # Up to +30%
    
    # MOMENTUM delays retirement (successful people work longer)
    momentum_factor = -min(profile.momentum_score / 50, 0.2)  # Up to -20%
    
    # LOW-LEVEL positions → forced retirement (skill irrelevance)
    if age > 60 and current_state in ["Entry Level", "Junior", "Mid-Level"]:
        base_prob += 0.15  # Forced out
    
    # HIGH-LEVEL positions → delayed retirement (still valuable)
    if current_state in ["C-Suite", "VP", "Director"]:
        base_prob -= 0.10
    
    # UNEMPLOYMENT → forced retirement
    if current_state == "Unemployed" and age > 55:
        base_prob += 0.20
    
    final_prob = max(0, min(1.0, base_prob + burnout_factor + momentum_factor))
    return final_prob


def apply_decision_modifiers(profile, transitions, current_state, years_worked):
    """
    Modify transition probabilities based on early decisions
    THIS IS WHERE BUTTERFLY EFFECT HAPPENS
    """
    modified = transitions.copy()
    
    # EARLY SPECIALIZATION (decision at year 3)
    if profile.early_specialization:
        # Faster initial climb, but higher plateau risk
        if current_state in ["Entry Level", "Junior"]:
            # Boost early promotions
            for state in modified:
                if state in ["Junior", "Mid-Level", "Senior"]:
                    modified[state] = modified.get(state, 0) * 1.3
        elif current_state in ["Senior", "Lead"]:
            # Higher plateau (specialized = less flexible)
            modified[current_state] = modified.get(current_state, 0) * 1.2
    else:
        # Slower start, but better long-term mobility
        if current_state in ["Manager", "Director", "VP"]:
            # Better late-career advancement
            for state in ["Director", "VP", "C-Suite"]:
                if state in modified:
                    modified[state] = modified.get(state, 0) * 1.25
    
    # RISK TOLERANCE affects unemployment recovery
    if current_state == "Unemployed":
        if profile.risk_tolerance == "high":
            # Risk-takers recover faster but at varied levels
            modified["Mid-Level"] = modified.get("Mid-Level", 0) * 1.5
            modified["Unemployed"] = modified.get("Unemployed", 0) * 0.8
        elif profile.risk_tolerance == "low":
            # Safe players take longer but more stable
            modified["Entry Level"] = modified.get("Entry Level", 0) * 1.3
            modified["Unemployed"] = modified.get("Unemployed", 0) * 1.1
    
    # Normalize probabilities
    total = sum(modified.values())
    if total > 0:
        modified = {k: v/total for k, v in modified.items()}
    
    return modified


def simulate_career(max_years=45, starting_age=22, profile=None):
    """Simulate a single career with decision tracking"""
    if profile is None:
        profile = CareerProfile()
    
    current_state = "Entry Level"
    career_path = [current_state]
    current_age = starting_age
    
    for year in range(max_years):
        current_age += 1
        
        if current_state == "Retired":
            career_path.append(current_state)
            continue
        
        # Update profile metrics
        profile.update_burnout(current_state, year)
        
        # Check for PATH-DEPENDENT retirement
        retirement_prob = get_retirement_probability(profile, current_state, year, current_age)
        if random.random() < retirement_prob:
            current_state = "Retired"
            career_path.append(current_state)
            continue
        
        # Apply decision modifiers to transitions
        base_transitions = TRANSITIONS[current_state]
        modified_transitions = apply_decision_modifiers(profile, base_transitions, current_state, year)
        
        # Make transition
        next_states = list(modified_transitions.keys())
        probabilities = list(modified_transitions.values())
        
        old_state = current_state
        next_state = random.choices(next_states, weights=probabilities, k=1)[0]
        
        # Update momentum
        profile.update_momentum(old_state, next_state)
        
        # Track unemployment
        if next_state == "Unemployed":
            profile.unemployment_history.append(year)
        
        career_path.append(next_state)
        current_state = next_state
    
    return career_path, profile


def get_peak_position(career):
    """Find the HIGHEST career level achieved"""
    state_ranks = {
        "Unemployed": 0, "Entry Level": 1, "Junior": 2,
        "Mid-Level": 3, "Senior": 4, "Lead": 5,
        "Manager": 6, "Director": 7, "VP": 8,
        "C-Suite": 9, "Retired": 0
    }
    
    max_rank = 0
    peak_state = "Entry Level"
    
    for state in career:
        rank = state_ranks.get(state, 0)
        if rank > max_rank:
            max_rank = rank
            peak_state = state
    
    return peak_state


def run_intervention_study(num_simulations=2500):
    """
    BUTTERFLY EFFECT PROOF:
    Compare outcomes with different early decisions
    """
    print("\n" + "=" * 70)
    print("INTERVENTION STUDY: Quantifying Butterfly Effect")
    print("=" * 70)
    
    # Control group: No early specialization, medium risk
    print("\n[1/3] Running CONTROL group (no specialization, medium risk)...")
    control_results = []
    for i in range(num_simulations):
        if (i + 1) % 500 == 0:
            print(f"  Progress: {i + 1}/{num_simulations}")
        profile = CareerProfile(early_specialization=False, risk_tolerance="medium")
        career, profile = simulate_career(profile=profile)
        peak = get_peak_position(career)
        control_results.append({
            'career': career,
            'peak': peak,
            'profile': profile,
            'final_state': career[-1]
        })
    
    # Intervention 1: Early specialization
    print("\n[2/3] Running INTERVENTION 1 (early specialization)...")
    specialist_results = []
    for i in range(num_simulations):
        if (i + 1) % 500 == 0:
            print(f"  Progress: {i + 1}/{num_simulations}")
        profile = CareerProfile(early_specialization=True, risk_tolerance="medium")
        career, profile = simulate_career(profile=profile)
        peak = get_peak_position(career)
        specialist_results.append({
            'career': career,
            'peak': peak,
            'profile': profile,
            'final_state': career[-1]
        })
    
    # Intervention 2: High risk tolerance
    print("\n[3/3] Running INTERVENTION 2 (high risk tolerance)...")
    risktaker_results = []
    for i in range(num_simulations):
        if (i + 1) % 500 == 0:
            print(f"  Progress: {i + 1}/{num_simulations}")
        profile = CareerProfile(early_specialization=False, risk_tolerance="high")
        career, profile = simulate_career(profile=profile)
        peak = get_peak_position(career)
        risktaker_results.append({
            'career': career,
            'peak': peak,
            'profile': profile,
            'final_state': career[-1]
        })
    
    return control_results, specialist_results, risktaker_results


def quantify_butterfly_effect(control, intervention, intervention_name):
    """Calculate numerical impact of decision"""
    print(f"\n{'=' * 70}")
    print(f"BUTTERFLY EFFECT ANALYSIS: {intervention_name}")
    print(f"{'=' * 70}")
    
    # Peak position comparison
    state_ranks = {
        "Entry Level": 1, "Junior": 2, "Mid-Level": 3,
        "Senior": 4, "Lead": 5, "Manager": 6,
        "Director": 7, "VP": 8, "C-Suite": 9
    }
    
    # Director+ achievement rate
    control_director_plus = sum(1 for r in control if state_ranks.get(r['peak'], 0) >= 7)
    intervention_director_plus = sum(1 for r in intervention if state_ranks.get(r['peak'], 0) >= 7)
    
    control_pct = (control_director_plus / len(control)) * 100
    intervention_pct = (intervention_director_plus / len(intervention)) * 100
    delta_pct = intervention_pct - control_pct
    
    print(f"\n📊 Director+ Achievement Rate:")
    print(f"  Control:      {control_director_plus:4d} / {len(control)} = {control_pct:5.2f}%")
    print(f"  Intervention: {intervention_director_plus:4d} / {len(intervention)} = {intervention_pct:5.2f}%")
    print(f"  ➜ IMPACT: {delta_pct:+.2f} percentage points")
    
    # Unemployment timing
    control_unemp_years = [year for r in control for year in r['profile'].unemployment_history]
    intervention_unemp_years = [year for r in intervention for year in r['profile'].unemployment_history]
    
    if control_unemp_years and intervention_unemp_years:
        control_median = np.median(control_unemp_years)
        intervention_median = np.median(intervention_unemp_years)
        delta_years = intervention_median - control_median
        
        print(f"\n⏱️  First Unemployment Timing:")
        print(f"  Control median:      Year {control_median:.1f}")
        print(f"  Intervention median: Year {intervention_median:.1f}")
        print(f"  ➜ IMPACT: {delta_years:+.1f} years delay")
    
    # Retirement age comparison
    control_retire_ages = []
    intervention_retire_ages = []
    
    for r in control:
        if "Retired" in r['career']:
            retire_year = r['career'].index("Retired")
            control_retire_ages.append(22 + retire_year)
    
    for r in intervention:
        if "Retired" in r['career']:
            retire_year = r['career'].index("Retired")
            intervention_retire_ages.append(22 + retire_year)
    
    if control_retire_ages and intervention_retire_ages:
        control_avg_retire = np.mean(control_retire_ages)
        intervention_avg_retire = np.mean(intervention_retire_ages)
        delta_retire = intervention_avg_retire - control_avg_retire
        
        print(f"\n🎯 Retirement Age:")
        print(f"  Control avg:      {control_avg_retire:.1f} years old")
        print(f"  Intervention avg: {intervention_avg_retire:.1f} years old")
        print(f"  ➜ IMPACT: {delta_retire:+.1f} years difference")
    
    # Peak position distribution
    print(f"\n📈 Peak Position Distribution:")
    control_peaks = Counter([r['peak'] for r in control])
    intervention_peaks = Counter([r['peak'] for r in intervention])
    
    for state in ["Mid-Level", "Senior", "Lead", "Manager", "Director", "VP", "C-Suite"]:
        c_count = control_peaks.get(state, 0)
        i_count = intervention_peaks.get(state, 0)
        c_pct = (c_count / len(control)) * 100
        i_pct = (i_count / len(intervention)) * 100
        delta = i_pct - c_pct
        
        print(f"  {state:12s}: {c_pct:5.1f}% → {i_pct:5.1f}% ({delta:+.1f}%)")
    
    print(f"\n{'=' * 70}")


def plot_intervention_comparison(control, specialist, risktaker):
    """Visualize butterfly effect"""
    fig = plt.figure(figsize=(18, 10))
    
    state_ranks = {
        "Entry Level": 1, "Junior": 2, "Mid-Level": 3,
        "Senior": 4, "Lead": 5, "Manager": 6,
        "Director": 7, "VP": 8, "C-Suite": 9
    }
    
    # Plot 1: Peak Position Comparison
    ax1 = plt.subplot(2, 3, 1)
    
    control_peaks = Counter([r['peak'] for r in control])
    specialist_peaks = Counter([r['peak'] for r in specialist])
    risktaker_peaks = Counter([r['peak'] for r in risktaker])
    
    peak_states = ["Mid-Level", "Senior", "Lead", "Manager", "Director", "VP", "C-Suite"]
    x = np.arange(len(peak_states))
    width = 0.25
    
    control_vals = [(control_peaks.get(s, 0) / len(control)) * 100 for s in peak_states]
    specialist_vals = [(specialist_peaks.get(s, 0) / len(specialist)) * 100 for s in peak_states]
    risktaker_vals = [(risktaker_peaks.get(s, 0) / len(risktaker)) * 100 for s in peak_states]
    
    ax1.bar(x - width, control_vals, width, label='Control', alpha=0.8)
    ax1.bar(x, specialist_vals, width, label='Early Specialization', alpha=0.8)
    ax1.bar(x + width, risktaker_vals, width, label='High Risk', alpha=0.8)
    
    ax1.set_xlabel('Peak Position')
    ax1.set_ylabel('Percentage of Careers')
    ax1.set_title('BUTTERFLY EFFECT: Peak Position by Decision')
    ax1.set_xticks(x)
    ax1.set_xticklabels(peak_states, rotation=45, ha='right')
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    
    # Plot 2: Director+ Achievement Rate
    ax2 = plt.subplot(2, 3, 2)
    
    groups = ['Control', 'Early\nSpecialization', 'High\nRisk']
    director_plus_rates = []
    
    for results in [control, specialist, risktaker]:
        rate = sum(1 for r in results if state_ranks.get(r['peak'], 0) >= 7) / len(results) * 100
        director_plus_rates.append(rate)
    
    colors = ['#3498db', '#e74c3c', '#f39c12']
    bars = ax2.bar(groups, director_plus_rates, color=colors, alpha=0.8)
    ax2.set_ylabel('Percentage Reaching Director+')
    ax2.set_title('Director+ Achievement Rate\n(Quantified Butterfly Effect)')
    ax2.grid(axis='y', alpha=0.3)
    
    # Add percentage labels on bars
    for bar, rate in zip(bars, director_plus_rates):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Plot 3: Retirement Age Distribution
    ax3 = plt.subplot(2, 3, 3)
    
    control_retire = [22 + r['career'].index("Retired") for r in control if "Retired" in r['career']]
    specialist_retire = [22 + r['career'].index("Retired") for r in specialist if "Retired" in r['career']]
    risktaker_retire = [22 + r['career'].index("Retired") for r in risktaker if "Retired" in r['career']]
    
    ax3.hist([control_retire, specialist_retire, risktaker_retire], 
             bins=20, label=['Control', 'Early Spec', 'High Risk'], alpha=0.6)
    ax3.set_xlabel('Retirement Age')
    ax3.set_ylabel('Number of Careers')
    ax3.set_title('Retirement Age Distribution\n(Path-Dependent)')
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)
    
    # Plot 4: Career Trajectory Samples
    ax4 = plt.subplot(2, 3, 4)
    
    sample_size = 50
    control_sample = random.sample([r['career'] for r in control], sample_size)
    
    state_to_num = {state: idx for idx, state in enumerate(STATES)}
    career_matrix = [[state_to_num[state] for state in career] for career in control_sample]
    
    im = ax4.imshow(career_matrix, aspect='auto', cmap='RdYlGn', interpolation='nearest')
    ax4.set_xlabel('Years')
    ax4.set_ylabel('Career Sample')
    ax4.set_title(f'Control Group Trajectories (n={sample_size})')
    
    # Plot 5: Specialist Trajectories
    ax5 = plt.subplot(2, 3, 5)
    
    specialist_sample = random.sample([r['career'] for r in specialist], sample_size)
    career_matrix2 = [[state_to_num[state] for state in career] for career in specialist_sample]
    
    ax5.imshow(career_matrix2, aspect='auto', cmap='RdYlGn', interpolation='nearest')
    ax5.set_xlabel('Years')
    ax5.set_ylabel('Career Sample')
    ax5.set_title(f'Early Specialization Trajectories (n={sample_size})')
    
    # Plot 6: Risk-Taker Trajectories
    ax6 = plt.subplot(2, 3, 6)
    
    risktaker_sample = random.sample([r['career'] for r in risktaker], sample_size)
    career_matrix3 = [[state_to_num[state] for state in career] for career in risktaker_sample]
    
    im = ax6.imshow(career_matrix3, aspect='auto', cmap='RdYlGn', interpolation='nearest')
    ax6.set_xlabel('Years')
    ax6.set_ylabel('Career Sample')
    ax6.set_title(f'High Risk Trajectories (n={sample_size})')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=[ax4, ax5, ax6], location='right', shrink=0.6)
    cbar.set_ticks(range(len(STATES)))
    cbar.set_ticklabels(STATES, fontsize=8)
    
    plt.tight_layout()
    plt.savefig('butterfly_effect_proof.png', dpi=300, bbox_inches='tight')
    print("\n✅ Plots saved to 'butterfly_effect_proof.png'")


def main():
    """Main execution with intervention study"""
    print("=" * 70)
    print("STUPID SIMULATOR v2.0 - BUTTERFLY EFFECT EDITION")
    print("=" * 70)
    
    # Run intervention study
    control, specialist, risktaker = run_intervention_study(num_simulations=2500)
    
    # Quantify effects
    quantify_butterfly_effect(control, specialist, "Early Specialization vs Control")
    quantify_butterfly_effect(control, risktaker, "High Risk vs Control")
    
    # Visualize
    plot_intervention_comparison(control, specialist, risktaker)
    
    print("\n" + "=" * 70)
    print("SIMULATION COMPLETE!")
    print("=" * 70)
    print("\n🎯 Key Insights:")
    print("  • Retirement is now PATH-DEPENDENT (burnout, momentum, level)")
    print("  • Butterfly effect is QUANTIFIED (specific % impacts)")
    print("  • Early decisions have MEASURABLE long-term consequences")
    print("\n📊 Check 'butterfly_effect_proof.png' for visualizations")
    print("=" * 70)


if __name__ == "__main__":
    main()
