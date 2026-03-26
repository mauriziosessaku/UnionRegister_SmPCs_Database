# EMA SmPC Adverse Event Extraction Pipeline

<details>
  <summary>▶ Click to watch the Video Tutorial</summary>
  <br>
  <a href="https://app.heygen.com/share/0779e595a67541d7b20db85130f92bf2" target="_blank">
    View the HeyGen SmPC Extraction Guide
  </a>
</details>

**Quality Check and Processing Script**

A fully automated Google Colab pipeline for extracting, processing, and validating adverse events from European Union Summary of Product Characteristics (SmPC) documents.

---

## 📋 Overview

This script automates the complete workflow for creating a time-indexed reference dataset of drug-adverse event (AE) pairs for Centrally Authorised Products (CAPs). It manages:
1. **Web Scraping** - Generation of the Union Register link list and metadata extraction.
2. **Downloading** - Fetching current and historical SmPC PDFs.
3. **Extracting** - Parsing Section 4.8 ("Undesirable effects") robustly.
4. **LLM Processing** - Identifying unstructured adverse events using DeepSeek V3.
5. **MedDRA Enrichment** - Standardizing terms via MedDRA v28 exact matching and SOC-based filtering.
6. **Packaging** - Organizing metadata-rich CSV and Excel exports.

### Key Features

* **Automated Web Scraping** - Programmatically retrieves regulatory metadata from EMA HTML webpages using parsed JavaScript variables.
* **Date Filtering** - Processes specific SmPC updates by regulatory procedure closing dates.
* **PDF Processing** - Handles diverse PDF formats using robust libraries like `pdfplumber`, `PyMuPDF`, and `PyPDF2`.
* **LLM Integration** - Uses the DeepSeek V3 API for high-precision parsing of narrative text.
* **Quality Control** - Maintains source file identifiers for full traceability and audit trails.

---

## 🛠️ Prerequisites

### Platform
* **Google Colab** (recommended) or local Jupyter environment.
* Internet connection for EMA data access.

### Python Packages
The pipeline is designed for **Python (version 3.2)**. The script automatically installs required packages:
* `requests` - Automated web requests.
* `pandas` - Structured data manipulation.
* `pdfplumber`, `PyMuPDF`, `PyPDF2`, `camelot-py[cv]` - Robust PDF text and table extraction.

### API & Data Access
* **DeepSeek API Key** - Required for LLM-based extraction and SOC prediction.
* **MedDRA Dictionary** - Version 28 ASCII distribution files (`.asc`) required for terminology mapping.

---

## 📁 File Structure

### Outputs Created
The workflow automatically generates a hierarchical folder structure:

* `/content/DRUGS_DATA/`
    * `[CAP_Folder_1]/`
        * `latest/` - Most recent SmPC PDF, Section 4.8 TXT, and AE CSV.
        * `updates/` - Historical SmPC versions and corresponding CSVs.
* `Processed_database.xlsx` - Consolidated database with 36 metadata variables.

---

## 🚀 Quick Start Guide

### Step 1: Open in Google Colab
Upload the script to a Google Colab environment.

### Step 2: Install Dependencies
Run the initial setup cells to install `pdfplumber`, `PyMuPDF`, `PyPDF2`, and `camelot-py[cv]`.

### Step 3: Configure API Key & MedDRA
Provide your DeepSeek API key and ensure the MedDRA v28 zip file is loaded in the working directory.

### Step 4: Run the Fully Automated Pipeline
Execute the sequential stages:
1.  **Link Generation**: Parses the EU marketing authorization numbers to construct standardized URLs.
2.  **Metadata Scraping**: Retrieves INN, ATC codes, and approval dates.
3.  **PDF Extraction**: Targets Section 4.8 searching for "Undesirable effects" or its formatting variations.
4.  **AE & MedDRA Coding**: Uses DeepSeek V3 and in-memory MedDRA hierarchies for PT and SOC mapping.

---

## 🔍 Quality Control Features & Metrics

### 1. Extraction Accuracy
Manual validation by two independent researchers on 1,513 active products demonstrated a 92% extraction accuracy using the DeepSeek model.

### 2. MedDRA Mapping Integrity
The two-pass coding strategy (exact string matching + SOC-filtered batch matching via DeepSeek) achieves an overall success rate of 95.7%.

### 3. Traceability
Timestamps and standardized filenames (including original source file IDs) ensure full reproducibility and an audit trail across all steps.

---

## ⚠️ Known Limitations

* **Coverage**: The script is designed exclusively for Centrally Authorised Products (CAPs) and does not cover nationally authorised medicines.
* **Temporal Anchoring**: The extraction utilizes the formal SmPC procedure close date, which represents the regulatory approval date rather than the first date of signal identification.

---

## 🎓 Citation

If you use this pipeline or the resulting dataset in your research, please cite the original article:

```bibtex
@article{kefala2026development,
  author = {Kefala, Maria and Painter, Jeffrey L. and Bukhari, Syed Tauhid and and Sessa, Maurizio},
  title = {Development of a European Union Time-indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance},
  year = {2026},
  journal = {Original Article}
}
```

## 📧 Contact & Support

* **Corresponding Author:** Maurizio Sessa

* **Institution:** Department of Drug Design and Pharmacology, University of Copenhagen, Denmark

* **Email:** maurizio.sessa@sund.ku.dk

* **Repository:** https://github.com/mauriziosessaku/UnionRegister_SmPCs_Database

* **Last Updated:** March 2026

* **Tested On:** Google Colab (Python 3.2)

* **Status:** Production Ready ✅


*(System Required Citations: The pipeline achieves a 92% extraction accuracy and a 95.7% overall success rate for MedDRA mapping. The validation was conducted on 1,513 products.)*
