# graspp-25S-fiscalpolicy

## 👥 Team Members
- Nomin-Erdene Munkhjargal  
- Fauziah Ramadhani  
- Patchara Pornpragit  
- Erlangga Gilang Pradana  

---
Main notebooks for this project are under /notebooks named:
- **0. Milestone 1.ipynb**
- **0. Milestone 2.ipynb**
- **0. Milestone 3.ipynb**
---

## 🎯 "How Does Demographic Structure Influence Fiscal Policy Spending?"

This question explores how governments adjust and allocate public spending—e.g., toward health, education, or development—depending on the age composition of their population.

---

## 💡 Hypothesis

A higher dependency ratio leads to a shift in fiscal policy toward social sectors (health, pensions, education), and away from capital expenditure (e.g., research and development).

## 📊 Data and Variables

- The dataset compiles data from 64 countries selected based on the World Values Survey (WVS) to reflect diverse global conditions. It spans the period from 2000 to 2020. The main focus is to examine the influence of demographic structure — using the age dependency ratio—on government spending in health, education, research & development (R&D), and social contributions.

Key Variables
| Variable              | Definition                                                                                                                           | Source                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Age Dependency Ratio  | The ratio of dependents (people younger than 15 or older than 64) to the working-age population (ages 15–64).                            | [World Bank - SP.POP.DPND](https://data.worldbank.org/indicator/SP.POP.DPND)             |
| Health Expenditure    | Current health expenditure as a percentage of GDP. Includes all healthcare goods and services consumed in a year.                        | [World Bank - SH.XPD.CHEX.GD.ZS](https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS) |
| Education Expenditure | General government expenditure on education (current, capital, transfers), as a percentage of GDP.                                       | [World Bank - SE.XPD.TOTL.GD.ZS](https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS) |
| R&D Expenditure | Gross domestic expenditures on research and development (R&D), expressed as a percent of GDP.                                       | [World Bank - GB.XPD.RSDV.GD.ZS](https://data.worldbank.org/indicator/GB.XPD.RSDV.GD.ZS) |
| Social Contribution   | Social security contributions by employees, employers, self-employed, and others, expressed as a percentage of total government revenue. | [World Bank - GC.REV.SOCL.ZS](https://data.worldbank.org/indicator/GC.REV.SOCL.ZS)       |

Control Variables
| Variable       | Definition                                                                                     | Source                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| GDP per Capita | Gross Domestic Product divided by midyear population, in current USD.                              | [World Bank - NY.GDP.PCAP.CD](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)           |
| Income Level   | World Bank classification of countries into income groups (low, lower-middle, upper-middle, high). | [World Bank Income Groups](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519) |
   
