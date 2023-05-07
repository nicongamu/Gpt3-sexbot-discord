## ⚠️ Warning

GPT has the ability to generate text responses on a wide range of topics. However, due to the nature of the content that it can generate, it may not be appropriate for **minors**.


## Dont wanna pay for a OpenAi key ? Thats alright use this this invite

[REDACTED] as there is a free version now


# Preview
## Paidbot
![image](https://user-images.githubusercontent.com/91066601/235471433-0bb55515-1f40-4705-a026-67999de6c7eb.png)
## Freebot + Image detect
![image](https://user-images.githubusercontent.com/91066601/236673540-e23e9ee1-643e-4b63-8b8a-3dff3b106fd4.png)
# Discord GPT-3 Sexbot

This bot uses OpenAI's GPT-3 to generate responses based on prompts from a JSON file and interacts with users on Discord.
Or you can use a free model using `freebot.py`

## Features

- Generate responses based on GPT-3 model
- Custom statuses that the bot cycles through
- Commands to change bot's profile picture, username, and more

## Installation

Before you start you must know there are 2 version of the bot 
`freebot.py`
and 
`paidbot.py`

`paidbot.py` uses openai key and `freebot.py` dosent

1. Clone the repository:
```
git clone https://github.com/mishalhossin/Gpt3-sexbot-discord
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key and Discord bot token 
For `paidbot.py` :
```
OPENAI_API_KEY=your_api_key_here
DISCORD_TOKEN=your_discord_bot_token
```
For `freebot.py` you only need discord token and hugging face access token
```
HUGGING_FACE_API=hf_access_token
DISCORD_TOKEN=your_discord_bot_token
```

4. Run the bot 
For `paidbot.py` :
```
python3 paidbot.py
```
Run the bot 
For `freebot.py`:
```
python3 freebot.py
```
   
## Usage

For all commmands use `!welp` or `!help`

To use the bot, invite it to a Discord server and use commands like `!ping`, `!changeusr`, etc.
For example, to change the bot's username, use:
```
!changeusr NewBotName
```
and to change profile picture use :
```
!pfp linktonewpfp.com/image.png
```
