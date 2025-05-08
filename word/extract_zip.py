import zipfile

with zipfile.ZipFile("moviedata.zip") as moviedatazip:
    for each_filename in moviedatazip.namelist():
        if not each_filename.startswith('Links/'):
            moviedatazip.getinfo(each_filename).filename = 'moviedata.csv'
            moviedatazip.extract(each_filename, '../data', '.')