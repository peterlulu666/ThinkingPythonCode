import unittest
import Car


class TestCar(unittest.TestCase):
    def test_init(self):
        car = Car.Car()
        self.assertEqual(car.make, 'Powell')
        self.assertEqual(car.model, 'The Homer')
        self.assertEqual(car.year, 1991)
        self.assertAlmostEqual(car.price, 82000.0​)

    def main():
        unittest.main(verbosity=3)

    main()
