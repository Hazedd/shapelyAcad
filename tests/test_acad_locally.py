# from shapely.geometry import LineString, Point
# from shapelyAcad import ShapelyAcad


class TestSimplePolyline:

    #####
    # All local needs interaction with autocad
    #####

    # acad = ShapelyAcad()

    def test_point_2d(self):
        pass
        # point = Point([6, 3])
        # self.acad.draw_shapely(point, color=3)
        # self.acad.draw_text("Sample Text", point)

    def test_point_3d(self):
        pass
        # point = Point([6, 3, 5])
        # self.acad.draw_shapely(point)
        # self.acad.draw_text("Sample Text", point)

    def test_line_2d(self):
        pass
        # line = LineString([[3, 0], [3, 10], [3, 20], [3, 30]])
        # self.acad.draw_shapely(line, color=3)

    def test_line_3d(self):
        pass
        # line = LineString([[3, 0, 0], [3, 10, 0], [3, 20, 0], [3, 30, 0]])
        # self.acad.draw_shapely(line, color=3)
        # self.acad.draw_profile(line, 5, 10)

    def test_get_shapely_from_selection(self):
        pass
        # list_of_shapley_objects = self.acad.get_shapelies_from_selection()