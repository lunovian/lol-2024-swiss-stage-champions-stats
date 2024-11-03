# LoL 2024 Swiss Stage Champions Stats 📊

This project provides an in-depth analysis of champion statistics from the **League of Legends (LoL) 2024 Swiss Stage**. The repository is designed for LoL enthusiasts, data analysts, and esports professionals interested in exploring champion performance metrics, trends, and insights from the Swiss Stage.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Highlights](#analysis-highlights)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The **League of Legends 2024 Swiss Stage Champions Stats** project dives into comprehensive statistics of champions played during the Swiss Stage of Worlds 2024. Using this dataset, we analyze performance metrics like win rates, pick and ban rates, kill-death-assist ratios, and more. This analysis helps provide insights into champion popularity, effectiveness, and meta shifts in the competitive scene.

## Dataset
The dataset for this project is sourced from **[Games of Legends](https://gol.gg)**, which provides detailed champion and player statistics from competitive League of Legends events. This data covers:
- **Champion Picks and Bans**
- **Win/Loss Records**
- **Performance Metrics**: KDA (Kill/Death/Assist) ratios, CS (Creep Score), gold earned, and more.

> **Note**: This project and dataset are not affiliated with or endorsed by Riot Games. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc.

## Project Structure
```
lol-2024-swiss-stage-champions-stats/
├── data/                # Raw and processed data files
├── notebooks/           # Jupyter notebooks for analysis
├── scripts/             # Data processing and analysis scripts
├── visualizations/      # Plotly and matplotlib visualizations
└── README.md            # Project documentation
```

## Features
- **Champion Analysis**: Detailed statistics on individual champions, including win rates, KDA, and CS.
- **Pick/Ban Rates**: Visualizations and analysis of champion pick and ban rates throughout the Swiss Stage.
- **Meta Insights**: Analysis of popular champions and shifts in the competitive meta.
- **Interactive Visualizations**: Explore data interactively using Plotly and matplotlib charts.

## Installation
To set up this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lunovian/lol-2024-swiss-stage-champions-stats.git
    cd lol-2024-swiss-stage-champions-stats
    ```

2. **Install Requirements**:
    Install the necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Data Preprocessing**:
   Run data preprocessing scripts in the `scripts/` folder to clean and prepare data.

2. **Data Analysis**:
   Open Jupyter notebooks in the `notebooks/` folder for in-depth data analysis and visualization.

3. **Visualizations**:
   Generate visualizations to explore champion stats, pick/ban rates, and more. Use interactive features in Plotly for deeper insights.

## Analysis Highlights
- **Top Picked and Banned Champions**: Discover which champions were most prioritized and why.
- **Performance Metrics**: Analyze metrics like KDA and CS to understand champion effectiveness.
- **Meta Trends**: Track shifts in champion popularity and effectiveness, offering insights into the current meta.

## Technologies Used
- **Python**: Core language for data analysis and processing
- **Pandas & NumPy**: Data manipulation
- **Matplotlib & Plotly**: Data visualization
- **Jupyter Notebook**: Interactive data analysis

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature suggestions, bug fixes, or improvements.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.
