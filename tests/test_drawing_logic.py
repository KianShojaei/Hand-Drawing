"""Unit tests for drawing-segment selection."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "DrawTable"))
from drawing_logic import get_drawing_segments


class DrawingLogicTests(unittest.TestCase):
    def test_first_single_hand_frame_sets_anchor_without_drawing(self):
        point = (10, 20)
        segments, anchor = get_drawing_segments([point], None, True)
        self.assertEqual(segments, [])
        self.assertEqual(anchor, point)

    def test_single_hand_draws_between_consecutive_frames(self):
        previous = (10, 20)
        current = (30, 40)
        segments, anchor = get_drawing_segments([current], previous, True)
        self.assertEqual(segments, [(previous, current)])
        self.assertEqual(anchor, current)

    def test_two_hands_draw_a_segment_between_fingertips(self):
        left_tip = (10, 20)
        right_tip = (90, 80)
        segments, anchor = get_drawing_segments([left_tip, right_tip], (50, 50), True)
        self.assertEqual(segments, [(left_tip, right_tip)])
        self.assertIsNone(anchor)

    def test_no_hands_reset_anchor(self):
        segments, anchor = get_drawing_segments([], (10, 20), True)
        self.assertEqual(segments, [])
        self.assertIsNone(anchor)

    def test_paused_mode_does_not_draw_and_resets_anchor(self):
        segments, anchor = get_drawing_segments([(30, 40)], (10, 20), False)
        self.assertEqual(segments, [])
        self.assertIsNone(anchor)

    def test_two_hand_to_single_hand_transition_does_not_bridge_old_points(self):
        segments, anchor = get_drawing_segments([(30, 40)], None, True)
        self.assertEqual(segments, [])
        self.assertEqual(anchor, (30, 40))


if __name__ == "__main__":
    unittest.main()
