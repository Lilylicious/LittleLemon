from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(Title='IceCream', Price=80, Inventory=100)
        MenuItem.objects.create(Title='HotDogs', Price=1337, Inventory=50)
        MenuItem.objects.create(Title='Bananas', Price=69, Inventory=3)

    def test_getall(self):
        test_item_1 = MenuItem.objects.get(Title='IceCream')
        test_item_2 = MenuItem.objects.get(Title='HotDogs')
        test_item_3 = MenuItem.objects.get(Title='Bananas')

        self.assertEqual(test_item_1.Price, 80)
        self.assertEqual(test_item_2.Price, 1337)
        self.assertEqual(test_item_3.Price, 69)
        
        self.assertEqual(test_item_1.Inventory, 100)
        self.assertEqual(test_item_2.Inventory, 50)
        self.assertEqual(test_item_3.Inventory, 3)