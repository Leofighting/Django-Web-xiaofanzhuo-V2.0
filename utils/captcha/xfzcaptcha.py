# -*- coding:utf-8 -*-
__author__ = "leo"

import random
import time
import os
import string
from PIL import Image, ImageDraw, ImageFont


class Captcha(object):
    """验证码"""
    font_path = os.path.join(os.path.dirname(__file__), "verdana.ttf")
    number = 4
    size = (100, 40)
    bg_color = (9, 9, 9)
    random.seed(int(time.time()))
    font_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
    font_size = 22
    line_color = (random.randint(0, 222), random.randint(0, 222), random.randint(0, 222))
    draw_line = True
    draw_point = True
    line_number = 3

    SOURCE = list(string.ascii_letters)
    for index in range(0, 10):
        SOURCE.append(str(index))

    NUMBER = [str(i) for i in range(0, 10)]

    @classmethod
    def gene_text(cls):
        """随机生成字符"""
        return "".join(random.sample(cls.SOURCE, cls.number))

    @classmethod
    def gene_number(cls):
        """随机生成数字"""
        return "".join(random.sample(cls.NUMBER, cls.number))

    @classmethod
    def __gene_line(cls, draw, width, height):
        """绘制干扰线"""
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=cls.line_color)

    @classmethod
    def __gene_points(cls, draw, point_chance, width, height):
        """绘制干扰点"""
        chance = min(100, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    @classmethod
    def gene_code(cls):
        """生成验证码图片"""
        width, height = cls.size
        image = Image.new("RGBA", (width, height), cls.bg_color)
        font = ImageFont.truetype(cls.font_path, cls.font_size)
        draw = ImageDraw.Draw(image)
        text = cls.gene_text()
        font_width, font_height = font.getsize(text)
        draw.text(((width - font_width) / 2, (height - font_height) / 2), text, font=font, fill=cls.font_color)
        if cls.draw_line:
            for x in range(0, cls.line_number):
                cls.__gene_line(draw, width, height)
        if cls.draw_point:
            cls.__gene_points(draw, 10, width, height)

        return text, image
