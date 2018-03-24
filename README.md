## This is a README

run this file for testing
```
	python stick_model.py
```

run this file for kinematic model
```
	python kin_testing.py
```

Directory structure

```
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
    └── Subject.py

```

walking_model description
- Subject.py is a model class with all attributes of the lower exoskeleton
- Plotter.py is a visualizer for the lower exoskeleton model
- dynamics.py is a helper module to calculate the dynamic model