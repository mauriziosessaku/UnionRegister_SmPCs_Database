# European Union time-indexed reference dataset for pharmacovigilance signal detection

This repository accompanies the manuscript **“Development of a European Union Time-Indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance using a Large Language Model”** (Kefala, Painter, Bukhari, and Sessa; manuscript under revision at *Clinical and Translational Science*).

It provides an EU-focused, time-indexed reference dataset of adverse events (AEs) first reported in the Summary of Product Characteristics (SmPC) of centrally authorised products (CAPs), together with extraction, terminology-mapping, and analysis code.

## Scope and key figures

**Source manuscript:** revised clean version supplied for CTS manuscript **CTS-2026-0457-T**. **Data lock:** 15 December 2025. The values below refer to two different dataset scopes and should not be interchanged.

| Measure | Complete historical database | Processed time-indexed reference dataset |
| --- | ---: | ---: |
| Centrally authorised products | 1,513 CAPs | 1,479 active CAPs |
| Drug–AE associations | 125,026 | 110,823 |
| SmPC versions | 17,763, across the historical collection | Derived from the historical SmPC collection |
| Observation period | 26 October 1995 – 15 December 2025 | Same historical source period |

In the **processed dataset**, 82,534 drug–AE associations (74.5%) were classified as **baseline/pre-marketing**, and 28,289 (25.5%) as **post-approval discoveries**. Its Excel file contains **36 variables** covering product identification, AE information, the MedDRA hierarchy, five-level WHO ATC coding, regulatory metadata, and source traceability.

A drug–AE pair's time index is the first identified inclusion in the SmPC, anchored to the available regulatory procedure-closing date. **This is not necessarily the date when a signal was first detected or validated.** The dataset supports research and methodological benchmarking; labelled associations are not a substitute for case-level clinical causality assessment.

## Data sources and five-stage workflow

1. **Product index:** generate a list of EU centrally authorised products using the European Commission Union Register brand index, supplemented with relevant European Medicines Agency (EMA) public product metadata.
2. **Regulatory metadata:** extract product and regulatory-procedure information from the Union Register and associated public EMA resources (including the relevant webpage metadata).
3. **SmPC extraction:** retrieve current and historical SmPC PDFs and extract Section 4.8 (“Undesirable effects”) text.
4. **AE extraction:** use **DeepSeek V3**, accessed through the `deepseek-chat` API endpoint with temperature 0, to identify individual AE expressions and produce structured files.
5. **MedDRA v28 enrichment:** use case-insensitive exact matching to Preferred Terms (PTs), followed where needed by LLM-guided SOC-filtered matching; attach the PT→HLT→HLGT→SOC hierarchy.

The model used for extraction is **DeepSeek V3**, **not DeepSeek R1**. An article describing DeepSeek-R1 cited in a manuscript bibliography should not be interpreted as the model used by this pipeline.

## Validation and terminology mapping

For the **most recent SmPC versions across the included products**, two researchers (MK and STB) manually checked extracted AEs, drug identification fields, and available regulatory metadata against the source documents and webpages. The manuscript reports **95.1% AE extraction accuracy**. Validation statuses included correct, incorrect, missing, duplicate, and triplicate items. See [Validation_dataset](Validation_dataset/) for the validation materials.

The manuscript reports a **95.7% MedDRA terminology-mapping success rate**, comprising **73.5% exact matches** and **22.2% SOC-filtered matches**. These percentages describe reported mapping outcomes; they do not independently establish the semantic correctness of every individual assigned PT.

**Structural limitation:** the original hierarchy reconstruction retains a single SOC relationship for a multi-axial PT based on dictionary loading order, without explicitly selecting the MedDRA-designated primary SOC. The associated SOC-level summaries should be interpreted with that limitation in mind (see Supplementary Methods S1).

## Repository contents

| Path | Contents |
| --- | --- |
| [Database](Database/) | Instructions for accessing the historical extracted SmPC database archive |
| [Processed_Database/Processed_database.xlsx](Processed_Database/Processed_database.xlsx) | Processed database for 1,479 active CAPs (110,823 drug–AE records) |
| [Validation_dataset](Validation_dataset/) | Manually reviewed validation materials |
| [Software/Software.py](Software/Software.py) | Product metadata retrieval, SmPC Section 4.8 extraction, and LLM AE extraction |
| [Software/soc_filtering_matching.py](Software/soc_filtering_matching.py) | MedDRA v28 terminology mapping |
| [Software/data_pre_processing.py](Software/data_pre_processing.py) | Product index and preprocessing |
| [Software/manuscript_analysis.py](Software/manuscript_analysis.py) | Descriptive analyses and figures in the manuscript |
| [Software/figure_s1_specificity_over_time.py](Software/figure_s1_specificity_over_time.py) | Three-year accrual-adjusted PT specificity analysis |

The descriptive analyses cover temporal accrual, baseline versus post-marketing additions, regulatory procedures, PT/SOC counts per drug, ATC therapeutic areas, drug-type SOC profiles, and time to first label update. Figure S1 uses a **fixed three-year observation window** for first-appearance PT cohorts through **2022**, limiting right-censoring bias in recent years.

## Reproducibility and use

The code was developed in a Python/Google Colab workflow. Required dependencies include pandas, requests, and PDF/text-processing libraries. Re-running terminology enrichment requires licensed access to **MedDRA v28 ASCII files**; running live extraction also requires access to the relevant source documents and a DeepSeek API key. The deposited spreadsheet is a snapshot at the stated data lock and is not automatically updated by GitHub.

The associated manuscript and Supplementary Methods S1 are the scientific reference for dataset definitions, validation design, and interpretation. When manuscript and an older README disagree, use the **revised manuscript** as the reference and report any remaining discrepancies.

## Contact

**Maurizio Sessa**, Department of Drug Design and Pharmacology, University of Copenhagen — maurizio.sessa@sund.ku.dk

## Disclaimer

This resource is intended for research and methodological evaluation, not as the sole basis for a clinical or regulatory decision. Consult current official SmPCs for up-to-date product safety information.
