# triangulate
2d polygons triangulation with earcut algorithm

## Input

csv file with polygon vertices coords ("x" first, "y" second):
```csv
1, 2
3, 19
5, 8
94, 3
```

## Output

 1. If success, csv with triangulation:

 ```csv
 1, 2, 3
 2, 3, 4
 ```

 2. If fault, csv file with error only:
 ```csv
 ERROR: Incorrect input data
 ```

## How to use

At first, do the following:
1. clone repo
2. move to project root folder
3. execute following commands:
```bash
python -m venv env  # setup new virtualenv
source env/bin/activate  # activate new virtualenv
pip install -r requirements.txt  # install all project requirements
```

4. to run program, just run python script with two params:

```bash
python main.py -i 'in.csv' -o 'out.csv'
```


# TODO:
## Options

`-g` - gui mode
