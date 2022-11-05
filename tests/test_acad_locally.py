# from shapely.geometry import LineString, Point
# from shapelyAcad import ShapelyAcad


class TestSimplePolyline:
    def test_init_2d(self):
        pass
        ######
        # All local needs interaction with autocad
        ######
        #
        # acad = ShapelyAcad()
        #
        # # draw point in AutoCAD
        # point = Point([6, 3])
        # acad.draw_shapely(point)
        # acad.draw_text("Sample Text", point)
        #
        # # draw line in AutoCAD
        # # line = LineString([[3, 0], [3, 10], [3, 20], [3, 30]])
        # line = LineString([[3, 0, 0], [3, 10, 0], [3, 20, 0], [3, 30, 0]])
        # acad.draw_shapely(line, color=3)
        # acad.draw_profile(line, 5, 10)
        #
        # select objects from AutoCAD, only when autocad is installed.
        # list_of_shapley_objects = acad.GetShapelyListFromSelection()
