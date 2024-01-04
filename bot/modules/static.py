from bot.config import Telegram

WelcomeText = \
"""
Hi **%(first_name)s**, send me a message or designate me as an admin in your groups. I'll promptly respond by attaching my reaction to the received message.

- /start to get this message.
- /emojis to get supported emojis. 
"""

SupportedEmojisText = \
"""
**I currently support following emojis:**
""" + '\n'.join(' '.join(Telegram.EMOJIS[i:i+5]) for i in range(0, len(Telegram.EMOJIS), 5))
