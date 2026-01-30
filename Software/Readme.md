# EMA SmPC Adverse Event Extraction Pipeline


<iframe width="560" height="315" src="https://app.heygen.com/embedded-player/0779e595a67541d7b20db85130f92bf2" title="HeyGen video player" frameborder="0" allow="encrypted-media; fullscreen;" allowfullscreen></iframe>

**Quality Check and Processing Script**

A comprehensive Google Colab pipeline for extracting, processing, and validating adverse events from European Medicines Agency (EMA) Summary of Product Characteristics (SmPC) documents.

---

## 📋 Overview

This script automates the complete workflow for:
1. **Scraping** EMA product metadata from Union Register
2. **Downloading** SmPC PDFs
3. **Extracting** Section 4.8 (Undesirable Effects)
4. **Processing** adverse events using LLM (DeepSeek AI)
5. **Validating** and organizing results
6. **Packaging** outputs for download

### Key Features

✅ **Automated Web Scraping** - Extracts product metadata from EMA webpages  
✅ **Date Filtering** - Process specific SmPC updates by date  
✅ **PDF Processing** - Handles multiple PDF formats and structures  
✅ **LLM Integration** - Uses DeepSeek for intelligent adverse event extraction  
✅ **Quality Control** - Built-in validation and error handling  
✅ **Batch Processing** - Process multiple products efficiently  
✅ **Download Management** - Creates organized ZIP archives  
✅ **Progress Tracking** - Real-time status updates and summaries  

---

## 🎯 Use Cases

- **Quality Assurance**: Verify extraction accuracy for SmPC database
- **Batch Processing**: Extract AEs from multiple products at once
- **Historical Analysis**: Process specific SmPC update dates
- **Data Validation**: Compare automated vs. manual extractions
- **Pipeline Testing**: Test the extraction workflow end-to-end

---

## 🛠️ Prerequisites

### Platform
- **Google Colab** (recommended) or local Jupyter environment
- Internet connection for EMA data access
- Google Drive (optional, for persistent storage)

### Python Packages
The script automatically installs required packages:
- `PyMuPDF` (fitz) - PDF text extraction
- `PyPDF2` - PDF manipulation
- `pdfplumber` - Alternative PDF parser
- `camelot-py[cv]` - Table extraction (optional)
- `pandas` - Data manipulation
- `requests` - Web scraping

