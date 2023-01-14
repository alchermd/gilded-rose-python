# -*- coding: utf-8 -*-

NORMAL_ITEM_NAME = "NORMAL-ITEM"
BACKSTAGE_PASS_ITEM_NAME = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE_ITEM_NAME = "Aged Brie"
LEGENDARY_ITEM_NAME = "Sulfuras, Hand of Ragnaros"
PASS_ITEMS = [BACKSTAGE_PASS_ITEM_NAME, AGED_BRIE_ITEM_NAME]
MAX_ITEM_QUALITY = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def _quality_can_be_deducted(item: "Item") -> bool:
        return item.quality > 0 and item.name != LEGENDARY_ITEM_NAME

    def update_quality(self):
        for item in self.items:
            if item.name in PASS_ITEMS:
                if item.quality < MAX_ITEM_QUALITY:
                    item.quality += 1
                    if item.name == BACKSTAGE_PASS_ITEM_NAME:
                        if item.sell_in < 11:
                            item.quality += 1
                        if item.sell_in < 6:
                            item.quality += 1

                    item.quality = item.quality if item.quality < MAX_ITEM_QUALITY else MAX_ITEM_QUALITY
            else:
                if self._quality_can_be_deducted(item):
                    item.quality = item.quality - 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
