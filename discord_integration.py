import os

from discord_webhook import AsyncDiscordWebhook


def get_webhook() -> AsyncDiscordWebhook:
    return AsyncDiscordWebhook(os.getenv("DISCORD_WEBHOOK"))
