# Processed SmPC Adverse Event Database

This folder contains the consolidated, processed database of adverse events extracted from Summary of Product Characteristics (SmPC) documents for all centrally authorized medicinal products in the European Union.

## 📊 Dataset Overview

**File**: `Processed_database.xlsx`

### Key Statistics
- **Total Records**: 110,548 drug-adverse event associations
- **Unique Drugs**: 1,481 brand names
- **Unique Active Substances (INN)**: 1,078
- **Unique Adverse Events**: 15,002 distinct events
- **Date Range**: October 1995 - December 2025 (30 years)
- **Geographic Coverage**: EU centrally authorized products

### Data Composition
- **Clinical Trial Data** (Baseline): 82,434 records (74.6%)
- **Post-Approval Discovery**: 28,114 records (25.4%)

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
| `LLM_extracted_AE` | Adverse event as extracted by LLM from SmPC |
| `Source` | Origin: "Clinical Trial (Baseline)" or "Post-Approval Discovery" |
| `Reference Date` | Date of PRAC meeting (if applicable) |
| `Date Added` | Date when AE was added to SmPC |

### 3. MedDRA Classification (Medical Dictionary for Regulatory Activities)
| Column | Description |
|--------|-------------|
| `MedDRA_PT_Term` | Preferred Term (most specific level) |
| `MedDRA_PT_Code` | Preferred Term code |
| `MedDRA_HLT_Term` | High Level Term |
| `MedDRA_HLT_Code` | High Level Term code |
| `MedDRA_HLGT_Term` | High Level Group Term |
| `MedDRA_HLGT_Code` | High Level Group Term code |
| `MedDRA_SOC_Term` | System Organ Class (highest level) |
| `MedDRA_SOC_Code` | System Organ Class code |
| `MedDRA_Match_Method` | Method used for MedDRA mapping |

**Match Method Distribution**:
- Exact Match: 81,273 (73.5%)
- SOC-Filtered Batch Match: 24,549 (22.2%)
- No Match: 591 (0.5%)
- Error: 2 (<0.01%)

### 4. ATC Classification (Anatomical Therapeutic Chemical)
Complete 5-level WHO ATC hierarchy:

| Level | Columns | Example |
|-------|---------|---------|
| Level 1 | `ATC_Level_1_Code`, `ATC_Level_1_Desc` | A - Alimentary tract and metabolism |
| Level 2 | `ATC_Level_2_Code`, `ATC_Level_2_Desc` | A10 - Drugs used in diabetes |
| Level 3 | `ATC_Level_3_Code`, `ATC_Level_3_Desc` | A10A - Insulins and analogues |
| Level 4 | `ATC_Level_4_Code`, `ATC_Level_4_Desc` | A10AE - Long-acting insulins |
| Level 5 | `ATC_Level_5_Code`, `ATC_Level_5_Desc` | A10AE04 - Insulin glargine |

### 5. Regulatory Metadata (Union Register)
| Column | Description |
|--------|-------------|
| `Union_register_close_date` | Date SmPC procedure was closed |
| `Union_register_procedure` | Type of regulatory procedure |
| `Union_register_Ema_number` | EMA procedure reference number |
| `Union_register_decisio_number` | EC decision number |
| `Union_register_decision_date` | Date of EC decision |
| `Union_register_link` | URL to official EC document |
| `Union_register_indication` | Approved therapeutic indication |
| `Union_register_atc` | Full ATC classification (JSON format) |

### 6. Traceability
| Column | Description |
|--------|-------------|
| `Source_File` | Original source file for audit trail |

## 📈 Data Distribution

### Top 10 Therapeutic Areas (ATC Level 1)
1. **Antineoplastic and immunomodulating agents**: 45,612 records (41.3%)
2. **Nervous system**: 12,301 records (11.1%)
3. **Antiinfectives for systemic use**: 11,761 records (10.6%)
4. **Alimentary tract and metabolism**: 7,090 records (6.4%)
5. **Blood and blood forming organs**: 6,279 records (5.7%)
6. **Cardiovascular system**: 4,680 records (4.2%)
7. **Sensory organs**: 2,855 records (2.6%)
8. **Musculo-skeletal system**: 2,670 records (2.4%)
9. **Genito urinary system and sex hormones**: 2,665 records (2.4%)
10. **Respiratory system**: 2,187 records (2.0%)

### Top 10 System Organ Classes (MedDRA SOC)
1. **Gastrointestinal disorders**: 11,613 records (10.5%)
2. **Skin and subcutaneous tissue disorders**: 9,924 records (9.0%)
3. **Nervous system disorders**: 9,901 records (9.0%)
4. **General disorders and administration site conditions**: 7,914 records (7.2%)
5. **Investigations**: 7,489 records (6.8%)
6. **Vascular disorders**: 5,940 records (5.4%)
7. **Respiratory, thoracic and mediastinal disorders**: 5,370 records (4.9%)
8. **Infections and infestations**: 5,209 records (4.7%)
9. **Musculoskeletal and connective tissue disorders**: 5,111 records (4.6%)
10. **Psychiatric disorders**: 4,914 records (4.4%)

