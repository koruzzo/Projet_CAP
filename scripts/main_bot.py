from django.conf import settings
from discord import Intents, Message, Client
from .responses_bot import get_response


bot_key = getattr(settings, 'DISCORD_TOKEN', '')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    """
    Fonction pour envoyer un message à l'utilisateur.
    
    Args:
        message (Message): L'objet représentant le message reçu.
        user_message (str): Le message de l'utilisateur.
    """
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = await get_response(user_message)  # Await here
        # pylint: disable=W0106
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    """
    Fonction exécutée lorsque le bot est prêt.
    """
    print(f'{client.user} ON!')


@client.event
async def on_message(message: Message) -> None:
    """
    Fonction exécutée lorsqu'un message est reçu.
    
    Args:
        message (Message): L'objet représentant le message reçu.
    """
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


def run() -> None:
    """
    Fonction pour exécuter le bot.
    """
    client.run(token=bot_key)


if __name__ == '__main__':
    run()
