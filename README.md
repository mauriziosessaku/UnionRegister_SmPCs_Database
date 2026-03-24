# Development of a European Union Time-indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance

A comprehensive system for extracting and analyzing adverse events from European Union Summary of Product Characteristics (SmPC) documents to create a dynamic, time-indexed reference dataset for benchmarking signal detection methods in pharmacovigilance.

## 📋 Overview

This project addresses a critical gap in pharmacovigilance research by developing a time-indexed reference dataset for the European Union (EU). The database includes 17,761 SmPC versions spanning from 1995 to 2025, comprising 123,868 drug–adverse event (AE) associations. The processed database for active centrally authorized products (CAPs) includes 1,479 medicinal products and 110,548 drug-event associations.

## 🎯 Motivation

The identification of optimal signal detection methods is hindered by the lack of reliable reference datasets. Existing datasets do not capture when adverse events (AEs) are officially recognized by regulatory authorities. This limitation prevents the restriction of analyses to pre-confirmation periods and limits the evaluation of early detection performance. 

## 🚀 Methodology and Features

The data processing workflow consists of sequential and fully automated stages:

* **Generation of the Union Register Link List**: Standardized URLs are constructed for each product to point to dedicated Union Register pages.
* **Web Scraping and Metadata Extraction**: Product information and regulatory procedure records are programmatically retrieved from EMA public HTML webpages.
* **PDF Download and Section 4.8 Extraction**: SmPC PDFs are downloaded and the "Undesirable effects" section is extracted using `pdfplumber`.
* **AE Extraction and Structured Data Output**: Extracted texts are processed using the DeepSeek R1 API to identify individual AEs.
* **MedDRA v28 Enrichment**: Unique AE terms are encoded against MedDRA version 28 using exact string matching and a System Organ Class (SOC)-based filtering strategy with DeepSeek.

## 📈 Analysis Capabilities

The repository includes code to replicate the statistical analyses and figures presented in the manuscript, including:

* Longitudinal growth of the database and temporal trends in safety label updates.
* Stratification of drug-AEs by discovery phase, specifically pre-marketing versus post-marketing.
* Quantification of MedDRA SOC coverage and ubiquity across the product population.
* Density metrics of safety information per medicinal product.
* Comparative analyses across therapeutic areas using WHO ATC level 1 hierarchy.
* Mechanism-based safety profile comparisons between small molecules and biological/targeted therapies.
* Kaplan-Meier survival analysis for time-to-first SmPC update.

## 💻 Technical Stack

* **Languages**: Python (version 3.2) and R (version RStudio 2026.01.0).
* **Environment**: Google Colab.
* **AI Models**: DeepSeek R1 for unstructured narrative text parsing and SOC predictions.
* **Key Python Libraries**: `requests` for web requests.
* **Key Python Libraries**: `pandas` for structured data manipulation.
* **Key Python Libraries**: `re` and `json` for parsing embedded web content.
* **Key Python Libraries**: `pdfplumber`, `PyMuPDF`, `PyPDF2`, and `camelot-py[cv]` for robust text extraction from PDFs.

## 📊 Data Sources

* **European Commission’s Union Register of Medicinal Products**: Sourced with a data lock point on 15 December 2025.
* **Medical Dictionary for Regulatory Activities (MedDRA)**: Version 28.

## 📄 License and Reproducibility

The workflow is fully reproducible. All code, package versions, data extraction rules, and transformations are documented in this repository.

## 📚 Citation

If you use this dataset or methodology in your research, please cite the original article:

```bibtex
@article{kefala2026development,
  author = {Kefala, Maria and Painter, Jeffrey L. and Bukhari, Syed Tauhid and Powell, Gregory E. and Bate, Andrew and Sessa, Maurizio},
  title = {Development of a European Union Time-indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance},
  year = {2026},
  journal = {Original Article}
}
