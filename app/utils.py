import time
from functools import wraps
import yaml



def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper



def get_yaml(filename):
    with open(filename, "r") as stream:
        try:
            conf_file = yaml.safe_load(stream)
            EXTENSIONS = conf_file.get("extensions")
            CHAT_IDS = conf_file.get("chat_ids")
            return EXTENSIONS, CHAT_IDS
        except yaml.YAMLError as exc:
            print(exc)