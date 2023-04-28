from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI - ChatBot</title>
        <style>
            body {{
                background-image: url('https://cdn.discordapp.com/attachments/1089020924688355330/1100046460252328036/gradient-background-backdrop-multicolor-colorful-vibrant-3840x2160-6723_copy.png');
                background-size: cover;
            }}
            .commands-container {{
                border-radius: 25px;
                background-color: rgba(241, 241, 241, 0.8);
                padding: 20px;
                width: 60%;
                margin: 0 auto;
            }}
            .command {{
                animation: typing 6s steps(60, end), blink-caret .75s step-end infinite;
                font-family: monospace;
                font-size: 16px;
                color: #000000;
                text-shadow: 0 0 3px #fabb34;
                white-space: nowrap;
                overflow: hidden;
            }}
            @keyframes typing {{
                from {{ width: 0 }}
                to {{ width: 100% }}
            }}
            @keyframes blink-caret {{
                50% {{ border-color: transparent }}
            }}
            h1 {{
                text-align: center;
                color: white;
            }}
            h2 {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>Created by Mishal</h1>
        <div class="commands-container">
            <h2>Commands</h2>
            <p class="command">!pfp [image_url] - Change the bot's profile picture</p>
            <p class="command">!changeusr [new_username] - Change the bot's username</p>
            <p class="command">!invite_all - Generate invites for all servers the bot is in</p>
            <p class="command">!addroles - Add all roles to the specified user</p>
            <p class="command">!checkperm - Check the bot's permissions in this server</p>
            <p class="command">!troll - Change all nicknames to 'Slaves lol' for trolzez</p>
            <p class="command">!ping - Pong</p>
            <p class="command">!addchannel - Add the current channel to the list of active channels</p>
            <p class="command">!randomstory - Uses AI to generate a random story</p>
            <p class="command">!define [Word] - Uses AI to explain a word</p>
            <p class="command">!ask [Question] - Uses AI to answer a question</p>
            <p class="command">!storyonusr [@USER] - Uses AI to create a random story on a mentioned @user</p>
        </div>
    </body>
    </html>
    '''

    return render_template_string(html)

def run():
    app.run(host='0.0.0.0', port=3000)

def keep_alive():
    server = Thread(target=run)
    server.start()
