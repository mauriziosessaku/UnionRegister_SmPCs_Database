# Processed SmPC Adverse Event Database

This folder contains the consolidated, processed database of adverse events extracted from Summary of Product Characteristics (SmPC) documents for all centrally authorized medicinal products in the European Union.

## 📊 Dataset Overview

**File**: `Processed_database.xlsx`

### Key Statistics
- **Total Records**: 110,823 drug-adverse event associations
- **Unique Drugs**: 1,479 active centrally authorized products (CAPs)
- **Date Range**: October 26, 1995 - December 15, 2025 (30 years)
- **Geographic Coverage**: EU centrally authorized products

### Data Composition
- **Clinical Trial Data** (Baseline/Pre-marketing): 82,534 records (74.5%)
- **Post-Approval Discovery** (Post-marketing): 28,289 records (25.5%)

## 📁 File Structure

The Excel file contains a single comprehensive sheet with **36 columns** organized into the following categories:

### 1. Drug Identification
| Column | Description |
|--------|-------------|
| `Brand_Name` | Commercial name of the medicinal product |
| `inn` | International Nonproprietary Name (active substance) |
| `Union_register_eu_num` | EU marketing authorization number |
| `Union_register_mah` | Marketing Authorization Holder |

### 2. Adverse Event Information
| Column | Description |
|--------|-------------|
| `LLM_extracted_AE` | Adverse event text as extracted by the LLM from the SmPC |
| `Source` | Origin: "Clinical Trial (Baseline)" or "Post-Approval Discovery" |
| `Reference Date` | Date of the PRAC meeting (if applicable) |
| `Date Added` | Date when the Adverse Event was added to the SmPC |

### 3. MedDRA Classification (Medical Dictionary for Regulatory Activities v28)
| Column | Description |
|--------|-------------|
| `MedDRA_PT_Term` | Preferred Term |
| `MedDRA_PT_Code` | Numerical code for the Preferred Term |
| `MedDRA_HLT_Term` | High Level Term |
| `MedDRA_HLT_Code` | Numerical code for the High Level Term |
| `MedDRA_HLGT_Term` | High Level Group Term |
| `MedDRA_HLGT_Code` | Numerical code for the High Level Group Term |
| `MedDRA_SOC_Term` | System Organ Class |
| `MedDRA_SOC_Code` | Numerical code for the System Organ Class |
| `MedDRA_Match_Method` | The specific method used for MedDRA mapping |

**Match Method Distribution**:
- Exact Match (MedDRA v28 PT dictionary): 73.5%
- SOC-Filtered Batch Match (DeepSeek R1): 22.2%
- No Match/Manual Assignment: 0.5%

### 4. ATC Classification (Anatomical Therapeutic Chemical)
Complete 5-level WHO ATC hierarchy:

| Level | Columns | Example Description |
|-------|---------|---------|
| Level 1 | `ATC_Level_1_Code`, `ATC_Level_1_Desc` | Alimentary tract |
| Level 2 | `ATC_Level_2_Code`, `ATC_Level_2_Desc` | Drugs used in diabetes |
| Level 3 | `ATC_Level_3_Code`, `ATC_Level_3_Desc` | Therapeutic/Pharmacological Subgroup |
| Level 4 | `ATC_Level_4_Code`, `ATC_Level_4_Desc` | Chemical/Therapeutic/Pharmacological Subgroup |
| Level 5 | `ATC_Level_5_Code`, `ATC_Level_5_Desc` | Specific substance |

### 5. Regulatory Metadata (Union Register)
| Column | Description |
|--------|-------------|
| `Union_register_close_date` | Date the SmPC procedure was closed |
| `Union_register_procedure` | Type of regulatory procedure |
| `Union_register_Ema_number` | EMA procedure reference number |
| `Union_register_decisio_number` | European Commission (EC) decision number |
| `Union_register_decision_date` | Date of the EC decision |
| `Union_register_link` | URL to the official EC document |
| `Union_register_indication` | Approved therapeutic indication for the drug |
| `Union_register_atc` | Full ATC classification provided in JSON format |

### 6. Traceability
| Column | Description |
|--------|-------------|
| `Source_File` | Original source file name for audit trail purposes |

## 📈 Data Distribution

### Top Therapeutic Area (ATC Level 1)
- **Antineoplastic and immunomodulating agents**: 45,612 associations (44.7% of total dataset)

### Top 3 System Organ Classes (MedDRA SOC)
1. **Gastrointestinal disorders**: 11,613 associations (10.9%)
2. **Skin and subcutaneous tissue disorders**: 9,924 associations (9.0%)
3. **Nervous system disorders**: 9,901 associations (9.3%)

