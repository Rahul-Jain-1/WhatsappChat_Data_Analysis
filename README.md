# 📊 WhatsApp Chat Analyzer

This is a Streamlit application for analyzing WhatsApp chat data. Users can upload a WhatsApp chat file and get various insights such as the most active users, common words, activity timelines, and more.

## Features

- 📂 Upload WhatsApp chat file in `.txt` format.
- 🧑‍🤝‍🧑 Analyze chat data with respect to specific users or overall.
- 📅 View monthly and daily activity timelines.
- 🌐 Generate a word cloud of the most common words.
- 🗓️ View weekly activity heatmaps.
- 💬 Get statistics on the most common words and emojis used.

## Requirements

- Python 3.6+
- Streamlit
- Matplotlib
- Seaborn
- Preprocessor and Helper scripts for data processing

## Installation

1. Clone the repository :
   ```sh
   git clone https://github.com/your-username/whatsapp-chat-analyzer.git
   cd whatsapp-chat-analyzer
2. Install the required packages :
    ```sh
    pip install -r requirements.txt

## Usage

1. **Run the App**: Open a terminal and run `streamlit run app.py`.
2. **Upload Chat File**: Go to `http://localhost:8501`, and upload your WhatsApp chat file (.txt) in the sidebar.
3. **Select User and Analyze**: Choose a user or "Overall" from the dropdown and click "Show analysis" to view various statistics and visualizations.