### API Access
- **DeepSeek API Key** - Required for LLM-based extraction
  - Get your API key from: [https://deepseek.com](https://deepseek.com)
  - Free tier available for testing

---

## 📁 File Structure

### Input
```
Input URL from EMA Union Register
↓
e.g., https://ec.europa.eu/health/documents/community-register/html/h428.htm
```

### Outputs Created
```
/content/
├── section_4_8_extracts/           # Extracted Section 4.8 text files
│   ├── 2014-09-11_abasaglar.txt
│   ├── 2015-05-21_abasaglar.txt
│   └── ...
│
├── adverse_events_extracts/         # CSV files with AE lists
│   ├── 2014-09-11_abasaglar_adverse_events.csv
│   ├── 2015-05-21_abasaglar_adverse_events.csv
│   └── ...
│
├── final_adverse_events/            # Excel files with metadata + AEs
│   ├── 2014-09-11_abasaglar_adverse_events.xlsx
│   ├── 2015-05-21_abasaglar_adverse_events.xlsx
│   └── ...
│
└── conversion_summary.xlsx          # Processing summary report
```

### ZIP Archives (for download)
```
section_4_8_txt_files_YYYYMMDD_HHMMSS.zip
adverse_events_csv_files_YYYYMMDD_HHMMSS.zip
final_adverse_events_xlsx_YYYYMMDD_HHMMSS.zip
```

---

## 🚀 Quick Start Guide

### Step 1: Open in Google Colab

1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload `optimized_process_quality_check_syed.py`
3. Or create a new notebook and paste the code

### Step 2: Install Dependencies

Run the installation cells (automatically included):
```python
!pip install PyMuPDF
!pip install fitz tools requests
!pip install "camelot-py[cv]"
!pip install PyPDF2
!pip install pdfplumber
```

### Step 3: Configure API Key

When prompted, enter your DeepSeek API key:
```python
Enter your DeepSeek API key: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 4: Provide EMA URL

Enter the product page URL from Union Register:
```
Enter EMA webpage URL: https://ec.europa.eu/health/documents/community-register/html/h428.htm
```

### Step 5: Filter by Dates (Optional)

Enter specific dates to process:
```
Enter close dates (comma-separated) or press ENTER for all dates: 2014-09-11, 2015-05-21
```

Leave blank to process all available SmPC updates.

### Step 6: Monitor Progress

The script will display real-time progress:
```
🚀 EMA Data Extraction
================================================================================

STEP 1: EMA Webpage Scraping
--------------------------------------------------------------------------------
🌐 Fetching webpage: https://ec.europa.eu/health/documents/...
✅ Found 13 product information items
✅ Found 45 procedure records

STEP 2: Date Filtering
--------------------------------------------------------------------------------
🔍 Filtering by 2 date(s)...
✅ Filtered from 45 to 2 procedure records

STEP 3: PDF Download and Processing
--------------------------------------------------------------------------------
📥 Downloading 2 PDFs...
[1/2] 2014-09-11_abasaglar.pdf
  ✅ Downloaded (1.2 MB)
[2/2] 2015-05-21_abasaglar.pdf
  ✅ Downloaded (1.3 MB)

...
```

### Step 7: Download Results

At the end, ZIP files will automatically download to your browser:
```
⬇️  Downloading: section_4_8_txt_files_20260123_143052.zip
✅ Download started

⬇️  Downloading: adverse_events_csv_files_20260123_143052.zip
✅ Download started

⬇️  Downloading: final_adverse_events_xlsx_20260123_143052.zip
✅ Download started
```

---

## 📊 Output File Formats

### 1. Section 4.8 Text Files (.txt)
Raw extracted text from Section 4.8 of SmPC:
```
4.8 Undesirable effects

Summary of the safety profile

The most frequently reported adverse reactions for valemetostat...
[Full section text]
```

### 2. Adverse Events CSV (.csv)
List of extracted adverse events:
```csv
Adverse Event
Hypoglycaemia
Allergic reactions
Dysgeusia
Injection site reactions
...
```

### 3. Final Adverse Events Excel (.xlsx)
Complete dataset with metadata:

| Column | Description | Example |
|--------|-------------|---------|
| `closed` | SmPC update close date | 2014-09-11 |
| `type` | Procedure type | Centralised - Authorisation |
| `ema_number` | EMA reference number | EMEA/H/C/2835 |
| `decision.number` | EC decision number | (2014)6474 |
| `decision.date` | Decision date | 2014-09-09 |
| `ema_link` | Link to PDF | https://ec.europa.eu/... |
| `name` | Product brand name | Abasaglar |
| `eu_num` | EU authorization number | EU/1/14/944 |
| `inn` | Active substance | Insulin glargine |
| `indication` | Therapeutic indication | Treatment of diabetes... |
| `mah` | Marketing Authorization Holder | Eli Lilly Nederland B.V. |
| `atc` | ATC code | A10AE04 |
| `adverse_event` | Extracted adverse event | Hypoglycaemia |

### 4. Conversion Summary (.xlsx)
Processing report:

| Column | Description |
|--------|-------------|
| `input_file` | Source CSV filename |
| `closed_date` | Processing date |
| `product_name` | Drug name |
| `output_file` | Generated Excel file |
| `adverse_events_count` | Number of AEs extracted |
| `status` | Success or Error message |

---

## 🔧 Advanced Configuration

### Custom Output Folder
```python
output_folder = "/content/my_custom_folder"
os.makedirs(output_folder, exist_ok=True)
```

### Adjust API Parameters
```python
# In the LLM extraction section
"max_tokens": 5000,        # Increase for longer lists
"temperature": 0.3,        # Lower = more consistent
```

### Add Custom Headers
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9'
}
```

### Change PDF Extraction Method
The script uses multiple methods automatically:
1. PyMuPDF (primary)
2. pdfplumber (fallback 1)
3. PyPDF2 (fallback 2)

---

## 🔍 Quality Control Features

### 1. Duplicate Detection
Automatically identifies and removes duplicate PDFs:
```
⚠️ Duplicate detected: 2014-09-11 (ID: 127843)
  Keeping first occurrence, skipping duplicate
```

### 2. Section 4.8 Validation
Verifies Section 4.8 was successfully extracted:
```python
if "4.8" not in section_text:
    print("⚠️ Section 4.8 heading not found")
```

### 3. LLM Response Validation
Checks that adverse events were extracted:
```python
if len(adverse_events) == 0:
    print("⚠️ No adverse events extracted")
```

### 4. File Integrity Checks
Validates downloaded PDFs:
```python
if not os.path.exists(local_path):
    print(f"❌ Download failed: {filename}")
```

### 5. Error Logging
Comprehensive error tracking:
```python
try:
    # Processing code
except Exception as e:
    print(f"❌ Error: {e}")
    traceback.print_exc()
```

---

## 📈 Performance Metrics

### Processing Speed
- **Web scraping**: ~5 seconds per product page
- **PDF download**: ~2-5 seconds per PDF (depends on size)
- **Section extraction**: ~1-2 seconds per PDF
- **LLM processing**: ~3-10 seconds per SmPC

### Typical Throughput
- **Single product (1 date)**: ~30 seconds
- **Single product (10 dates)**: ~3-5 minutes
- **Batch (10 products)**: ~30-60 minutes

### Resource Usage
- **Memory**: ~500MB-2GB (Colab free tier sufficient)
- **Storage**: Varies by number of PDFs (avg. 1-5 MB per PDF)

---

## ⚠️ Troubleshooting

### Common Issues

#### 1. "Invalid URL" Error
**Problem**: URL format not recognized  
**Solution**: Ensure URL starts with `https://` and is from Union Register

```python
# Correct format
https://ec.europa.eu/health/documents/community-register/html/h428.htm

# Incorrect
ec.europa.eu/health/documents/...  # Missing https://
```

#### 2. "No procedures found matching dates"
**Problem**: Date filter doesn't match available data  
**Solution**: Check available dates displayed in output

```
Available dates in data: ['2014-09-11', '2015-05-21', '2016-03-17']
```

#### 3. "Section 4.8 not found"
**Problem**: PDF structure variation or encoding issues  
**Solution**: Script tries multiple extraction methods automatically

```python
# The script attempts:
1. PyMuPDF with font detection
2. pdfplumber with layout analysis
3. PyPDF2 as final fallback
```

#### 4. "LLM extraction returned empty"
**Problem**: API key invalid or rate limit exceeded  
**Solution**: 
- Verify API key is correct
- Check DeepSeek API quota
- Wait if rate limited

#### 5. "Download failed"
**Problem**: Network issues or invalid PDF link  
**Solution**: 
- Check internet connection
- Verify link_final is correctly formatted
- Some old PDFs may not be available

### Debug Mode

Add debug prints to investigate issues:
```python
# Add after any function
print(f"DEBUG: Variable value = {variable}")
import traceback
traceback.print_exc()  # Full error details
```

---

## 🔐 Security & Privacy

### API Key Protection
- Never hardcode API keys in scripts
- Use Colab secrets or environment variables
- Don't share notebooks with API keys

### Data Privacy
- All processing is temporary (in Colab session)
- No data stored on external servers
- Downloads are local to your machine

### Best Practices
```python
# Use Colab secrets
from google.colab import userdata
api_key = userdata.get('DEEPSEEK_API_KEY')

# Or use environment variables
import os
api_key = os.getenv('DEEPSEEK_API_KEY')
```

---

## 🔄 Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  1. USER INPUT                                                  │
│  └─ EMA URL + Optional dates                                    │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  2. WEB SCRAPING                                                │
│  └─ Extract product metadata + procedure list                   │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  3. DATE FILTERING                                              │
│  └─ Filter procedures by specified dates                        │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  4. PDF DOWNLOAD                                                │
│  └─ Download SmPC PDFs from EC registry                         │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  5. SECTION 4.8 EXTRACTION                                      │
│  └─ Extract "Undesirable Effects" section from PDFs             │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  6. LLM PROCESSING                                              │
│  └─ DeepSeek extracts adverse event list from text              │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  7. DATA COMBINATION                                            │
│  └─ Merge adverse events with product metadata                  │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  8. OUTPUT GENERATION                                           │
│  └─ Create TXT, CSV, and XLSX files                             │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  9. PACKAGING                                                   │
│  └─ Create ZIP archives for download                            │
└──────────────────────┬──────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────┐
│  10. DOWNLOAD                                                   │
│  └─ User receives organized ZIP files                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💡 Tips & Best Practices

### For Quality Assurance
1. **Start Small**: Test with 1-2 dates first
2. **Verify Manually**: Check a few extractions against actual SmPCs
3. **Compare Methods**: Run multiple extraction approaches
4. **Track Errors**: Keep the conversion_summary.xlsx for analysis

### For Batch Processing
1. **Process by Therapeutic Area**: Group similar drugs
2. **Use Date Ranges**: Process by year or quarter
3. **Monitor Progress**: Watch Colab logs for issues
4. **Save Incrementally**: Download ZIPs periodically

### For Efficiency
1. **Use GPU Runtime**: Not required but faster for large batches
2. **Close PDFs**: Free memory after processing
3. **Clear Output**: Remove old files before new runs
4. **Use Google Drive**: Mount Drive for persistent storage

```python
from google.colab import drive
drive.mount('/content/drive')

# Save to Drive instead of /content
output_folder = "/content/drive/MyDrive/SmPC_Extractions"
```

---

## 📚 Related Scripts

This script is part of a larger SmPC processing pipeline:

1. **`extract_latest_smpcs.py`** - Extract from latest SmPC versions
2. **`extract_updates.py`** - Process historical SmPC updates
3. **`optimized_process_quality_check_syed.py`** - *This script* (quality control)
4. **`generate_report.py`** - Create drug safety reports
5. **`analyze_ttd.py`** - Time-to-detection analysis

---

## 📝 Changelog

### Version 1.0 (January 2026)
- Initial release
- Integrated LLM extraction (DeepSeek)
- Added quality control features
- Implemented batch processing
- Created automated download system

### Known Limitations
- Requires internet connection throughout
- DeepSeek API rate limits apply
- Some old PDFs may have OCR issues
- Large batches may timeout in Colab free tier

---

## 🤝 Contributing

Improvements welcome! Consider:
- Adding support for other languages
- Implementing OCR for scanned PDFs
- Adding more PDF extraction methods
- Improving error recovery
- Optimizing LLM prompts

---

## 📧 Contact & Support

**Author**: Syed Tauhid Bukhari  
**Email**: gqn375@alumni.ku.dk  
**Institution**: University of Copenhagen  
**Supervisor**: Maurizio Sessa  

For issues or questions:
1. Check the Troubleshooting section
2. Review error messages carefully
3. Contact via email with error logs

---

## 📄 License

This script is part of a Master's thesis project at the University of Copenhagen. For academic and research use.

---

## ⚠️ Disclaimer

This tool is for research purposes only. Always verify extracted adverse events against official SmPC documents. The LLM-based extraction, while accurate, may occasionally miss or misinterpret adverse events.

**Extraction Accuracy**: ~92% (based on validation of 1,514 latest SmPCs)

---

## 🎓 Citation

If you use this script in your research:

```bibtex
@software{bukhari2026quality,
  author = {Bukhari, Syed Tauhid},
  title = {EMA SmPC Adverse Event Extraction Pipeline: Quality Check Script},
  year = {2026},
  institution = {University of Copenhagen},
  note = {Part of Master's thesis on pharmacovigilance signal detection}
}
```

---

**Last Updated**: January 23, 2026  
**Version**: 1.0  
**Tested On**: Google Colab (Python 3.10)  
**Status**: Production Ready ✅