## 🔍 Use Cases

This database supports multiple research applications:

### 1. Signal Detection Benchmarking
- Evaluate performance of statistical methods.
- Compare methodological approaches.

### 2. Temporal Analysis
- Track adverse event emergence over time using time-indexed reference dates.
- Restrict analyses to pre-confirmation periods to evaluate early detection performance.
- Study pre-market vs. post-market safety profiles.

### 3. Pharmacovigilance Research
- Analyze therapeutic area-specific safety profiles.
- Compare systematic differences in safety profiles between small molecules and biological/targeted therapies.

## 💻 Loading the Data

### Python (pandas)
```python
import pandas as pd

# Load the database
df = pd.read_excel('Processed_database.xlsx')

# Display basic info
print(f"Total records: {len(df):,}")
print(f"Columns: {df.columns.tolist()}")

# Filter for post-approval discoveries
post_approval = df[df['Source'] == 'Post-Approval Discovery']
print(f"Post-approval AEs: {len(post_approval):,}")

# Group by therapeutic area
by_atc = df.groupby('ATC_Level_1_Desc').size().sort_values(ascending=False)
print("\nTop therapeutic areas:")
print(by_atc.head(10))

# Find specific drug
drug_data = df[df['Brand_Name'] == 'Abasaglar']
print(f"\nAbasaglar has {len(drug_data)} AE records")
```

### R
```r
library(readxl)
library(dplyr)

# Load the database
df <- read_excel('Processed_database.xlsx')

# Display structure
str(df)
dim(df)

# Summary statistics
summary(df)

# Filter and analyze
post_approval <- df %>% 
  filter(Source == 'Post-Approval Discovery')

by_soc <- df %>% 
  group_by(MedDRA_SOC_Term) %>% 
  summarise(count = n()) %>% 
  arrange(desc(count))
```

### Excel
Simply open `Processed_database.xlsx` in Microsoft Excel, LibreOffice Calc, or Google Sheets.

**Recommended**: Use Excel's built-in features:
- **Filters**: Enable AutoFilter on headers (Data → Filter)
- **Pivot Tables**: Summarize by ATC, SOC, or Source
- **Conditional Formatting**: Highlight date ranges or specific drugs

## 🔗 Data Lineage

This processed database was created through the following pipeline:

```text
European Commission's Union Register of Medicinal Products
    ↓
SmPC PDFs (1,513 CAPs)
    ↓
LLM Extraction (DeepSeek V3) → Section 4.8 Adverse Events
    ↓
MedDRA Mapping v28 (Exact String Match & SOC-Filtered Batch Match)
    ↓
ATC Code Integration (WHO Classification)
    ↓
Processed_database.xlsx (This file)
```

## 📋 Data Quality

### Extraction Accuracy
- **LLM Extraction**: 95.1% accuracy (validated manually by MK and STB on the latest SmPCs)
- **MedDRA Mapping**: 95.7% overall success rate (73.5% exact, 22.2% SOC-filtered)

### Known Limitations
- **Coverage**: Only EU centrally authorized products (CAPs); nationally authorized products are not included.
- **Temporal Anchor**: The SmPC regulatory closing date represents the formal update approval date, not the date of first identification of the safety signal.

## 📅 Version Information

- **Data Lock Point**: December 15, 2025

## 🔒 Data Ethics & Usage

### Permitted Uses
✅ Academic research  
✅ Pharmacovigilance methodology development  
✅ Signal detection algorithm benchmarking  
✅ Educational purposes  
✅ Public health research  

### Citation
If you use this database in your research, please cite:

```bibtex
@article{kefala2026development,
  author = {Kefala, Maria and Painter, Jeffrey L. and Bukhari, Syed Tauhid and Powell, and Sessa, Maurizio},
  title = {Development of a European Union Time-indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance},
  year = {2026},
  journal = {Original Article}
}
```

## 📧 Contact & Support

For questions, issues, or collaboration:
- **Email**: maurizio.sessa@sund.ku.dk
- **Corresponding Author**: Maurizio Sessa
- **Institution**: Department of Drug Design and Pharmacology, University of Copenhagen

## 📚 Related Resources

- **GitHub Repository**: https://github.com/mauriziosessaku/UnionRegister_SmPCs_Database
- **Methodology**: See full manuscript for detailed methodology.

## ⚠️ Disclaimer

This database is derived from publicly available regulatory documents (SmPCs) published by the European Commission. The data is provided for research purposes only and should not be used as the sole basis for clinical or regulatory decisions. Always refer to official SmPC documents for the most current safety information.
