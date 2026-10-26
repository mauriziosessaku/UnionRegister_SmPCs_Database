# Validation Subset

## 📝 Overview
This directory contains manually reviewed validation material for adverse events (AEs) extracted from the Summaries of Product Characteristics (SmPCs) of centrally authorised products (CAPs) in the European Union. This validation subset serves as the human-verified ground truth used to evaluate the performance of the DeepSeek V3 large language model in extracting AEs from the SmPCs.

## 🔍 Validation Methodology
Two researchers (MK and STB) manually reviewed information extracted from the most recent SmPC version for the included products, verifying AE expressions, INNs and brand names against the SmPC and regulatory metadata against the source product webpages. The validation was not described as an independent manual review of every historical SmPC version or of every one of the 36 fields across all 110,823 historical drug–AE records.

## 📂 Dataset Structure
Each extracted piece of information about the AEs was manually categorized into one of five predefined validation statuses:
* **Correct**: Information present in the SmPC and accurately extracted.
* **Incorrect**: Information not present in the SmPC but erroneously extracted.
* **Missing**: Information present in the SmPC but not extracted.
* **Duplicate**: Information extracted twice.
* **Triplicate**: Information extracted three or more times.

The revised manuscript reports 95.1% AE extraction accuracy. Consult the underlying validation files and analysis script for actual counts and denominators; do not infer counts by applying 95.1% to all historical drug–AE records.

## 📊 Validation Performance Metrics
* **Overall Accuracy**: Manual validation of the DeepSeek extraction model showed 95.1% accuracy.
* **Error Handling**: Missing events were identified as the most prevalent error type and were manually assigned to complete the reference standard.
* **Terminology Mapping**: MedDRA terminology mapping achieved an overall success rate of 95.7%. This included exact string matching (73.5%) and SOC-filtered batch matching (22.2%).
