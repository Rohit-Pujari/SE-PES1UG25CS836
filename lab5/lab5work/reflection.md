# Lab 5 — Reflection

> The uploaded three-page handout mentions reflection questions but does not show their exact wording. These are draft answers to common reflection prompts; replace or reorder them to match the exact questions provided by the instructor.

## 1. What is static code analysis, and why is it useful?
Static code analysis checks source code without executing the program. It helps identify security risks, likely bugs, unused code, and style violations early. It makes code easier to maintain and reduces the chance of defects reaching users, although it cannot detect every runtime or logic problem.

## 2. What did Pylint, Bandit, and Flake8 each help identify?
Pylint checks code quality, naming, unused imports, and potential programming mistakes. Bandit focuses on common security problems, such as unsafe deserialization and insecure configuration. Flake8 checks Python style and formatting, including whitespace, line length, and related violations. Using all three gives broader coverage than relying on one tool.

## 3. What issues were fixed, and how did the fixes improve the program?
The code was updated to use a safe YAML loader, avoid a hardcoded password, disable Flask debug mode, and escape user-controlled HTML output. Logic fixes addressed room capacity, gender compatibility, duplicate allocations, room vacancy records, vacant-bed counting, and seniority ordering. The changes improve security, data consistency, and expected behavior.

## 4. What are the limitations of static analysis?
Static analysis can report false positives and may not understand the intended behavior of a program. It can miss business-logic errors, incorrect results, and problems that depend on runtime data or configuration. For that reason, the findings should be reviewed and followed by running the program and testing important cases.

## Verification status
The corrected source was prepared for the lab, but Pylint, Bandit, and Flake8 could not be installed in the preparation environment because network access was unavailable. Therefore, no final scores or clean-tool results are claimed. Run the commands in `run_analysis.sh` in your lab environment and save the resulting reports before submission.
