# shapelyAcad, draw shapely objects in autocad

Easy draw shapely objects in autocad by using pyAutocad.

## Installation

```bash
pip install shapelyAcad
```

### Warning if you use this project make sure to pin the version, api is far from stable!

# Usage:

```python
from shapely.geometry import Point, LineString
from shapelyAcad import ShapelyAcad

s_acad = ShapelyAcad()

# draw point in AutoCAD
point = Point([6, 3])
s_acad.draw_shapely(point)
s_acad.draw_text("Sample Text", point)

# draw line in AutoCAD
# line = LineString([[3, 0], [3, 10], [3, 20], [3, 30]])
line = LineString([[3, 0, 0], [3, 10, 0], [3, 20, 0], [3, 30, 0]])
s_acad.draw_shapely(line, color=3)
s_acad.draw_profile(line, 5, 10)

# select objects from AutoCAD
list_of_shapley_objects = s_acad.get_shapelies_from_selection()

```

# Contribute
Feel free to do some black math magic, add test or make suggestions.

## Requirements 
pyproject.toml to manage requirements and can be build by a newer build backend.

## Build and Test
Install MakeFile for quality of life

After setting up a venv we use `make install` to build a fresh pulled repo

Code quality checks and testing needs to be passed and will be checked on every commit and in the pipeline. If code wont pass it wont commit so make sure to check it before with make check-all!

We use:
- flit as a build-backend. 
- pytest for testing, manual by `make test` in a console.
- flake8 and black for linting, manual by `make lint` in a console.
- myPy for typechecking, manual by `make typecheck` in a console.
- black and isort, manual by `make format` in a console.
- bumpversion for changing the version

## Testing
Make an effort to test each bit of functionality you add. Try to keep it simple.

# Links
- [make](https://www.gnu.org/software/make/manual/make.html)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [black](https://github.com/psf/black)
- [myPy](https://mypy.readthedocs.io/en/stable/)
- [iSort](https://github.com/PyCQA/isort)
- [flit](https://flit.pypa.io/en/latest/)
- [bumpversion](https://github.com/peritus/bumpversion)

