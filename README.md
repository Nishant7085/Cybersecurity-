# Enterprise Ransomware Risk Assessment

A beginner-friendly Python project based on the accompanying project report. It reads a sample risk register, calculates inherent risk scores, assigns risk ratings, summarises expected residual ratings, ranks the top five risks, and writes a detailed CSV report.

## Project files

- `risk_register.csv` — sample input data for 14 ransomware risks.
- `ransomware_risk_analyzer.py` — Python program that analyses the risk register.
- `risk_summary.csv` — generated output after running the program.
- `requirements.txt` — dependencies (the project uses only Python's standard library).

## Risk scoring

Inherent score = Likelihood × Impact. Both values are from 1 to 5.

| Rating | Score |
|---|---:|
| Critical | 20–25 |
| High | 12–19 |
| Medium | 6–11 |
| Low | 1–5 |

The residual score is the expected score after the recommended controls, as supplied in the sample dataset.

## Run the project

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python ransomware_risk_analyzer.py
   ```

5. Read the summary in the terminal and open `risk_summary.csv`.

## Important note

This is an educational demonstration using a fictional enterprise and estimated risk values. It is not a live security scanner and does not inspect a real network. Review and adjust the sample data before using it for any real organisation.

## Framework

The report maps risks to categories from the NIST Cybersecurity Framework (CSF) 2.0.
