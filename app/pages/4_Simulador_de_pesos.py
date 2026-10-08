from deploy.space import hosted_frame
hosted_frame()
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[1] / '_protected/pages/4_Simulador_de_pesos.py'), run_name='__main__')
