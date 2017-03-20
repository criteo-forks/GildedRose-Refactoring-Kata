# -*- coding: utf-8 -*-
"""
Do not run this file directly, use ``py.test`` instead.
"""


from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "fixme"
