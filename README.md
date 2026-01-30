# Dynamic Reference Set for Pharmacovigilance Signal Detection

A comprehensive system for extracting and analyzing adverse events from European Medicines Agency (EMA) Summary of Product Characteristics (SmPC) documents to create a dynamic, time-indexed reference dataset for benchmarking signal detection methods in pharmacovigilance.

## 📋 Overview

This project addresses a critical gap in pharmacovigilance research by developing the first comprehensive, dynamic reference dataset based on historical SmPC documents for all centrally authorized products in the European Union. The dataset enables temporal tracking of adverse event emergence and supports the evaluation of both traditional statistical methods and AI-based approaches for safety signal detection.

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
- MedDRA terminology mapping
- ATC code integration
- Temporal tracking of AE emergence

### Analysis Capabilities
- Time-to-detection analysis
- Pre-market vs. post-market AE comparison
- System Organ Class (SOC) distribution
- Therapeutic area correlation analysis
- Individual drug safety profiles

## 💻 Technical Stack

- **Language**: Python 3.12
- **Platform**: Google Colab
- **LLM**: DeepSeek AI for text extraction
- **Key Libraries**: 
  - pandas (data handling)
  - openpyxl (Excel operations)
  - PyPDF2 (PDF processing)
  - pymysql (database connectivity)

## 📊 Data Sources

1. **European Commission Union Register** - Historical SmPC documents up to 15/12/2025
2. **MedDRA v21** - Medical terminology standardization

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
  author = {Bukhari, Syed Tauhid; Kefala, Mary; Sessa, Maurizio},
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
- Email: maurizio.sessa.ku.dk
- Project Lead: Maurizio Sessa

## ⚠️ Disclaimer

This is a research project. The database is intended for methodological research in pharmacovigilance and should not be used as the sole basis for clinical decision-making.

---

**Version**: 2.2  
**Last Updated**: January 23, 2026  
**Status**: Active Development
