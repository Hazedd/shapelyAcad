import array

from pyautocad import APoint, Autocad
from shapely.geometry import LineString, Point


class AutocadService:
    acad = Autocad(create_if_not_exists=True)

    @staticmethod
    def autocad_polyline_to_coordinates(autocad_line_obj, number_of_coordinates):
        res = tuple(
            autocad_line_obj.Coordinates[n : n + number_of_coordinates]
            for n, i in enumerate(autocad_line_obj.Coordinates)
            if n % number_of_coordinates == 0
        )
        return res

    @classmethod
    def get_shapely_from_cad_object(cls, cad_object):
        if cad_object.ObjectName in ["AcDbPoint"]:
            return Point(cad_object.Coordinates)
        elif cad_object.ObjectName in ["AcDbLine"]:
            return LineString([cad_object.StartPoint, cad_object.EndPoint])
        elif cad_object.ObjectName in ["AcDbPolyline"]:
            return LineString(cls.autocad_polyline_to_coordinates(cad_object, 2))
        elif cad_object.ObjectName in ["AcDb3dPolyline"]:
            return LineString(cls.autocad_polyline_to_coordinates(cad_object, 3))

    @classmethod
    def init_autocad_selection_and_get_shapely(cls):
        selection = cls.acad.get_selection()
        shapely_objects = [cls.get_shapely_from_cad_object(item) for item in selection]
        return shapely_objects

    @classmethod
    def draw_polyline_2d(cls, shapely_line, color=None):
        points_2d = [coord for coords in shapely_line.coords[:] for coord in coords]
        points_double = array.array("d", points_2d)
        line = cls.acad.model.AddLightWeightPolyline(points_double)
        if color is not None:
            line.Color = color

    @classmethod
    def draw_polyline_3d(cls, shapely_line, color=None):
        points_3d = [coord for coords in shapely_line.coords[:] for coord in coords]
        points_double = array.array("d", points_3d)
        line = cls.acad.model.Add3Dpoly(points_double)
        if color is not None:
            line.Color = color

    @classmethod
    def draw_point(cls, shapely_point, color=None):
        # todo: add draw as circle option
        if shapely_point.has_z:
            p = APoint(shapely_point.x, shapely_point.y, shapely_point.z)
            point = cls.acad.model.AddPoint(p)
        else:
            p = APoint(shapely_point.x, shapely_point.y)
            point = cls.acad.model.AddPoint(p)

        if color is not None:
            point.Color = color

    @staticmethod
    def get_profile(line, distance):
        if distance <= 0.0 or distance >= line.length:
            return [LineString(line)]
        coords = list(line.coords)
        for i, p in enumerate(coords):
            pd = line.project(Point(p))
            if pd == distance:
                return [LineString(coords[: i + 1]), LineString(coords[i:])]
            if pd > distance:
                cp = line.interpolate(distance)
                if cp.has_z:
                    return [
                        LineString(coords[:i] + [(cp.x, cp.y, cp.z)]),
                        LineString([(cp.x, cp.y, cp.z)] + coords[i:]),
                    ]
                else:
                    return [
                        LineString(coords[:i] + [(cp.x, cp.y)]),
                        LineString([(cp.x, cp.y)] + coords[i:]),
                    ]


class ShapelyAcad:
    def draw_shapely(self, shapely_object, color: int = None):
        if shapely_object.geom_type == "LineString":
            if shapely_object.has_z:
                AutocadService.draw_polyline_3d(shapely_object, color)
            else:
                AutocadService.draw_polyline_2d(shapely_object, color)

        elif shapely_object.geom_type == "Point":
            AutocadService.draw_point(shapely_object, color)

        elif shapely_object.geom_type == "MultiLineString":
            for linestring in shapely_object:
                if linestring.has_z:
                    AutocadService.draw_polyline_3d(linestring)
                else:
                    AutocadService.draw_polyline_2d(linestring)

        elif shapely_object.geom_type == "Polygon":
            raise NotImplementedError("Polygon")

        else:
            print(shapely_object.geom_type)
            raise NotImplementedError

    def draw_text(self, text_value, point=Point(), size=0.2):
        # todo: add to service
        AutocadService.acad.model.AddText(f"{text_value}", APoint(point.x, point.y), size)

    def get_shapelies_from_selection(self):
        return AutocadService.init_autocad_selection_and_get_shapely()

    def draw_profile(self, shapelyLineObject, fromDistance, toDistance):
        if toDistance <= fromDistance:
            raise ValueError("toDistance less or equeal as fromDistance")

        LineToEnd = LineString(
            [list(x.coords) for x in AutocadService.get_profile(shapelyLineObject, toDistance)][0]
        )
        cutFrontAndEndPoint = [list(x.coords) for x in AutocadService.get_profile(LineToEnd, fromDistance)]
        if len(cutFrontAndEndPoint) <= 1:
            cuttedLine = LineString(cutFrontAndEndPoint[0])
        else:
            cuttedLine = LineString(cutFrontAndEndPoint[1])

        self.draw_shapely(cuttedLine)
        return cuttedLine
