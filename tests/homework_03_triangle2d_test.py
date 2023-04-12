import logging


def test_triangle2d_area(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Triangle2D.area for %s", surname)
        s = m.Triangle2D(m.Point2D(0, 0), m.Point2D(1, 0), m.Point2D(0, 1))
        assert s.area() == 0.5
        logging.info("Test Triangle2D.area for %s: OK", surname)


def test_triangle2d_mirror_point(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Triangle2D.mirror_point for %s", surname)
        t = m.Triangle2D(m.Point2D(1, 0), m.Point2D(2, 0), m.Point2D(1, 1))
        mp = m.Point2D(0, 0)
        newt = t.mirror_point(mp)
        assert newt.p1.x == -1
        assert newt.p1.y == 0
        assert newt.p2.x == -2
        assert newt.p2.y == 0
        assert newt.p3.x == -1
        assert newt.p3.y == -1
        logging.info("Test Triangle2D.mirror_point for %s: OK", surname)


def test_triangle2d_mirror_line(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Triangle2D.mirror_line for %s", surname)
        t = m.Triangle2D(m.Point2D(1, 1), m.Point2D(2, 1), m.Point2D(1, 2))
        ml = m.Segment2D(m.Point2D(0, 0), m.Point2D(0, 1))
        newt = t.mirror_line(ml)
        assert newt.p1.x == -1
        assert newt.p1.y == 1
        assert newt.p2.x == -2
        assert newt.p2.y == 1
        assert newt.p3.x == -1
        assert newt.p3.y == 2
        logging.info("Test Triangle2D.mirror_line for %s: OK", surname)


def test_triangle2d_belongs_point(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Triangle2D.belongs_point for %s", surname)
        t = m.Triangle2D(m.Point2D(1, 1), m.Point2D(2, 1), m.Point2D(1, 2))
        bp1 = m.Point2D(0.2, 0.2)
        bp2 = m.Point2D(1, 1)
        assert t.belongs_point(bp1)
        assert not t.belongs_point(bp2)
        logging.info("Test Triangle2D.belongs_point for %s: OK", surname)
