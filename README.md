## Walking model for Lower Limb Exoskeleton 

[Image_1](./doc/figure_1.png)
[Image_2](./doc/figure_1-1.png)
[Image_3](./doc/figure_1-2.png)
[Image_4](./doc/figure_1-3.png)

#### Edit config.json accroding to subject
``` json
{
  "TEST_FILE": "bin/test.csv",
  "SUBJECT": {
    "MASS": 64,
    "HEIGHT": 1.7
  }
}
```

#### run this file for testing
```shell
python stick_model.py
```

#### run this file for kinematic model
```shell
python kin_testing.py
```

#### Directory structure

```shell
.
├── bin
│   ├── test.csv
│   └── traj.csv
├── FES
│   ├── fes.py
│   ├── __init__.py
│   └── Muscle.py
├── kin_testing.py
├── README.md
├── stick_model.py
├── utils
│   └── get_meta_data.py
└── walking_model
    ├── dynamics.py
    ├── __init__.py
    ├── Plotter.py
    ├── common.py
    └── Subject.py

```

#### walking_model description
- *Subject.py* is a model class with all attributes of the lower exoskeleton
- *Plotter.py* is a visualizer for the lower exoskeleton model
- *dynamics.py* is a helper module to calculate the dynamic model
- *common.py* has all the required helper functions