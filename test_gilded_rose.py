# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_update_quality_decrements_sell_in_for_items_that_arent_sulfuras():
    items = [Item("NON-SULFURAS", 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4


def test_aged_brie_increases_in_quality_the_older_it_gets():
    items = [Item("Aged Brie", -1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 2


def test_item_quality_is_reduced():
    items = [Item("NORMAL-ITEM", 5, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 4
