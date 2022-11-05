from shapely.geometry import Point, LineString

from shapelyAcad import AutocadService


class TestSimplePolyline:

    def test_init_2d(self):

        acad = AutocadService()

        # draw point in AutoCAD
        point = Point([6, 3])
        acad.DrawShapelyObject(point)
        acad.DrawText("Sample Text", point)

        # draw line in AutoCAD
        line = LineString([[3, 0, 0], [3, 10, 0], [3, 20, 0], [3, 30, 0]])
        acad.DrawShapelyObject(line, color=3)
        acad.DrawProfileOverLine(line, 5, 10)

        # select objects from AutoCAD
        list_of_shapley_objects = acad.GetShapelyListFromSelection()
