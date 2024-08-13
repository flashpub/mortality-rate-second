---
title: Mortality Rates Over Multiple Decades in Japan and Switzerland
---

## Abstract

This study presents a comprehensive analysis of mortality rates in Japan and Switzerland from 1960 to 2020, examining multiple dimensions, including age, sex, cause of death, and years.

## Background

The choice of Switzerland and Japan for this analysis stems from their contrasting healthcare systems and unique locations. Switzerland has a universal private healthcare system, while Japan has a universal public one. We focus on the period 1960-2019, a turning point in medicine post-WWII, marked by advancements in healthcare. Our approach considers age and gender disparities to avoid overgeneralization. The chosen timeframe avoids skewing results due to the COVID-19 pandemic, providing a multifaceted view of mortality trends [@10.1002/9781118521373.wbeaa074;@UCLA_Medical_Advances;@Swiss_Health;@Ikegami_2011;@Numbeo_Cost_of_Living].

## Research overview

This study presents a comprehensive analysis of mortality rates in Japan and Switzerland from 1960 to 2019. The study looks at mortality patterns across age, cause of death, and gender factors. Using different descriptive, statistical and visualization tools [@10.4103/aca.ACA_157_18;@10.1002/9780470473900.ch7;@10.1016/j.bjoms.2007.09.002;@10.1002/9781405186407.wbiecc148], our research uncovers trends, nuances and factors influencing mortality rates. These findings carry significant implications for public health policies and practices, providing a multifaceted perspective on mortality dynamics in these two nations.

## Results

The current study examined trends for specific causes of death over the entire period and identified variations in mortality rates between genders in both countries. Additionally, the study investigated how death rates change with age, analyzed the primary reasons for death based on age and country, assessed the dominant causes for each age group and country.

Analysis of the data [@WHO_Mortality] from 1960 to 2020 reveals that Switzerland's mortality rates exhibit a consistent downward trend, while Japan's rates declined until 1985 but subsequently increased, surpassing Switzerland's rates by 2020 [@fig1].

:::{figure} images/fig1.png
:label: fig1
:::

After confirming the non-normal distribution of the variable death rate per 100,000 population for each cause (Shapiro-Wilk test, p-value < 0.05), the Mann-Whitney test examined gender differences [@10.2307/2333709;@10.1214/09-SS051]. For all causes, except communicable and ill defined diseases, the p-value exceeded alpha (0.05), supporting gender differences (men's mean value was higher than women's). Similar results were found for both countries.

The Mann-Whitney test for communicable diseases revealed p-values below alpha (0.05) in Switzerland and Japan, indicating no conclusive evidence of gender differences. No significant gender disparity was found for ill defined diseases for Switzerland. Notably, for Japan, differences were indicated (p-value > 0.05), with women showing a higher average mortality rate than men.

It is also worth mentioning that the populations in both countries have a different age structure, which is probably the reason for the significant increase in mortality in Japan in the period 1980-1990. This increase lasted until 2020 (i.e., the end of the entire selected period). Japan experienced a surge in births in the aftermath of World War II, occurring from 1947 to 1949. This was followed by an extended period of reduced fertility, which led to the problem of an aging population and an increase in mortality [@Li_1981]. Switzerland experienced less pronounced demographic challenges. Other differences and observations for specific causes of death are shown in the table [@table1].

:::{table}
:label: table1

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Cause</th>
      <th>Country</th>
      <th>Observation</th>
      <th>Hypothetical explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background:#F6E5D7" rowspan="2">Noncommunicable diseases (+Malignant neoplasms)</td>
      <td>Switzerland</td>
      <td>Trend of a slow decline in mortality. After 2000, the mortality rate of women in Switzerland surpassed that of men.</td>
      <td>Non-communicable diseases are the primary cause, significantly influencing mortality trends. They constitute the largest share of all deaths, setting the prevailing trend. The increase in statistics is challenging to explain due to numerous contributing factors.</td>
    </tr>
    <tr>
      <td>Japan</td>
      <td>Rapid increase in death rate from 1980s. Men have higher mortality rates.</td>
      <td>Non-communicable diseases are the primary cause, significantly influencing mortality trends. They constitute the largest share of all deaths, setting the prevailing trend. The increase in statistics is challenging to explain due to numerous contributing factors.</td>
    </tr>
    <tr>
      <td rowspan="2" style="background:#EAB389">Communicable, maternal, perinatal and nutritional conditions</td>
      <td>Switzerland</td>
      <td>Until 1990, mortality trends in Switzerland and Japan seemed similar. However, a shift occurred afterward, with Switzerland seeing a decrease in mortality while Japan observed an increase.</td>
      <td>There was an outbreak of tuberculosis from 1975 to 2000.</td>
    </tr>
    <tr>
      <td>Japan</td>
      <td>Until 1990, mortality trends in Switzerland and Japan seemed similar. However, a shift occurred afterward, with Switzerland seeing a decrease in mortality while Japan observed an increase.</td>
      <td>In Japan, something appears to have provoked the spread of deadly low respiratory diseases, as they specifically underpin the surge in statistics.</td>
    </tr>
    <tr>
      <td rowspan="2" style="background:#C9C9C9">Injuries</td>
      <td>Switzerland</td>
      <td>A significant decline in mortality rates occurred around 1995.</td>
      <td>Among other injury types, notably poisonings and falls distinguished, for which a substantial decline in mortality was observed.</td>
    </tr>
    <tr>
      <td>Japan</td>
      <td>In Japan, there was a notable increase in mortality rates after the year 1990, accompanied by isolated spikes in 2011 and 1995.</td>
      <td>In 2011, Japan experienced its strongest earthquake, followed by a tsunami where many individuals suffered fatal injuries. Furthermore, the Fukushima tragedy in 2011, caused by the earthquake, played a significant role in the increase in the number of deaths from injuries. Additionally, the charts indicate a mortality rate spike in 1995, attributed to an earthquake in that year.</td>
    </tr>
  </tbody>
