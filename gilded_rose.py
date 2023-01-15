# -*- coding: utf-8 -*-


TAFKAL80ETC_CONCERT_PASS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE_ITEM_NAME = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED_ITEM = "CONJURED-ITEM"

CONCERT_PASSES = [TAFKAL80ETC_CONCERT_PASS, AGED_BRIE_ITEM_NAME]
REGULAR_CONCERT_PASSES = [TAFKAL80ETC_CONCERT_PASS]
SPECIAL_CONCERT_PASSES = [AGED_BRIE_ITEM_NAME]
LEGENDARY_ITEMS = [SULFURAS]
CONJURED_ITEMS = [CONJURED_ITEM]

MAX_ITEM_QUALITY = 50


def quality_can_be_deducted(item: "Item") -> bool:
    return item.quality > 0 and item.name not in LEGENDARY_ITEMS


def reduce_item_quality(item: "Item") -> "Item":
    if item.name in CONCERT_PASSES:
        if item.quality < MAX_ITEM_QUALITY:
            item.quality += 1

            if item.name in REGULAR_CONCERT_PASSES:
                if item.sell_in < 11:
                    item.quality += 1
                if item.sell_in < 6:
                    item.quality += 1

            item.quality = item.quality if item.quality < MAX_ITEM_QUALITY else MAX_ITEM_QUALITY
    elif item.name in CONJURED_ITEMS:
        item.quality = item.quality - 2
    elif quality_can_be_deducted(item):
        item.quality = item.quality - 1

    return item


def reduce_item_sell_in(item: "Item") -> "Item":
    if item.name not in LEGENDARY_ITEMS:
        item.sell_in = item.sell_in - 1

    return item


def update_quality_for_expired_item(item: "Item") -> "Item":
    if item.name == AGED_BRIE_ITEM_NAME:
        if item.quality < MAX_ITEM_QUALITY:
            item.quality = item.quality + 1
    elif item.name not in REGULAR_CONCERT_PASSES:
        if quality_can_be_deducted(item):
            item.quality = item.quality - 1
    else:
        item.quality = 0

    return item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            reduce_item_quality(item)
            reduce_item_sell_in(item)

            if item.sell_in < 0:
                update_quality_for_expired_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
