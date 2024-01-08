#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from assets.s_and_p_500 import S_And_P_500
from waveshare_epd import epd3in52
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd3in52 Demo")
    
    epd = epd3in52.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.display_NUM(epd.WHITE)
    epd.lut_GC()
    epd.refresh()

    epd.send_command(0x50)
    epd.send_data(0x17)
    
    # font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    # font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    # font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    # Drawing on the Horizontal image
    asset_to_show = S_And_P_500()
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    font = ImageFont.truetype("font.ttf", size=60)
    draw.text((10, 0), asset_to_show.name, font=font, fill = 0)
    draw.text((epd.height//2, 0), asset_to_show.price, font=font, fill = 0)
    epd.display(epd.getbuffer(Himage.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)))
    epd.lut_GC()
    epd.refresh()
    time.sleep(2)
    
    # logging.info("3.read bmp file")
    # Himage = Image.open(os.path.join(picdir, '3in52-1.bmp'))
    # epd.display(epd.getbuffer(Himage.transpose(Image.FLIP_TOP_BOTTOM)))
    # epd.lut_GC()
    # epd.refresh()
    # time.sleep(2)
    
    # logging.info("4.read bmp file on window")
    # Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    # Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2.transpose(Image.FLIP_TOP_BOTTOM)))
    # epd.lut_GC()
    # epd.refresh()
    # time.sleep(2)


    # print("Quick refresh is supported, but the refresh effect is not good, but it is not recommended")
    # Himage = Image.open(os.path.join(picdir, '3in52-2.bmp'))
    # epd.display(epd.getbuffer(Himage))
    # epd.lut_DU()
    # epd.refresh()
    # time.sleep(2)

    # Himage = Image.open(os.path.join(picdir, '3in52-3.bmp'))
    # epd.display(epd.getbuffer(Himage))
    # epd.lut_DU()
    # epd.refresh()
    # time.sleep(2)


    logging.info("Clear...")
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd3in52.epdconfig.module_exit(cleanup=True)
    exit()