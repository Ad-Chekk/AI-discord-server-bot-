# Discord NLP Bot
![WhatsApp Image 2025-04-01 at 22 55 22_5b4a4196](https://github.com/user-attachments/assets/e7a9fdab-b373-449b-bea8-15cf164a27ae)


A **Discord bot** built with **Python** and the `discord.py` library, designed to perform various **NLP tasks** like **summarization, sentiment analysis, grammar checking, tokenization, and part-of-speech tagging**.

## Features 🚀
- **Text Summarization**: Condenses long messages into a concise summary.
- **Sentiment Analysis**: Determines whether a message is positive, negative, or neutral.
- **Grammar Checking**: Identifies and suggests corrections for grammatical errors.
- **Tokenization**: Splits sentences into words and tokens.
- **Part-of-Speech (POS) Tagging**: Identifies the grammatical categories of words in a message.

## Installation 🛠
### Prerequisites
- **Python 3.8+**
- **Discord Bot Token** (from [Discord Developer Portal](https://discord.com/developers/applications))

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/discord-nlp-bot.git
   cd discord-nlp-bot
   ```
2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Create a `.env` file and add your bot token:
   ```env
   DISCORD_BOT_TOKEN=your-bot-token-here
   ```
5. **Run the bot**
   ```sh
   python bot.py
   ```

## Usage 💡
- **Summarization**: `!summarize <text>`
- **Sentiment Analysis**: `!sentiment <text>`
- **Grammar Check**: `!grammar <text>`
- **Tokenization**: `!tokenize <text>`
- **POS Tagging**: `!pos <text>`

## Example 🤖
```
User: !sentiment I love this bot!
Bot: Sentiment: Positive 😊

User: !summarize This bot is super helpful because it can analyze text and summarize it.
Bot: Summary: Helpful bot for text analysis.
```

## Technologies Used ⚙️
- **Python**
- **discord.py** (for bot functionality)
- **spaCy / NLTK** (for NLP tasks)
- **transformers** (for text summarization)

## Contributing 👥
1. Fork the repository
2. Create a new branch 
3. Make your changes 
4. Submit a pull request 

## License 📜
This project is licensed under the **MIT License**.

---
### Need Help? 🤔
Feel free to open an issue or reach out on Discord
help me to further decide and improvise the performance of summarizing feature of this bot which uses BART AI model 

