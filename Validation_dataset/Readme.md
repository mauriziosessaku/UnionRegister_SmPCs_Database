# Validation Subset

## 📝 Overview
This repository contains the manually validated dataset for the extraction of adverse events (AEs) from the Summaries of Product Characteristics (SmPCs) of  Centrally Authorized Products (CAPs) in the European Union. This validation subset serves as the human-verified ground truth used to evaluate the performance of the DeepSeek V3 large language model in extracting AEs from the SmPCs.

## 🔍 Validation Methodology
For the latest version of the SmPCs, two researchers (MK and STB) performed a manual validation of all extracted information included in the validation datasets.

## 📂 Dataset Structure
Each extracted piece of information about the AEs was manually categorized into one of five predefined validation statuses:
* **Correct**: Information present in the SmPC and accurately extracted.
* **Incorrect**: Information not present in the SmPC but erroneously extracted.
* **Missing**: Information present in the SmPC but not extracted.
* **Duplicate**: Information extracted twice.
* **Triplicate**: Information extracted three or more times.

## 📊 Validation Performance Metrics
* **Overall Accuracy**: Manual validation of the DeepSeek extraction model showed 95.1% accuracy.
* **Error Handling**: Missing events were identified as the most prevalent error type and were manually assigned to complete the reference standard.
* **Terminology Mapping**: MedDRA terminology mapping achieved an overall success rate of 95.7%. This included exact string matching (73.5%) and SOC-filtered batch matching (22.2%).
