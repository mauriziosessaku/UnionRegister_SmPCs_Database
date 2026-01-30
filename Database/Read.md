# SmPC Database

This directory should contain the extracted SmPC database files.

## Download Instructions

1. Go to the [Releases page](https://github.com/yourusername/repo-name/releases)
2. Download the latest `smpc-database.zip` file
3. Extract it into this directory
```bash
# Extract the downloaded file here
unzip smpc-database.zip -d .
```

## Expected Structure

After extraction, you should have:
```
data/
├── Abasaglar/
│   ├── Latest/
│   └── Updates/
├── Abecma/
│   ├── Latest/
│   └── Updates/
...
└── [1,514 total drug folders]
```

## Alternative: Direct Download via Command Line
```bash
# Using GitHub CLI
gh release download v1.0.0 --pattern "smpc-database.zip"

# Using wget
wget https://github.com/yourusername/repo-name/releases/download/v1.0.0/smpc-database.zip

# Using curl
curl -L -O https://github.com/yourusername/repo-name/releases/download/v1.0.0/smpc-database.zip
```
