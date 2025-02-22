1.Create env
```bash
conda create -p myenv python -y
```

2.activate env
```bash
conda activate (path to myenv)
```

3.Create Requirements.txt

4.Install requirements.txt
```bash
pip install -r requirements.txt
```

5.Initilize git
```bash
git init
```

6.Initilize DVC
```bash
dvc init
```

7.Add data to DVC
```bash
dvc add data_given/winequality.csv
```

8.
```bash
git add . && git commit -m "first commit"
git push origin main
```

9.Tox
```bash
tox
tox -r  #for rebuilding use this else only tox
```

10.pytest
```bash
pytest -v
```

11.setup command
```bash
pip install -e .
```

12.build your own package
```bash
python setup.py sdist bdist_wheel
```
