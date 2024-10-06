# Music Control Bot 🎶

This Telegram bot allows you to control music playback on your computer. You can switch between tracks and adjust the volume directly from your Telegram chat.

## Features
- **⏯Play/Pause music**
- **⏪Previous track**
- **⏩Next track**
- **🔉 ⬇️Decrease volume**
- **🔊 ⬆️Increase volume**

## How It Works
The bot sends commands from Telegram to your computer, which controls your music player.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lipaev/remote_music_bot.git
   cd remote_music_bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Configure your bot**:  
   * Create a Telegram bot using BotFather.  
   * Copy the bot token, your user id and add it to the .env file:
   ```.env
   ADMINS_IDS=[your_id]
   BOT_TOKEN=your_telegram_bot_token_here
   ```

4. **Run the bot**:  
   ```bash
   python main.py
   ```
