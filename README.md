# PyMO
A library for using motion capture data for machine learning

**This library is currently highly experimental and everything is subject to change :)**


## Roadmap
* Mocap Data Parsers and Writers

## Current Features
* [Read BVH Files](#read-bvh-files)
* Crop BVH Files
* Write BVH Files

### Read BVH Files

```python
from pymo.parsers import BVHParser
import pymo.viz_tools

parser = BVHParser()

parsed_data = parser.parse('data/AV_8Walk_Meredith_HVHA_Rep1.bvh')
```

## Feedback, Bugs, and Questions
For any questions, feedback, and bug reports, please use the [Github Issues](https://github.com/omimo/PyMO/issues).

## Credits
Created by [Omid Alemi](https://omid.al/projects/)


## License
This code is available under the [MIT license](http://opensource.org/licenses/MIT).
