# [cite_start]Development of a European Union Time-indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance [cite: 3]

[cite_start]A comprehensive system for extracting and analyzing adverse events from European Union Summary of Product Characteristics (SmPC) documents to create a dynamic, time-indexed reference dataset for benchmarking signal detection methods in pharmacovigilance[cite: 25, 36].

## 📋 Overview

[cite_start]This project addresses a critical gap in pharmacovigilance research by developing a time-indexed reference dataset for the European Union (EU)[cite: 25]. [cite_start]The database includes 17,761 SmPC versions spanning from 1995 to 2025, comprising 123,868 drug–adverse event (AE) associations[cite: 29]. [cite_start]The processed database for active centrally authorized products (CAPs) includes 1,479 medicinal products and 110,548 drug-event associations[cite: 30].

## 🎯 Motivation

[cite_start]The identification of optimal signal detection methods is hindered by the lack of reliable reference datasets[cite: 23]. [cite_start]Existing datasets do not capture when adverse events (AEs) are officially recognized by regulatory authorities[cite: 24]. [cite_start]This limitation prevents the restriction of analyses to pre-confirmation periods and limits the evaluation of early detection performance[cite: 24]. 

## 🚀 Methodology and Features

[cite_start]The data processing workflow consists of sequential and fully automated stages[cite: 74]:

* [cite_start]**Generation of the Union Register Link List**: Standardized URLs are constructed for each product to point to dedicated Union Register pages[cite: 79].
* [cite_start]**Web Scraping and Metadata Extraction**: Product information and regulatory procedure records are programmatically retrieved from EMA public HTML webpages[cite: 82].
* [cite_start]**PDF Download and Section 4.8 Extraction**: SmPC PDFs are downloaded and the "Undesirable effects" section is extracted using `pdfplumber`[cite: 86, 87].
* [cite_start]**AE Extraction and Structured Data Output**: Extracted texts are processed using the DeepSeek R1 API to identify individual AEs[cite: 89].
* [cite_start]**MedDRA v28 Enrichment**: Unique AE terms are encoded against MedDRA version 28 using exact string matching and a System Organ Class (SOC)-based filtering strategy with DeepSeek[cite: 93, 97].

## 📈 Analysis Capabilities

The repository includes code to replicate the statistical analyses and figures presented in the manuscript, including:

* [cite_start]Longitudinal growth of the database and temporal trends in safety label updates[cite: 104].
* [cite_start]Stratification of drug-AEs by discovery phase, specifically pre-marketing versus post-marketing[cite: 105].
* [cite_start]Quantification of MedDRA SOC coverage and ubiquity across the product population[cite: 106].
* [cite_start]Density metrics of safety information per medicinal product[cite: 107].
* [cite_start]Comparative analyses across therapeutic areas using WHO ATC level 1 hierarchy[cite: 109].
* [cite_start]Mechanism-based safety profile comparisons between small molecules and biological/targeted therapies[cite: 110].
* [cite_start]Kaplan-Meier survival analysis for time-to-first SmPC update[cite: 111].

## 💻 Technical Stack

* [cite_start]**Languages**: Python (version 3.2) and R (version RStudio 2026.01.0)[cite: 71, 112].
* [cite_start]**Environment**: Google Colab[cite: 71].
* [cite_start]**AI Models**: DeepSeek R1 for unstructured narrative text parsing and SOC predictions[cite: 52, 97].
* [cite_start]**Key Python Libraries**: `requests` for web requests[cite: 72].
* [cite_start]**Key Python Libraries**: `pandas` for structured data manipulation[cite: 72].
* [cite_start]**Key Python Libraries**: `re` and `json` for parsing embedded web content[cite: 72].
* [cite_start]**Key Python Libraries**: `pdfplumber`, `PyMuPDF`, `PyPDF2`, and `camelot-py[cv]` for robust text extraction from PDFs[cite: 72, 73].

## 📊 Data Sources

* [cite_start]**European Commission’s Union Register of Medicinal Products**: Sourced with a data lock point on 15 December 2025[cite: 48].
* [cite_start]**Medical Dictionary for Regulatory Activities (MedDRA)**: Version 28[cite: 53].

## 📄 License and Reproducibility

[cite_start]The workflow is fully reproducible. [cite_start]All code, package versions, data extraction rules, and transformations are documented in this repository.

## 📚 Citation

If you use this dataset or methodology in your research, please cite the original article:

```bibtex
@article{kefala2026development,
  author = {Kefala, Maria and Painter, Jeffrey L. and Bukhari, Syed Tauhid and Powell, Gregory E. and Bate, Andrew and Sessa, Maurizio},
  title = {Development of a European Union Time-indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance},
  year = {2026},
  journal = {Original Article}
}
