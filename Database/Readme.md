# SmPC Database

This directory should contain the extracted SmPC database files.

## Download Instructions

1. Go to the [Releases page](https://github.com/mauriziosessaku/UnionRegister_SmPCs_Database/releases)
2. Download the latest `Database.zip` file
3. Extract it into this directory
```bash
# Extract the downloaded file here
unzip Database.zip -d .
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
gh release download v1.0.0 --pattern "Database.zip"

```
