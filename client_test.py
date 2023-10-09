import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for q in quotes:
      self.assertEqual(getDataPoint(q),(q['stock'], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for q in quotes:
      self.assertEqual(getDataPoint(q),(q['stock'], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_AandBareDifferent(self):
    self.assertEqual(round(getRatio(2, 1.5), 4), 1.3333)
    self.assertEqual(round(getRatio(1, 2.5), 4), 0.4000)

  def test_getDataPoint_AandBAre0(self):
   self.assertEqual(getRatio(0,2), 0)
   self.assertEqual(getRatio(2, 0), None)


if __name__ == '__main__':
    unittest.main()
