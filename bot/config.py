#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "16732227")
    API_HASH = config("API_HASH", "8b5594ad7ad37f3a0a7ddbfb3963bb51")
    BOT_TOKEN = config("BOT_TOKEN", "7166838432:AAGINOHgckdiIwV8z67I9LvGM5ptKoisvpE")
    DEV = 5868426717
    OWNER = config("OWNER", "5868426717")
    ffmpegcode = ["-preset veryfast -c:v libx265 -b:a 64k -crf 38 -map 0 -c:s copy"]
    THUMB = config("THUMB", "https://static7.depositphotos.com/1009183/713/i/950/depositphotos_7132926-stock-photo-beautiful-tree-in-the-sunset.jpg")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
