import sys
import os
import mlrun

from mlrun.serving.v2_serving import V2ModelServer

from mlrun.serving.routers import ParallelRun, ExecutorTypes

from mlrun.serving.utils import _extract_input_data, _update_result_body

from mlrun.execution import MLClientCtx

from mlrun import new_function, auto_mount, code_to_function, get_or_create_project

 

# src_path = os.path.join(os.getcwd(), 'src')
# print(src_path)
# sys.path.append(src_path)



def echo(event):
    return 1

