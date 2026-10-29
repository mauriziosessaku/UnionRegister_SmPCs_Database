# Revision analyses and figures — CTS-2026-0457-T

This folder documents the analyses and figures added to the manuscript
**"Development of a European Union Time-Indexed Reference Dataset for Assessing the
Performance of Signal Detection Methods in Pharmacovigilance using a Large Language Model"**
during peer review at *Clinical and Translational Science*.

It is an **addendum** to `Software/manuscript_analysis.py`; the original analysis code is unchanged.
Everything here is reproducible from the published dataset
[`Processed_Database/Processed_database.xlsx`](../Processed_Database/Processed_database.xlsx).

## Contents

| File | Description |
|------|-------------|
| `Revision_Analyses.ipynb` | Google Colab / Jupyter notebook reproducing **all** revision analyses and figures (Rounds 1 & 2). |
| `union_register_source_example.png` | Screenshot of the `view-source:` of a Union Register product page (Kineret, h203.htm), illustrating R2.1. |
| `union_register_source_excerpt.js` | Trimmed, annotated copy of the embedded data arrays from that page. |
| `REVISIONS_README.md` | This file. |

## How to run

**Google Colab**
1. Open `Revision_Analyses.ipynb` in Colab.
2. Upload `Processed_database.xlsx` to the session (or mount Google Drive) and set, in the first code cell,
   `DATA_PATH = "/content/Processed_database.xlsx"` (or an environment variable `DATA_PATH`).
3. *Runtime → Run all.* Figures are written to `revision_figures/` at 600 dpi.

**Local**
```bash
pip install pandas numpy matplotlib seaborn openpyxl "plotly==5.24.1" "kaleido==0.2.1" jupyter
DATA_PATH=/path/to/Processed_database.xlsx jupyter nbconvert --to notebook --execute --inplace Revision_Analyses.ipynb
```

> The sunburst in Figure 3 (Panel D) is rendered with Plotly + Kaleido. The pinned versions
> `plotly==5.24.1` and `kaleido==0.2.1` are used because newer Kaleido (≥1.0) changes the static-image API.

## What was changed, and why (mapping to reviewer comments)

### Round 1 — Reviewer #1
| Ref | Change | Where |
|-----|--------|-------|
| **R1.4** | New **Figure S1**: accrual-adjusted specificity of newly introduced MedDRA PTs over time, using a fixed *K*-year window (default 3) so every annual cohort has an equal observation period. Shows that the apparent drift toward "unique" terms in a naive tabulation is largely a **right-censoring artefact**. | Notebook §6; Supplementary (Figure S1) |
| **R1.5** | **Figure 2, Panel B** y-axis ordered from most to least frequent for small molecules. | Notebook §3 |
| **R1.6** | **Figure 3, Panel A** now shows the full **WHO ATC level-1 names** beside each code. | Notebook §4 |
| **R1.7** | **Figure 4, Panel A** axes relabelled (*Unique MedDRA PTs per Drug* vs *Number of Drugs*). | Notebook §5 |

### Round 2 — Reviewer #2
| Ref | Change | Where |
|-----|--------|-------|
| **R2.1** | Data sources enumerated (three source corpora + two reference dictionaries) and the 36 metadata variables listed by origin. | Notebook §8; Methods §2.1 |
| **R2.3** | **Figure 1, Panel B** now overlays the **standardised per-product rate** of post-approval AE additions on the absolute annual count. The absolute count peaks ~2012, but the **per-product rate peaks in the mid-2000s and declines** — the absolute peak reflects portfolio growth. | Notebook §2 |
| **R2.6** | **Figure 3, Panel C** renamed *"Cross-product sharing of adverse-event terms"*; x-axis *"Number of distinct products in which the PT appears"* (bands Unique/Rare/Common/Ubiquitous); the term *"uniquity"* removed; classification defined in Methods §2.2.4. | Notebook §4 |
| **R2.8** | **Figure 4** Panels A & B axis labels clarified (*… per Drug* / *Number of Drugs*). | Notebook §5 |
| **R2.9** | **MedDRA mapping reconciliation**: full accounting over all 110,823 associations — 95.7% automated (73.5% exact + 22.2% SOC-filtered), 0.5% manual after no automated match, <0.01% errors, and 3.7% retained without a MedDRA PT (excluded from PT-level analyses). Now sums to 100%. | Notebook §7; Results §3.3 |

## Data-source example: the Union Register HTML source (R2.1)

The regulatory and pharmacological metadata are parsed directly from the **HTML source** of each
Union Register product page — not scraped from rendered tables. Each page embeds its data as
JavaScript variables (`dataSet_product_information`, `dataSet_proc`); the pipeline reads these.

- Example product: **Kineret** (anakinra)
- URL: `https://ec.europa.eu/health/documents/community-register/html/h203.htm`
  (to inspect, prefix with `view-source:` in the browser)

![view-source of a Union Register product page (Kineret)](union_register_source_example.png)

A trimmed copy of the embedded arrays is in `union_register_source_excerpt.js`. Field mapping:

| Source field | Processed-database variable(s) |
|---|---|
| `name.value` | `Brand_Name` |
| `eu_num.value` | `Union_register_eu_num` |
| `inn.value` | `inn` |
| `mah.value` (+ `meta.address`) | `Union_register_mah` |
| `atc.meta[0]` (levels 1–5) | `ATC_Level_1..5_Code` / `_Desc`, `Union_register_atc` |
| `ema_links.meta[].url` | `Union_register_link` |
| `proc[].closed` | `Union_register_close_date` → **Date Added / Reference Date** (temporal anchor) |
| `proc[].type` | `Union_register_procedure` |
| `proc[].ema_number` | `Union_register_Ema_number` |
| `proc[].decision.number` / `.date` | `Union_register_decisio_number` / `Union_register_decision_date` |

Notebook §9 parses an offline copy of these arrays to demonstrate the mechanism without network access.

## Specificity bands (used in Figure 3C and Figure S1)

Each MedDRA Preferred Term is classified by the number of distinct products in which it appears:

| Band | Products |
|------|----------|
| Unique | 1 |
| Rare | 2–5 |
| Common | 6–50 |
| Ubiquitous | > 50 |

For Figure S1 the count is restricted to a fixed *K*-year window from the term's first appearance.

## Notes
- Figures are regenerated from the current `Processed_database.xlsx`; minor numeric drift versus the
  submitted manuscript can occur if the dataset is updated. The qualitative conclusions are unaffected.
- The notebook does not alter the dataset; it only reads it.
