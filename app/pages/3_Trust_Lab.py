from deploy.space import hosted_frame
hosted_frame()
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[1] / '_protected/pages/3_Trust_Lab.py'), run_name='__main__')
