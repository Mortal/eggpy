from eggy.eggy import Eggy
from eggy import settings
import asyncore


if __name__ == "__main__":
    bot = Eggy()
    bot.connect(settings.SERVER)
    try:
        while asyncore.socket_map:
            prev_count = bot.event_count
            asyncore.poll(1)
            if bot.event_count == prev_count:
                bot.inactive()
    except KeyboardInterrupt:
        bot.logger.error("Keyboard interrupt")
    except Exception as exn:
        bot.logger.error("Unhandled exception "+str(type(exn)))
        bot.logger.error(str(exn))
