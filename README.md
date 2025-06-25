# Basic Data Analysis: Lotofácil Lottery

## Introduction

This project aims to analyze and extract insights from the official results of *Lotofácil*, a popular Brazilian lottery game. In Lotofácil, players select 15 numbers from a pool of 1 to 25. The minimum prize is awarded for matching at least 11 numbers, while the top prize is given for correctly matching all 15 numbers.

## Dataset Analysis

Analysis was performed on 461 historical results provided in `results.json`.

- ✅ **All results are unique** (no repeated full combinations).

### Number Distribution

- Even Numbers: **48.32%**
- Odd Numbers: **51.68%**

### Frequency Insights

- **Most Frequently Drawn Numbers**: 10, 11, 12, 20, 25
- **Least Frequently Drawn Numbers**: 6, 16, 17, 19, 23
- **Range with Most Drawn Numbers**: 11–15
- **Range with Least Drawn Numbers**: 16–20

### Result Similarity Over Time

- In **64.13%** of the 460 games, a new result had **at least 9 numbers** in common with the previous one.

### 🔗 Sequence Patterns

- **Frequency of Consecutive Sequences**:

    | Max Consecutive Sequence | Frequency |
    |--------------------------|-----------|
    | 1 seq.                   | 0.22%     |
    | 2 seq.                   | 11.93%    |
    | 3 seq.                   | 33.19%    |
    | 4 seq.                   | 29.50%    |
    | 5 seq.                   | 13.23%    |
    | 6 seq.                   | 6.72%     |
    | 7 seq.                   | 2.82%     |
    | 8 seq.                   | 1.74%     |
    | 9 seq.                   | 0.22%     |
    | 10 seq.                  | 0.22%     |
    | 11 seq.                  | 0.22%     |

- **Game with Most Numbers in Sequence**:  
  `3, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25`

- **Game with Least Numbers in Sequence**:  
  `1, 2, 4, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22, 24, 25`

- **Frequency of Gapped Sequences**:

    | Gapped Sequence Length | Frequency |
    |------------------------|-----------|
    | 4 seq.                 | 0.00%     |
    | 5 seq.                 | 0.87%     |
    | 6 seq.                 | 4.99%     |
    | 7 seq.                 | 16.49%    |
    | 8 seq.                 | 33.41%    |
    | 9 seq.                 | 26.46%    |
    | 10 seq.                | 13.67%    |
    | 11 seq.                | 3.90%     |
    | 12 seq.                | 0.22%     |

- **Game with More Gapped Sequence**:  
  `2-3-4-5-6-7-8-9-10-11-12-17-18-21-22`

- **Game with Less Gapped Sequence**:  
  `1-3-4-5-7-9-12-14-16-18-19-21-22-23-25`


### 🔄 Frequency of Repeat Matches

Each result was compared with all subsequent ones. Below is the frequency of match points observed:

| Points Matched | Occurrences |
|----------------|-------------|
| 5 pts          | 83          |
| 6 pts          | 1,634       |
| 7 pts          | 9,322       |
| 8 pts          | 24,981      |
| 9 pts          | 34,035      |
| 10 pts         | 24,833      |
| 11 pts         | 9,224       |
| 12 pts         | 1,745       |
| 13 pts         | 169         |
| 14 pts         | 4           |
| 15 pts         | 0           |

## 🎲 Simulation of Random Games

Out of **326,876 simulated games**, the following results occurred:

| Score  | Frequency |
|--------|-----------|
| 11 pts | 28,667    |
| 12 pts | 5,586     |
| 13 pts | 468       |
| 14 pts | 10        |
| 15 pts | 0         |

### 📐 Estimated Probability of Winning

| Score  | Approx. Odds (1 in N) |
|--------|-----------------------|
| 11 pts | 11                    |
| 12 pts | 60                    |
| 13 pts | 692                   |
| 14 pts | 21,792                |
| 15 pts | 3,268,760             |

---

## ⚠️ Disclaimer

Lottery results are inherently random. While statistical analysis can provide interesting patterns, it **does not predict future results**. All insights presented are based solely on the current dataset (`results.json`) and may change as more data is added or removed.

## Prerequisites

- Python 3.x

## 🚀 How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/RobisonTorres/Data_Analysis_Lottery.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Data_Analysis_Lottery
   ```

3. Run the main script:

   ```bash
   python analyzing.py
   ```

---

Feel free to fork, analyze, and contribute!