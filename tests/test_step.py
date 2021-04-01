import unittest
import ga.structures.step as st
import ga.structures.point as p
from ga.const import *
import copy


class TestStep(unittest.TestCase):
    def setUp(self):
        self.start = p.Point(0, 0)

    def test_convert_to_point_list_right(self):
        step = st.Step(3, RIGHT)
        act_point, point_list = step.convert_to_point_list(self.start)
        self.assertEqual(point_list, [p.Point(0, 0), p.Point(1, 0), p.Point(2, 0)])
        self.assertEqual(act_point, p.Point(3, 0))

    def test_convert_to_point_list_left(self):
        step = st.Step(3, LEFT)
        act_point, point_list = step.convert_to_point_list(self.start)
        self.assertEqual(point_list, [p.Point(0, 0), p.Point(-1, 0), p.Point(-2, 0)])
        self.assertEqual(act_point, p.Point(-3, 0))

    def test_convert_to_point_list_up(self):
        step = st.Step(3, UP)
        act_point, point_list = step.convert_to_point_list(self.start)
        self.assertEqual(point_list, [p.Point(0, 0), p.Point(0, -1), p.Point(0, -2)])
        self.assertEqual(act_point, p.Point(0, -3))

    def test_convert_to_point_list_down(self):
        step = st.Step(3, DOWN)
        act_point, point_list = step.convert_to_point_list(self.start)
        self.assertEqual(point_list, [p.Point(0, 0), p.Point(0, 1), p.Point(0, 2)])
        self.assertEqual(act_point, p.Point(0, 3))

    def test_set_oppose_direction_right(self):
        step = st.Step(3, RIGHT)
        step.set_oppose_direction()
        self.assertEqual(step, st.Step(-3, LEFT))

    def test_set_oppose_direction_left(self):
        step = st.Step(3, LEFT)
        step.set_oppose_direction()
        self.assertEqual(step, st.Step(-3, RIGHT))

    def test_set_oppose_direction_up(self):
        step = st.Step(3, UP)
        step.set_oppose_direction()
        self.assertEqual(step, st.Step(-3, DOWN))

    def test_set_oppose_direction_down(self):
        step = st.Step(3, DOWN)
        step.set_oppose_direction()
        self.assertEqual(step, st.Step(-3, UP))

    def test_copy(self):
        step = st.Step(3, DOWN)
        step_copy = copy.deepcopy(step)
        self.assertEqual(step is step_copy, False)
        self.assertEqual(step == step_copy, True)


if __name__ == '__main__':
    unittest.main()
