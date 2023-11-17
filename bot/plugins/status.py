import asyncio
import io
import math
import os
import shutil
import sys
import time
import traceback

# import psutil

from ..config import Config
from ..helpers.display_progress import humanbytes
from ..utubebot import UtubeBot
from ..translations import Messages as tr
from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

log = logging.getLogger(__name__)


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("status")
    & Filters.user(Config.BOT_OWNER)
)
async def stats_message_fn(client, message):
    restart_time = Config.BOT_START_DATETIME
    hr, mi, se = map(time_format, up_time(time.time() - Config.BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    # ram = psutil.virtual_memory().percent
    # cpu = psutil.cpu_percent()
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    # sent = humanbytes(psutil.net_io_counters().bytes_sent)
    # recv = humanbytes(psutil.net_io_counters().bytes_recv)

    msg = (
        f"<b>Bot Current Status</b>\n\n"
        f"<b>Restarted on {restart_time}</b>\n"
        f"<b>Bot Uptime</b>: {hr}:{mi}:{se}\n\n"
        f"<b>Total disk space:</b> {total}\n"
        f"<b>Used :</b> {used}\n"
        f"<b>Free :</b> {free}\n"
        # f"<b>RAM Usage:</b> {ram}%\n"
        # f"<b>CPU Usage:</b> {cpu}%\n"
        # f"<b>Downloaded Data:</b> {recv} 🔻\n"
        # f"<b>Uploaded Data:</b> {sent} 🔺"
    )

    await message.reply_text(msg, quote=True)
