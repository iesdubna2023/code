import logging


def test_segment2d_area(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Segment2D.area for %s", surname)
        s = m.Segment2D(m.Point2D(0, 0), m.Point2D(1, 0))
        assert s.area() == 0
        logging.info("Test Segment2D.area for %s: OK", surname)


def test_segment2d_mirror_point(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Segment2D.mirror_point for %s", surname)
        s = m.Segment2D(m.Point2D(1, 0), m.Point2D(0, 1))
        mp = m.Point2D(0, 0)
        news = s.mirror_point(mp)
        assert news.p1.x == -1
        assert news.p1.y == 0
        assert news.p2.x == 0
        assert news.p2.y == -1
        logging.info("Test Segment2D.mirror_point for %s: OK", surname)


def test_segment2d_mirror_line(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Segment2D.mirror_line for %s", surname)
        s = m.Segment2D(m.Point2D(0, 1), m.Point2D(1, 1))
        ml = m.Segment2D(m.Point2D(0, 0), m.Point2D(1, 0))
        news = s.mirror_line(ml)
        assert news.p1.x == 0
        assert news.p1.y == -1
        assert news.p2.x == 1
        assert news.p2.y == -1
        logging.info("Test Segment2D.mirror_line for %s: OK", surname)


def test_segment2d_belongs_point(iter_homework):
    for surname, m in iter_homework(3):
        logging.info("Test Segment2D.belongs_point for %s", surname)
        s = m.Segment2D(m.Point2D(0, 0), m.Point2D(1, 0))
        bp1 = m.Point2D(0.5, 0)
        bp2 = m.Point2D(2, 0)
        assert s.belongs_point(bp1)
        assert not s.belongs_point(bp2)
        logging.info("Test Segment2D.belongs_point for %s: OK", surname)