## 🔍 Use Cases

This database supports multiple research applications:

### 1. Signal Detection Benchmarking
- Evaluate performance of statistical methods (PRR, ROR, EBGM, IC)
- Test machine learning algorithms for safety signal detection
- Compare traditional vs. AI-based approaches

### 2. Temporal Analysis
- Track adverse event emergence over time
- Calculate time-to-detection metrics
- Study pre-market vs. post-market safety profiles

### 3. Pharmacovigilance Research
- Identify patterns in adverse event reporting
- Analyze therapeutic area-specific safety profiles
- Study regulatory decision-making timelines

### 4. Data Mining
- Explore drug-event associations
- Identify rare or delayed adverse events
- Support hypothesis generation for safety studies

### 5. Educational Purposes
- Teach pharmacovigilance methodologies
- Demonstrate real-world safety surveillance
- Train on medical terminology (MedDRA, ATC)

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

```
Union Register (EC) 
    ↓
SmPC PDFs (1,514 drugs × 16,594 updates)
    ↓
LLM Extraction (DeepSeek AI) → Section 4.8 Adverse Events
    ↓
MedDRA Mapping (Hierarchical Classification)
    ↓
ATC Code Integration (WHO Classification)
    ↓
PRAC Signal List Matching (2012-2025)
    ↓
Processed_database.xlsx (This file)
```

## 📋 Data Quality

### Extraction Accuracy
- **LLM Extraction**: 92% accuracy (validated on 1,514 latest SmPCs)
- **MedDRA Mapping**: 95.7% successfully mapped (Exact or SOC-Filtered)
- **Data Completeness**: All 36 fields populated for regulatory records

### Validation Steps Applied
1. ✅ Manual validation of LLM extractions (sample-based)
2. ✅ MedDRA terminology standardization
3. ✅ ATC code verification against WHO database
4. ✅ Duplicate detection and removal
5. ✅ Date range validation (1995-2025)
6. ✅ Source file traceability maintained

### Known Limitations
- **Coverage**: Only EU centrally authorized products (no nationally authorized drugs)
- **Language**: Extracted from English-language SmPCs
- **Granularity**: Frequency information (very common, common, etc.) not extracted
- **Causality**: Associations do not imply causation
- **Completeness**: Missing data for 33 withdrawn products

## 📅 Version Information

- **Version**: 1.0
- **Last Updated**: January 2026
- **Data Cutoff**: December 8, 2025
- **Processing Date**: January 2026

## 🔒 Data Ethics & Usage

### Permitted Uses
✅ Academic research  
✅ Pharmacovigilance methodology development  
✅ Signal detection algorithm benchmarking  
✅ Educational purposes  
✅ Public health research  

### Restrictions
❌ Not for clinical decision-making without expert review  
❌ Not a substitute for official SmPC documents  
❌ Not for commercial drug development without proper licensing  
❌ Not for identifying individual patients or cases  

### Citation
If you use this database in your research, please cite:

```bibtex
@dataset{bukhari2026smpc,
  author = {Bukhari, Syed Tauhid and Sessa, Maurizio},
  title = {Processed SmPC Adverse Event Database: A Dynamic Reference Set 
           for Pharmacovigilance Signal Detection},
  year = {2026},
  institution = {University of Copenhagen},
  version = {1.0},
  note = {Data extracted from EU Union Register, covering 1,514 centrally 
          authorized products from 1995-2025}
}
```

## 🔄 Updates & Maintenance

This database will be updated periodically to include:
- New centrally authorized products
- Updated SmPC versions
- New PRAC signal decisions
- Enhanced MedDRA mappings

**Next scheduled update**: Q3 2026

## 📧 Contact & Support

For questions, issues, or collaboration:
- **Email**: maurizio.sessa@sund.ku.dk
- **Author**: Syed Tauhid Bukhari
- **Supervisor**: Maurizio Sessa
- **Institution**: University of Copenhagen

## 📚 Related Resources

- **Raw Data**: See `/data/` folder for original SmPC files
- **Extraction Scripts**: See `/extract_*.py` files in repository
- **Analysis Scripts**: See `/analysis/` folder
- **Database Viewer**: Access via SmPC Database Viewer interface
- **Methodology**: See full thesis document for detailed methodology

## ⚠️ Disclaimer

This database is derived from publicly available regulatory documents (SmPCs) published by the European Commission. The data is provided for research purposes only and should not be used as the sole basis for clinical or regulatory decisions. Always refer to official SmPC documents for the most current safety information.

---

**Last updated**: January 23, 2026  
**File size**: ~50MB (compressed)  
**Format**: Microsoft Excel (.xlsx)  
**Encoding**: UTF-8

