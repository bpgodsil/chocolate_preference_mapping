# External Preference Mapping (EPM) with Simulated Chocolate Data

Status: Work in progress

This project explores how External Preference Mapping (EPM) techniques can be implemented in Python to relate sensory product profiles to simulated consumer liking data.
EPM combines objective Descriptive Analysis (DA) data with subjective liking scores, and is often analyzed with Partial Least Squares Regression (PLS-R) (Drake, Watson, & Liu, Annual Review of Food Science and Technology, 2024).

Here, we simulate this analysis using DA data for six chocolate types and Python/scikit-learn’s PLS-R implementation.

## Project Goals

Simulate consumer liking data based on chocolate sensory profiles (e.g., sweetness, bitterness, astringency)

Incorporate age effects on sweetness preference

Apply mean-centering to control for individual rating biases

Prepare data for modeling using PLSRegression to link sensory and consumer preference spaces

## Current Progress

- Simulated consumer liking data for multiple products and age groups
- Applied normalization (mean-centering) for within-subject variability
- Visualized the distribution of raw and centered liking scores
- Next: Fit and interpret a PLS-R model and visualize preference maps

## Next Steps

Implement and visualize the PLS-R model (PLS1 & PLS2 variants)

Compare sensory vs. preference spaces

Document the analytical workflow and insights

## Why this project

This notebook demonstrates how predictive analytics techniques like PLS-R can be used to bridge sensory science and consumer insights — a key capability in flavor and food product research.


## View Notebooks (HTML)

- [Chocolate Preference Mapping](https://bpgodsil.github.io/chocolate_preference_mapping/Chocolate_EPM_Project.html)