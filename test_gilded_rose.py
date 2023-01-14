# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_sell_in_is_reduced():
    items = [Item("NORMAL-ITEM", 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4


def test_sell_in_is_not_reduced_for_legendary_items():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 5


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


def test_quality_of_expired_items_gets_reduced():
    items = [Item("NORMAL-ITEM", -1, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 3


def test_quality_of_legendary_items_dont_get_reduced():
    items = [Item("Sulfuras, Hand of Ragnaros", -1, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 5


def test_quality_of_passes_becomes_zero_once_expired():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_quality_of_passes_increases_by_two_if_the_event_happens_in_10_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 7


def test_quality_of_passes_increases_by_three_if_the_event_happens_in_5_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 8


def test_item_string_representation():
    item = Item("NORMAL-ITEM", 10, 5)
    assert str(item) == "NORMAL-ITEM, 10, 5"
