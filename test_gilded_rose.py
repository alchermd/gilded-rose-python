# -*- coding: utf-8 -*-
from typing import List

from gilded_rose import Item, GildedRose


def update_quality(items: List[Item]) -> List[Item]:
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items


def test_foo():
    items = update_quality([Item("foo", 0, 0)])
    assert "foo" == items[0].name


def test_sell_in_is_reduced():
    items = update_quality([Item("NORMAL-ITEM", 5, 0)])
    assert items[0].sell_in == 4


def test_sell_in_is_not_reduced_for_legendary_items():
    items = update_quality([Item("Sulfuras, Hand of Ragnaros", 5, 0)])
    assert items[0].sell_in == 5


def test_aged_brie_increases_in_quality_the_older_it_gets():
    items = update_quality([Item("Aged Brie", -1, 0)])
    assert items[0].quality == 2


def test_item_quality_is_reduced():
    items = update_quality([Item("NORMAL-ITEM", 5, 5)])
    assert items[0].quality == 4


def test_quality_of_expired_items_gets_reduced():
    items = update_quality([Item("NORMAL-ITEM", -1, 5)])
    assert items[0].quality == 3


def test_quality_of_legendary_items_dont_get_reduced():
    items = update_quality([Item("Sulfuras, Hand of Ragnaros", -1, 5)])
    assert items[0].quality == 5


def test_quality_of_passes_becomes_zero_once_expired():
    items = update_quality([Item("Backstage passes to a TAFKAL80ETC concert", -1, 5)])
    assert items[0].quality == 0


def test_quality_of_passes_increases_by_two_if_the_event_happens_in_10_days_or_less():
    items = update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 10, 5)])
    assert items[0].quality == 7


def test_quality_of_passes_increases_by_three_if_the_event_happens_in_5_days_or_less():
    items = update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)])
    assert items[0].quality == 8


def test_quality_of_items_never_go_negative():
    items = update_quality([Item("NORMAL-ITEM", 5, 0)])
    assert items[0].quality == 0


def test_quality_of_items_never_go_above_50():
    items = update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)])
    assert items[0].quality == 50


def test_item_string_representation():
    item = Item("NORMAL-ITEM", 10, 5)
    assert str(item) == "NORMAL-ITEM, 10, 5"
