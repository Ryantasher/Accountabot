from lib.bot import bot
from lib.bot import __init__
import logging

logger = logging.getLogger(__name__)

VERSION = "0.0.0"

bot.run(VERSION)
