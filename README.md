# Music Control Bot 🎶

This Telegram bot allows you to control music and video playback on your computer. You can switch between tracks, rewind video and adjust the volume directly from your Telegram chat.

[![2025-04-15-224405806.png](https://i.postimg.cc/8Cv9KVkJ/2025-04-15-224405806.png)](https://postimg.cc/KKZ0jwMx)

## Features
- **⏯️Play/Pause music**
- **⏪Previous track**
- **⏩Next track**
- **🔉 ⬇️Volume down**
- **🔊 ⬆️Volume up**
- **⬅️ Rewind on 5 seconds**
- **➡️ Forward on 5 seconds**
- **⟪J Rewind on 10 seconds**
- **K Play/Pause video**
- **L⟫ Forward on 10 seconds**
- **[F] Full screen**


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
   Or use MusicBot.bat.
