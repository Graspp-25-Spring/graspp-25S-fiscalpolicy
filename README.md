# graspp-25S-fiscalpolicy

## 👥 Team Members
- Nomin-Erdene Munkhjargal  
- Fauziah Ramadhani  
- Patchara Pornpragit  
- Erlangga Gilang Pradana  

---
Main notebooks for this project are under /notebooks named:
- **0. MAIN PROJECT**
---

## Demographic Structure and Health-Education Spending Analysis
This project explores how changes in a country’s demographic profile—such as population aging, youth dependency, and working-age ratio—affect the allocation and efficiency of public spending in the health and education sectors.

## 🎯 Research Objectives:

1. Analyze how demographic structure influences fiscal policy priorities, specifically health and education expenditure.
2. Project future health and education spending using key variables such as age distribution, dependency ratios, GDP per capita, and population growth.
3. Construct a Health-Education Efficiency Index, comparing outcomes (e.g., life expectancy, infant mortality, school enrollment) relative to public spending levels across countries.

---

## 📊 Data and Variables

The dataset compiles data from 54 countries selected based on the World Values Survey (WVS) and the availability of the data to reflect diverse global conditions. It spans the period from 2000 to 2022. Projection data will be projected up until 2050.

**Key Variables**
| Variable              | Definition                                                                                                                           | Source                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Age Dependency Ratio  | The ratio of dependents (people younger than 15 or older than 64) to the working-age population (ages 15–64).                            | [World Bank - SP.POP.DPND](https://data.worldbank.org/indicator/SP.POP.DPND)             |
| Health Expenditure    | Current health expenditure as a percentage of GDP. Includes all healthcare goods and services consumed in a year.                        | [World Bank - SH.XPD.CHEX.GD.ZS](https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS) |
| Education Expenditure | General government expenditure on education (current, capital, transfers), as a percentage of GDP.                                       | [World Bank - SE.XPD.TOTL.GD.ZS](https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS) |    |

**Outcome Variables**
| Variable       | Definition                                                                                     | Source                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Life Expectancy | The number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.                              | [World Bank - SP.DYN.LE00.IN](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)           |
| Mortality Rate | The number of infants dying before reaching one year of age, per 1,000 live births in a given year.                              | [World Bank - SP.DYN.IMRT.IN](https://data.worldbank.org/indicator/SP.DYN.IMRT.IN)           |
| Average Years of Schooling | Average number of years (excluding years spent repeating individual grades) adults over 25 years participated in formal education.                              | [Our World in Data - UNDP](https://ourworldindata.org/grapher/average-years-of-schooling)           |
| Average Learning Outcomes   | Average learning outcomes correspond to harmonized test scores across standardized, psychometrically-robust international and regional student achievement tests. | [Our World in Data- World Bank](https://ourworldindata.org/grapher/average-harmonized-learning-outcome-scores) |

**Control Variables**
| Variable       | Definition                                                                                     | Source                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| GDP per Capita | Gross Domestic Product divided by midyear population, in current USD.                              | [World Bank - NY.GDP.PCAP.CD](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)           |
| Population   | Total population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship. The values shown are midyear estimates. | [World Bank Population Estimates and Projection](https://databank.worldbank.org/source/population-estimates-and-projections) |
| Income Level   | World Bank classification of countries into income groups (low, lower-middle, upper-middle, high). | [World Bank Income Groups](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519) |
   
## Research Framework

🎯 1. Relationship between demographic structure and public spending
🎯 2. Health and Education data projection
🎯 3. Health-Education Efficiency Index