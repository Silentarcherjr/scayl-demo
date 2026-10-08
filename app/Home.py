from deploy.space import hosted_frame
hosted_frame()
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[0] / '_protected/Home.py'), run_name='__main__')
