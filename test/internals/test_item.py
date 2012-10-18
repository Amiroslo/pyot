from test.framework import FrameworkTestGame

class TestItem(FrameworkTestGame):
    def test_transformitem(self):
        """ This report: http://vapus.net/forum/pyot-opentibia-server-287/debug-serious-bugs-thread-2925-100/#post31523 """
        position = Position(1000,1000,7)
        
        item = Item(2148)
        
        tile = position.getTile()
        
        tile.placeItem(item)
        
        transformItem(item, 2149, position)
        
        self.assertEqual(item.itemId, 2149)
        
        # Transform back, and to 0. These should work too.
        item.transform(2148, position)
        item.transform(0, position)
        
        