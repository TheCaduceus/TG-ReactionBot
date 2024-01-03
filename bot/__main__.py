from bot import TelegramBot, logger

if __name__ == '__main__':
    logger.info('Initializing...')
    TelegramBot.run()