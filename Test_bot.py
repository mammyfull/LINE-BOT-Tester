#!/usr/bin/python
#-*-coding: utf-8 -*-

from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
 SourceUser, SourceGroup, SourceRoom,
 TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
 ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
 CarouselTemplate, CarouselColumn, PostbackEvent,
 StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
 ImageMessage, VideoMessage, AudioMessage,
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

line_bot_api = LineBotApi('lK+LiftMxJYs2X3wm0XzcykDvsJO8j8VY9R2xdxLzbjACs6RF0SpXkUP/Q3BLVXePKM6aF+RM7HkK5ExlTbDBS1FicGR1GHLdEakqLcun0+a4QnhW2+wBkQW7yRkUNAsjiU3EeP4khtaxqfDrVTj3gdB04t89/1O/w1cDnyilFU=')

try:
    line_bot_api.push_message('Ucf88fc62d218cfd2f42f358ff16c8551', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
