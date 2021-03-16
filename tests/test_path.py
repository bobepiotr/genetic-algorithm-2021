import unittest

import ga.point as pt
import ga.step as st
import ga.path as pa
from ga.const import *


class TestPath(unittest.TestCase):
    def setUp(self):
        self.step1 = st.Step(5, LEFT)
        self.step2 = st.Step(4, UP)
        self.step3 = st.Step(1, RIGHT)
        self.step_list = [self.step1, self.step2, self.step3]

    def test_add_step(self):
        path = pa.Path()
        path.add_step(self.step1)
        path.add_step(self.step2)
        path.add_step(self.step3)

        self.assertEqual(path.step_list, self.step_list)

    def test_convert_to_point_list(self):
        start = pt.Point(3, 4)
        p_list = [pt.Point(3, 4), pt.Point(2, 4), pt.Point(1, 4), pt.Point(0, 4), pt.Point(-1, 4), pt.Point(-2, 4),
                  pt.Point(-2, 3), pt.Point(-2, 2), pt.Point(-2, 1), pt.Point(-2, 0),
                  pt.Point(-1, 0)]

        path = pa.Path(start)
        path.step_list = self.step_list
        point_list = path.convert_point_list()
        self.assertEqual(point_list, p_list)

    def test_concat(self):
        path = pa.Path(pt.Point(2,3), pt.Point(3,4))
        step1 = st.Step(4, LEFT)
        step2 = st.Step(4, RIGHT)
        step3 = st.Step(3, RIGHT)
        step4 = st.Step(6, RIGHT)
        step5 = st.Step(10, UP)
        step_list = [step1, step2, step3, step4, step5]
        path.step_list = step_list
        path.concat_same_direction_steps()

        self.assertEqual(path.step_list, [st.Step(4, LEFT), st.Step(13, RIGHT), st.Step(10, UP)])

    def test_remove_zero_steps(self):
        path = pa.Path(pt.Point(2, 3), pt.Point(3, 4))
        step1 = st.Step(0, LEFT)
        step2 = st.Step(0, RIGHT)
        step3 = st.Step(3, RIGHT)
        step4 = st.Step(6, RIGHT)
        step5 = st.Step(0, UP)
        step_list = [step1, step2, step3, step4, step5]
        path.step_list = step_list
        path.remove_zero_steps()

        self.assertEqual(path.step_list, [st.Step(3, RIGHT), st.Step(6, RIGHT)])


if __name__ == '__main__':
    unittest.main()
