from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
line_bot_api = LineBotApi('brOMDu5QcOnD+wdlnGh/YAixgUBZgf7O9F72OW+Fa15xv9Msdx6zPEP4+KUFqQKALU9+kcs/lF0ce4ZtlhNwqSR0gb5mV7PXvdK0A340fSGoPsCFgRFJOy1J5zeqhVS899Cg2PvMztAFFZNSaKN7lgdB04t89/1O/w1cDnyilFU='
)
UserID = 'U16b6c72cd097c620df323756df3dcf22'

text_message = TextSendMessage(text = '王伯很憨')
line_bot_api.push_message(UserID, text_message)

Sticker_message = StickerSendMessage(package_id = '789', sticker_id = '10855')
line_bot_api.push_message(UserID, Sticker_message)

image_message = ImageSendMessage(
    original_content_url='https://i.imgur.com/xyPtn4m.jpeg',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg')
line_bot_api.push_message(UserID,image_message)

location_message = LocationSendMessage(
    title='CodingAPE猿創力程式設計學校',
    address='台北市信義區基隆路一段180號',
    latitude=25.042408,
    longitude=121.564839)
line_bot_api.push_message(UserID,location_message)

video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)
