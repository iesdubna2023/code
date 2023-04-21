import logging


def test_point2d_area(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Point2D.area for %s", surname)
        p = m.Point2D(0, 0)
        assert p.area() == 0
        logging.info("Test Point2D.area for %s: OK", surname)


def test_point2d_mirror_point(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Point2D.mirror_point for %s", surname)
        p = m.Point2D(1, 1)
        mp = m.Point2D(1, 0)
        newp = p.mirror_point(mp)
        assert newp.x == 1
        assert newp.y == -1
        logging.info("Test Point2D.mirror_point for %s: OK", surname)


def test_point2d_mirror_line(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Point2D.mirror_line for %s", surname)
        p = m.Point2D(1, 1)
        ml = m.Segment2D(m.Point2D(0, 0), m.Point2D(1, 0))
        newp = p.mirror_line(ml)
        assert newp.x == 1
        assert newp.y == -1
        logging.info("Test Point2D.mirror_line for %s: OK", surname)


def test_point2d_belongs_point(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Point2D.belongs_point for %s", surname)
        p = m.Point2D(1, 1)
        bp1 = m.Point2D(0, 0)
        bp2 = m.Point2D(1, 1)
        assert not p.belongs_point(bp1)
        assert p.belongs_point(bp2)
        logging.info("Test Point2D.belongs_point for %s: OK", surname)
