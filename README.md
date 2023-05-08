## ⚠️ Warning

GPT has the ability to generate text responses on a wide range of topics. However, due to the nature of the content that it can generate, it may not be appropriate for **minors**.


## Dont wanna pay for a OpenAi key ? Thats alright use this this invite

[REDACTED] as there is a free version now


# Preview
## Paidbot - openai
![image](https://user-images.githubusercontent.com/91066601/235471433-0bb55515-1f40-4705-a026-67999de6c7eb.png)
## Freebot + Image detect - Theb
![image](https://user-images.githubusercontent.com/91066601/236673540-e23e9ee1-643e-4b63-8b8a-3dff3b106fd4.png)
# Discord GPT-3 Sexbot

This bot uses OpenAI's GPT-3 to generate responses based on prompts from a JSON file and interacts with users on Discord.
Or you can use a free model using `freebot.py`

## Features

- Generate responses based on GPT-3 model
- Custom statuses that the bot cycles through
- Commands to change bot's profile picture, username, and more
# Getting all the stuff
## Getting Get discord token
##### Select [application](https://discord.com/developers/applications)
![image](https://user-images.githubusercontent.com/91066601/235554871-a5f98345-4197-4b55-91d7-1aef0d0680f0.png)

##### Enable intents
![image](https://user-images.githubusercontent.com/91066601/235555012-e8427bfe-cffc-4761-bbc0-d1467ca1ff4d.png)

##### Get the token !!! by clicking copy
![image](https://user-images.githubusercontent.com/91066601/235555065-6b51844d-dfbd-4b11-a14b-f65dd6de20d9.png)

## Getting Hugging face token from [here](https://huggingface.co/settings/tokens)
Dosent matter which one you use it can be read or write 
![image](https://user-images.githubusercontent.com/91066601/236817328-9ca5f240-d500-4292-8f2b-7b8e97363c6d.png)
## Getting OpenAI API key from [here](https://platform.openai.com/account/api-keys)
![image](https://user-images.githubusercontent.com/91066601/236817881-e787b446-e59a-4994-b4b6-600c4c9e3897.png)


## Installation
# 1. Clone the repository:
```
git clone https://github.com/mishalhossin/Gpt3-sexbot-discord
```

# 2. Install dependencies:
```
pip install -r requirements.txt
```
# 3. Create a `.env` file with your OpenAI API key and Discord bot token (THE BOT NEEDS TO HAVE ALL THE INTENTS)
For `paidbot.py` :

```
OPENAI_API_KEY=your_api_key_here
DISCORD_TOKEN=your_discord_bot_token
```
For `freebot.py` you needs discord token (THE BOT NEEDS TO HAVE ALL THE INTENTS) and hugging face access token

```
HUGGING_FACE_API=your_hf_access_token
DISCORD_TOKEN=your_discord_bot_token
```

# Run the bot For `paidbot.py` :
```
python paidbot.py
```
## or
# Run the bot For `freebot.py`:
```
python freebot.py
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