</table>
:::

Plotting mortality rates by different age groups revealed an exponential distribution for both Japan and Switzerland. We performed a log-linear least-squares fit, yielding high R-squared values exceeding 0.99. We did not consider the first two age groups (0, and 1 - 4) in our fit. In these age groups, the dependence of mortality rate on age is not described by a single exponential function [@fig3]. More advanced models that take all age groups into account have been introduced by [Gompertz, Makeham](https://en.wikipedia.org/wiki/Gompertz%E2%80%93Makeham_law_of_mortality), and Siler [@Gompertz_Makeham;@10.4054/DemRes.2018.38.29].

:::{figure} images/fig3.png
:label: fig3
:::

Analyzing mortality data by cause and age, we identified the most and least frequent causes of deaths in both countries [@table2].

:::{table} Cause of Death
:label: table2

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th rowspan="2">Age Group</th>
      <th colspan="2" class="text-center">Japan</th>
      <th colspan="2" class="text-center">Switzerland</th>
    </tr>
    <tr>
      <th class="text-center">Highest</th>
      <th class="text-center">Lowest</th>
      <th class="text-center">Highest</th>
      <th class="text-center">Lowest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td style="background:#EAB389">Communicable, Maternal, Perinatal, and Nutritional conditions</td>
      <td style="background:#FAE5A3" rowspan="16">Ill-defined diseases</td>
      <td style="background:#EAB389">Communicable, Maternal, Perinatal, and Nutritional conditions</td>
      <td style="background:#C9C9C9">Injuries</td>
    </tr>
    <tr>
      <td>1–4</td>
      <td style="background:#C9C9C9" rowspan="2">Injuries</td>
      <td style="background:#F6E5D7">Noncommunicable diseases</td>
      <td style="background:#FAE5A3" rowspan="16">Ill-defined diseases</td>
    </tr>
    <tr>
      <td>5–9</td>
      <td style="background:#C9C9C9" rowspan="5">Injuries</td>
    </tr>
    <tr>
      <td>10–14</td>
      <td style="background:#F6E5D7">Noncommunicable diseases</td>
    </tr>
    <tr>
      <td>15–19</td>
      <td style="background:#C9C9C9" rowspan="3">Injuries</td>
    </tr>
    <tr>
      <td>20–24</td>
    </tr>
    <tr>
      <td>25–29</td>
    </tr>
    <tr>
      <td>30–34</td>
      <td style="background:#F6E5D7" rowspan="12">Noncommunicable diseases</td>
      <td style="background:#F6E5D7" rowspan="12">Noncommunicable diseases</td>
    </tr>
    <tr>
      <td>35–39</td>
    </tr>
    <tr>
      <td>40–44</td>
    </tr>
    <tr>
      <td>45–49</td>
    </tr>
    <tr>
      <td>50–54</td>
    </tr>
    <tr>
      <td>55–59</td>
    </tr>
    <tr>
      <td>60–64</td>
    </tr>
    <tr>
      <td>65–69</td>
    </tr>
    <tr>
      <td>70–74</td>
    </tr>
    <tr>
      <td>75–79</td>
      <td style="background:#C9C9C9">Injuries</td>
    </tr>
    <tr>
      <td>80–84</td>
      <td style="background:#FAE5A3">Ill-defined diseases</td>
      <td style="background:#C9C9C9">Injuries</td>
    </tr>
    <tr>
      <td>85+</td>
      <td style="background:#C9C9C9">Injuries</td>
      <td style="background:#FAE5A3">Ill-defined diseases</td>
    </tr>
  </tbody>
</table>
:::

After age 15, average mortality rates increase with age in both countries. The mortality rates for all age groups in both countries demonstrate a downward trend over the course of 60 years. However, the overall mortality rate for the total population for all age groups in Japan demonstrated an upward trajectory [@fig5]. The log-linear model employed to fit mortality rate variations across diverse age groups in both countries has exhibited a satisfactory level of conformity, with correlation coefficients exceeding 0.9 for the majority of age cohorts. However, the exponential model does not capture the increase of mortality with age in the age range of 20 to 39 years.

:::{figure} images/fig5.png
:label: fig5
:::

### Summary

```yaml
Year: 1960-2019 (60 years)

Sex: Female, Male, All

Age Group: 0-85+ (divided every 5 years), All

Cause: All causes, Communicable diseases, Noncommunicable diseases, Injuries, Ill-defined diseases

Country: Japan, Switzerland

Death rate: For each variables above exists a single death rate per 100,000 population

Percentage of cause-specific deaths out of total deaths: 0-100
```
