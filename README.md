# 📁 graspp-25S-fiscalpolicy

## 👥 Team Members
- Nomin-Erdene Munkhjargal  
- Fauziah Ramadhani  
- Patchara Pornpragit  
- Erlangga Gilang Pradana  

---

Main notebooks for this project are under `/notebooks` and titled:  
- **0. MAIN PROJECT**

---

## 🧠 Demographic Structure and Health-Education Spending Analysis

This project explores how changes in a country’s demographic profile—such as population aging, youth dependency, and working-age ratio—affect the allocation and efficiency of public spending in the health and education sectors.

---

## 🎯 Research Objectives

1. Examine how demographic structures shape fiscal priorities in health and education spending.
2. Project long-term public expenditure in health and education based on demographic and economic indicators.
3. Construct a cross-country **Health-Education Efficiency Index (HEE)** that benchmarks spending effectiveness.

---

## 📊 Data and Variables

The dataset covers 54 countries from 2000 to 2022, selected based on World Values Survey (WVS) availability and data completeness. Projection models extend up to 2050.

### 🔹 Key Fiscal and Demographic Variables

| Variable              | Description                                                                                  | Source                                                                                   |
|----------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Age Dependency Ratio  | Ratio of dependents (ages <15 or >64) to working-age population (15–64)                      | [World Bank - SP.POP.DPND](https://data.worldbank.org/indicator/SP.POP.DPND)             |
| Health Expenditure (% GDP) | Total current health expenditure as a % of GDP                                            | [World Bank - SH.XPD.CHEX.GD.ZS](https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS) |
| Education Expenditure (% GDP) | Government education spending as a % of GDP                                         | [World Bank - SE.XPD.TOTL.GD.ZS](https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS) |

### 🔹 Outcome Variables

| Variable       | Description                                                                                   | Source                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Life Expectancy | Expected years of life at birth                                                              | [World Bank - SP.DYN.LE00.IN](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)       |
| Infant Mortality Rate | Deaths of infants under age 1 per 1,000 live births                                   | [World Bank - SP.DYN.IMRT.IN](https://data.worldbank.org/indicator/SP.DYN.IMRT.IN)       |
| Avg. Years of Schooling | Mean years of education for adults aged 25+                                         | [Our World in Data - UNDP](https://ourworldindata.org/grapher/average-years-of-schooling)|
| Learning Outcome Scores | Harmonized international test scores (e.g., PISA, TIMSS)                             | [Our World in Data](https://ourworldindata.org/grapher/average-harmonized-learning-outcome-scores) |

### 🔹 Control Variables

| Variable         | Description                                                                                  | Source                                                                                   |
|------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| GDP per Capita    | GDP divided by midyear population (USD)                                                     | [World Bank - NY.GDP.PCAP.CD](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)       |
| Population        | Midyear total population (de facto definition)                                              | [World Bank](https://databank.worldbank.org/source/population-estimates-and-projections) |
| Income Level      | World Bank income group classification (low, lower-middle, upper-middle, high)              | [WB Income Groups](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519)     |

---

## 🧩 Research Framework

This project is organized into three main components:

### 🎯 1. Demographic Structure and Public Spending

We analyze the relationship between demographic composition and government expenditure in health and education. This includes visualizations of population pyramids of dependency ratios and scatter plots between spending and demographic indicators

To empirically test this relationship, we estimate the following panel regression:

$$
\text{Spending}_{it} = \alpha + \beta_1 \cdot \text{DependencyRatio\_Old}_{it} + \beta_2 \cdot \text{DependencyRatio\_Young}_{it} + \beta_3 \cdot \ln(\text{GDPpc}_{it}) + \varepsilon_{it}
$$

Where:
- \( i \) indexes countries  
- \( t \) indexes years

---

### 🎯 2. Health and Education Expenditure Projections (to 2050)

Using the relationships established in Part 1, we forecast future expenditure levels. The process includes:

- **Log-linear GDP projection**:

$$
\log(\text{GDP}_{t}) = \alpha + \delta \cdot t + \varepsilon_t
$$

- **Demographic forecasting** using existing UN projections on dependency ratios
- **Spending forecast** based on coefficients from regression models:

$$
\widehat{\text{Spending}}_{t} = f(\text{Projected Dependency Ratio}_t, \text{Projected GDP per capita}_t)
$$

---

### 🎯 3. Health-Education Efficiency Index (HEE)

We assess how effectively countries convert fiscal inputs into social outcomes by constructing the HEE Index, based on [ECB (2020)](https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp242.pdf):

#### Step 1: Health-Education Performance (HEP)
- Combine four outcome indicators:
  - *Health*: Life expectancy, infant mortality rate
  - *Education*: Average years of schooling, learning outcomes
- Normalize each indicator
- Assign equal weights and average to compute HEP
- Set average HEP across countries to 1

#### Step 2: Efficiency Calculation
- Normalize health and education spending
- Calculate:

$$
\text{HEE}_i = \frac{\text{HEP}_i}{\text{Normalized Spending}_i}
$$
