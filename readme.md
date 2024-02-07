# Project Overview

## Description:

Explore mortality rates in Japan and Switzerland from 1960 to 2020, delving into diverse dimensions such as age, cause of death, and years. This in-depth analysis considers contrasting healthcare systems and geographical contexts between Switzerland and Japan. Focused on the transformative post-WWII era (1960-2019), our study avoids the impact of the COVID-19 pandemic, ensuring a nuanced understanding of mortality trends with a particular emphasis on age and gender disparities.

## Research Scope:

Our study unfolds along three primary axes: 

1. **Mortality Rates by Cause and Year:**
   - In-depth analysis of cause-specific trends over the entire period.
   - Detection of gender-based variations in mortality rates.

2. **Age-Specific Mortality Patterns by Cause:**
   - Examination of age-specific disparities in mortality rates in both countries.
   - Identification of age-related changes in death rates.

3. **Age-Specific Mortality Trends Across the Years:**
   - Investigation into primary causes of death by age and country.
   - Evaluation of dominant causes for each age and country.
   - Identification of trends in death rates across various age groups.

The study employs various descriptive, statistical, and visualization tools to uncover distinct trends and nuances, providing valuable insights into the factors contributing to changes in mortality rates.

## Key Findings:

- Switzerland exhibits a consistent downward trend in mortality rates, whereas Japan's rates declined until 1985 but subsequently increased, surpassing Switzerland's rates by 2020.

- Statistical tests reveal no significant difference in mortality rates between males and females.

- Mortality rates by age groups exhibit an exponential distribution for both countries, with fitted exponential curves yielding high R-squared values exceeding 0.99.

- Analysis of mortality by cause across age groups prioritizes leading causes of death within each category.

- After the age of 15, average mortality rates in both countries increase with age, demonstrating a downward trend over 60 years for all age groups.

# File Structure:

The project file structure comprises:

- **Data Folder:** Contains all data sourced from [WHO Mortality Database](https://platform.who.int/mortality).

- **utils.py:** Houses custom functions used in the analysis.

- **Analysis Sections:** Divided into three parts - age_cause analysis, age_year analysis, and years_cause analysis. Sex is added as a relevant dimension where applicable.

# Technical Details:

- **Python Version:** 3.11.5

- **Required Packages:**
  - ipykernel: 6.25.2
  - pandas: 1.5.3
  - numpy: 1.23.5
  - matplotlib: 3.7.1
  - seaborn: 0.12.2
  - scipy: 1.10.1

