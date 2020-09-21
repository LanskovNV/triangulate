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

to run program, just run python script with two params:

```bash
python main.py -i 'in.csv' -o 'out.csv'
```


# TODO:
## Options

`-g` - gui mode
`-i` - manual vertices input mode
`-h`, `--help` - print help message
