import glob
import shutil

files = glob.glob('/Users/kyanchen/codes/levir-lab/_site/*/*/*')
files = files + glob.glob('/Users/kyanchen/codes/levir-lab/_site/*/*')
files = files + glob.glob('/Users/kyanchen/codes/levir-lab/_site/*')
for file in files:
    if file.endswith('.html'):
        shutil.move(file, file.replace('.html', '.jsp'))
