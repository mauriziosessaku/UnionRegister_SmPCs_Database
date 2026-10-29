# -*- coding: utf-8 -*-
"""
Figure S1 - Accrual-adjusted specificity of newly introduced MedDRA PTs
========================================================================
Revision analysis added in response to Reviewer #1, comment R1.4:
    "Have the proportions of unique drug-reaction pairs relative to
     ubiquitous reactions changed over time?"

Why an accrual-adjusted design
------------------------------
A naive tabulation - classifying each PT by how many products list it across
the WHOLE corpus and then plotting by year of first appearance - is confounded
by right-censoring: a PT first recorded near the data-lock has had little
calendar time to propagate to further products, so it is almost tautologically
"unique". In our data the naive version rises to ~99% unique for the 2025
cohort purely because of this, not because of biology.

To remove that artefact, this script gives every annual cohort an IDENTICAL
observation window. For each PT it:
  1. determines the year of first appearance (min 'Date Added');
  2. counts the number of distinct products that list the PT WITHIN A FIXED
     K-YEAR WINDOW of that first appearance;
  3. classifies the PT by that windowed count, using the same specificity
     bands as Figure 3C (Unique 1 | Rare 2-5 | Common 6-50 | Ubiquitous >50);
  4. plots the 100% composition of newly introduced PTs per cohort year,
     restricting to cohorts <= (max_year - K) so that a full K-year window is
     observable for every cohort shown.

Interpretation
--------------
Once accrual time is held constant the composition is comparatively stable
across the three decades: newly described terms are predominantly
product-specific or shared with only a few products in every era, and no term
reaches >50 products within K years. The apparent secular drift toward
uniqueness in the uncensored view is therefore largely an accrual artefact.

Reproducibility
---------------
Input : Processed_database.xlsx  (Processed_Database/ folder of the repository)
Output: Figure_S1_specificity_over_time.png  (600 dpi)

Dependencies: pandas, numpy, matplotlib, openpyxl
    pip install pandas numpy matplotlib openpyxl
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
INPUT_XLSX = "Processed_database.xlsx"           # adjust path if needed
OUTPUT_PNG = "Figure_S1_specificity_over_time.png"
ACCRUAL_WINDOW_YEARS = 3                          # K; set to 5 for a stricter window
START_YEAR = 1995
CATEGORY_ORDER = ["Unique (1)", "Rare (2-5)", "Common (6-50)", "Ubiquitous (>50)"]
CATEGORY_COLORS = ["#440154", "#31688e", "#35b779", "#fde725"]   # viridis-consistent


def classify_specificity(n_products: int) -> str:
    """Assign a windowed product count to a sharing band (identical to Fig 3C)."""
    if n_products == 1:
        return "Unique (1)"
    elif n_products <= 5:
        return "Rare (2-5)"
    elif n_products <= 50:
        return "Common (6-50)"
    else:
        return "Ubiquitous (>50)"


def main() -> None:
    K = ACCRUAL_WINDOW_YEARS

    # ---- load ------------------------------------------------------------
    df = pd.read_excel(INPUT_XLSX)
    df["Date Added"] = pd.to_datetime(df["Date Added"], errors="coerce")
    df["Year Added"] = df["Date Added"].dt.year
    max_year = int(df["Year Added"].max())
    last_cohort = max_year - K            # last cohort with a full K-year window

    valid = df.dropna(subset=["MedDRA_PT_Term", "Year Added"]).copy()

    # ---- year each product first lists a given PT ------------------------
    pt_product_year = (
        valid.groupby(["MedDRA_PT_Term", "Brand_Name"])["Year Added"]
        .min()
        .reset_index(name="product_year")
    )
    # ---- global first-appearance year per PT -----------------------------
    pt_first_year = (
        valid.groupby("MedDRA_PT_Term")["Year Added"]
        .min()
        .reset_index(name="first_year")
    )

    merged = pt_product_year.merge(pt_first_year, on="MedDRA_PT_Term")
    # keep only product listings that fall within K years of first appearance
    merged = merged[merged["product_year"] <= merged["first_year"] + K]

    windowed = (
        merged.groupby("MedDRA_PT_Term")["Brand_Name"]
        .nunique()
        .reset_index(name="windowed_product_count")
        .merge(pt_first_year, on="MedDRA_PT_Term")
    )
    windowed["first_year"] = windowed["first_year"].astype(int)
    windowed["Category"] = windowed["windowed_product_count"].apply(classify_specificity)

    # restrict to cohorts with a full K-year observation window
    cohort = windowed[
        (windowed["first_year"] >= START_YEAR) & (windowed["first_year"] <= last_cohort)
    ]

    # ---- yearly 100% composition ----------------------------------------
    counts = (
        cohort.groupby(["first_year", "Category"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=CATEGORY_ORDER, fill_value=0)
    )
    proportions = counts.div(counts.sum(axis=1), axis=0) * 100.0

    # ---- plot ------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11.69, 6.5))
    bottom = np.zeros(len(proportions))
    for category, color in zip(CATEGORY_ORDER, CATEGORY_COLORS):
        ax.bar(
            proportions.index, proportions[category],
            bottom=bottom, label=category, color=color, width=0.85,
        )
        bottom += proportions[category].values

    ax.set_xlabel("Year of first appearance of the MedDRA PT (cohort)", fontsize=12)
    ax.set_ylabel("Proportion of newly introduced PTs (%)", fontsize=12)
    ax.set_ylim(0, 100)
    ax.set_xlim(proportions.index.min() - 0.5, proportions.index.max() + 0.5)
    ax.set_title(
        f"Accrual-adjusted specificity of newly introduced MedDRA PTs "
        f"(fixed {K}-year window)",
        fontsize=12, fontweight="bold",
    )
    ax.legend(
        title=f"Products sharing the PT within {K} years of first appearance",
        fontsize=9, title_fontsize=10, ncol=4, frameon=False,
        loc="upper center", bbox_to_anchor=(0.5, -0.12),
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_PNG, dpi=600, bbox_inches="tight")
    plt.close(fig)

    # ---- console summary -------------------------------------------------
    print(f"Saved: {OUTPUT_PNG}")
    print(f"Accrual window (K)        : {K} years")
    print(f"Cohorts shown             : {int(proportions.index.min())}-{int(proportions.index.max())} "
          f"(data max year {max_year}; cohorts > {last_cohort} excluded)")
    print(f"PTs included              : {len(cohort)}")
    print(f"Reached >50 products in {K}y: {int((cohort['Category']=='Ubiquitous (>50)').sum())}")


if __name__ == "__main__":
    main()
