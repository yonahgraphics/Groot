import discord
from rag import rag_chain
from env import DISCORD_TOKEN

def run_discord_bot(TOKEN):
    # Set up the bot with intents
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    command_prefix = '/ask '

    @client.event
    async def on_ready():
        print(f'{client.user} is now online!')

    @client.event
    async def on_message(message):
        # Ignore messages from the bot itself
        if message.author == client.user:
            return 

        # Determine if the message should be private
        is_private = False
        content = message.content.strip()
        if content.lower().endswith('p'):
            is_private = True
            # Remove the last character 'p' and any trailing spaces
            content = content[:-1].strip()

        # Check if the message starts with the bot's prefix
        if content.startswith(command_prefix):
            # Remove the prefix from the message
            question = content[len(command_prefix):].strip()
            
            # Get the response from the RAG system
            response = rag_chain(question)
            
            if is_private:
                # Send the response privately
                await message.author.send(response)
            else:
                # Send the response back to the Discord channel
                await message.channel.send(response, reference=message)

    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot(DISCORD_TOKEN)
