# External Preference Mapping (EPM) with Simulated Chocolate Data

Status: Demonstration project

This project explores how External Preference Mapping (EPM) techniques can be implemented in Python to relate sensory product profiles to simulated consumer liking data.

EPM combines objective Descriptive Analysis (DA) data with subjective liking scores, and is often analyzed with Partial Least Squares Regression (PLS-R) (Drake, Watson, & Liu, Annual Review of Food Science and Technology, 2024).

Here, we simulate this analysis using DA data for chocolate types combined with simulated liking scores, and we use Python/scikit-learn’s PLS-R implementation.

## Business Relevance

Sensory science often seeks to link data from trained sensory panels to consumer preferences.

Here, we show how the statistical technique PLS-R can help visualize and predict relationships between these two types of data.

This approach can inform why consumers may like a product and highlight which features are most likely to optimize new products.

## Project Goals

Simulate consumer liking data based on chocolate sensory profiles (e.g., sweetness, bitterness, astringency)

Incorporate age effects on sweetness preference

Apply mean-centering to control for individual rating biases

Prepare data for modeling using PLSRegression to link sensory and consumer preference spaces

Compare PLS-R's performance when the relationship between the sensory profile and liking is either linear vs non-linear

## Key Findings

• The PLS‑R model explained ~82% of variance in simulated liking scores.
• Sweetness had the strongest positive loading; bitterness and astringency loaded negatively.

## Current Progress

- Simulated consumer liking data for multiple products using linear and nonlinear approaches
- Applied normalization (mean-centering) for within-subject variability
- Visualized the distribution of raw and centered liking scores
- Fitted and interpreted a PLS-R model with the linear liking data and visualized results with a biplot

## Next Steps

- Fit and interpret a PLS-R model with the non-linear liking data and visualized results with a biplot
- Compare results to those of the linear liking approach

## Why this project

This notebook demonstrates how predictive analytics techniques like PLS-R can be used to bridge sensory science and consumer insights, which is a key capability in flavor and food product research.


## View Notebooks (HTML)

- [Chocolate Preference Mapping](https://bpgodsil.github.io/chocolate_preference_mapping/Chocolate_EPM_Project.html)
