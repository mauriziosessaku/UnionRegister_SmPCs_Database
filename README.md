# Dynamic Reference Set for Pharmacovigilance Signal Detection

A comprehensive system for extracting and analyzing adverse events from European Medicines Agency (EMA) Summary of Product Characteristics (SmPC) documents to create a dynamic, time-indexed reference dataset for benchmarking signal detection methods in pharmacovigilance.

## 📋 Overview

This project addresses a critical gap in pharmacovigilance research by developing the first comprehensive, dynamic reference dataset based on historical SmPC documents for all centrally authorized products in the European Union. The dataset enables temporal tracking of adverse event emergence and supports the evaluation of both traditional statistical methods and AI-based approaches for safety signal detection.

### Key Statistics
- **1,514** centrally authorized medicinal products analyzed
- **123,944** total adverse events extracted
- **17,064** unique adverse events identified
- **16,594** SmPC updates processed (spanning 1995-2025)
- **92%** LLM extraction accuracy
- **33%** of AEs identified post-marketing

## 🎯 Motivation

Current pharmacovigilance faces significant challenges:
- ~95% false positive rate in EMA statistical signal detection (2024)
- Average 2.5 years from signal detection to validation
- Existing reference datasets (OMOP, SIDER) are static and limited in scope
- No comprehensive EU-specific, time-indexed reference standards exist

## 🚀 Features

### Part 1: Automated AE Extraction
- Systematic extraction from all historical SmPC versions
- LLM-based text mining (DeepSeek AI)
- Automated PDF processing and Section 4.8 parsing
- Quality validation with 92% accuracy

### Part 2: Dynamic Reference Database
- SQL-based relational database with CRUD functionality
- Web-based interface (SmPC Database Viewer)
- MedDRA terminology mapping
- ATC code integration
- Temporal tracking of AE emergence

### Analysis Capabilities
- Time-to-detection analysis
- Pre-market vs. post-market AE comparison
- System Organ Class (SOC) distribution
- Therapeutic area correlation analysis
- Individual drug safety profiles

## 🏗️ System Architecture
```
SmPC Database
├── Dashboard (Visual Analytics)
├── Human Gold Standard (Validated AE Records)
├── SmPCs (Product Characteristics)
├── SmPCs Updates (Historical Versions)
└── Export Data (Filtered Exports)
```

### Database Tables

**SmPCs Table**
- Drug name, EMA links, SmPC text, Closed date

**SmPCs Updates Table**
- Drug name, INN, Type, Decision date, MAH, ATC codes, Indication, EMA number

**Human Gold Standard Table**
- Drug-AE pairs, Assessment status, Regulatory metadata, MedDRA coding

## 💻 Technical Stack

- **Language**: Python 3.12
- **Platform**: Google Colab
- **Database**: MySQL with MyAdmin interface
- **LLM**: DeepSeek AI for text extraction
- **Key Libraries**: 
  - pandas (data handling)
  - openpyxl (Excel operations)
  - PyPDF2 (PDF processing)
  - pymysql (database connectivity)

## 📊 Data Sources

1. **European Commission Union Register** - Historical SmPC documents
2. **EudraVigilance** - EU adverse reaction database
3. **PRAC Signal List** - Validated safety signals (2012-2025)
4. **MedDRA** - Medical terminology standardization
5. **WHO-DD** - Drug dictionary

## 🔧 Installation & Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/smpc-reference-database.git

# Install required packages
pip install pandas openpyxl PyPDF2 pymysql requests --break-system-packages

# Configure database connection
# Update credentials in config file
```

## 📖 Usage

### Extracting SmPC Data
```python
# Run extraction script for latest SmPCs
python extract_latest_smpcs.py

# Run extraction for historical updates
python extract_updates.py --drug_url [PRODUCT_URL] --date [OPTIONAL_DATE]
```

### Accessing the Database

1. Navigate to SmPC Database Viewer interface
2. Select module (Dashboard, SmPCs, Updates, etc.)
3. Filter and export data as needed

### Generating Reports
```python
# Create drug safety surveillance report
python generate_report.py --drug_name "Abasaglar"

# Analyze time-to-detection by SOC
python analyze_ttd.py --soc "Cardiac disorders"
```

## 📈 Key Findings

- **Mean time to detection**: 6.02 years
- **Median time to detection**: 4.67 years
- **Clinical trial detection**: 67% of all AEs
- **Post-marketing detection**: 33% of all AEs
- Notable delays for:
  - Ophthalmic complications (~5-6 years)
  - Hypersensitivity reactions (~5-6 years)

## 🗂️ File Structure
```
project/
├── extract_latest_smpcs.py
├── extract_updates.py
├── database/
│   ├── schema.sql
│   └── config.py
├── analysis/
│   ├── generate_report.py
│   ├── analyze_ttd.py
│   └── visualization.py
├── data/
│   ├── [Drug folders with Latest/Updates subfolders]
│   └── exports/
└── docs/
    └── methodology.md
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

## 📄 License

This project is licensed under [LICENSE TYPE] - see LICENSE file for details.

## 📚 Citation

If you use this dataset or methodology in your research, please cite:
```bibtex
@misc{bukhari2026dynamic,
  author = {Bukhari, Syed Tauhid},
  title = {Making a Dynamic Reference Set for Assessing Performance of Traditional and 
           Artificial Intelligence-based Methods for Signal Detection in Pharmacovigilance},
  year = {2026},
  institution = {University of Copenhagen}
}
```

## 🙏 Acknowledgments

- **Supervisor**: Maurizio Sessa
- **Institution**: University of Copenhagen
- **Data Sources**: European Medicines Agency, European Commission
- **AI Tools**: ChatGPT, Gemini, DeepSeek (for code development)

## 📧 Contact

For questions or collaboration inquiries, please contact:
- Email: gqn375@alumni.ku.dk
- Project Lead: Syed Tauhid Bukhari

## ⚠️ Disclaimer

This is a research project. The database is intended for methodological research in pharmacovigilance and should not be used as the sole basis for clinical decision-making.

---

**Version**: 2.2  
**Last Updated**: January 23, 2026  
**Status**: Active Development
