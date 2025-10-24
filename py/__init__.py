import functools

from .hook import pre_execute, pre_get_input_data
import execution


# refer. https://stackoverflow.com/a/35758398
def prefix_function(function, prefunction):
    @functools.wraps(function)
    def run(*args, **kwargs):
        prefunction(*args, **kwargs)
        return function(*args, **kwargs)

    return run


execution.PromptExecutor.execute = prefix_function(
    execution.PromptExecutor.execute, pre_execute
)


execution.get_input_data = prefix_function(execution.get_input_data, pre_get_input_data)


def get_output_cache_wrapper(self, input_unique_id, unique_id):
    return self.output_cache.get(input_unique_id)

from comfy_execution.graph import ExecutionList
ExecutionList.get_output_cache = get_output_cache_wrapper


# --- Compatibility shims for ComfyUI cache objects ---
# Make HierarchicalCache/LRUCache/NullCache expose get_output_cache(...) expected by execution.get_input_data(...)
from comfy_execution.caching import HierarchicalCache, LRUCache, NullCache

def _cache_get_output_cache(self, input_unique_id, unique_id):
    # unique_id is ignored here; we only need cached outputs of input_unique_id
    try:
        return self.get(input_unique_id)
    except Exception:
        return None

def _nullcache_get_output_cache(self, input_unique_id, unique_id):
    return None

if not hasattr(HierarchicalCache, "get_output_cache"):
    HierarchicalCache.get_output_cache = _cache_get_output_cache
if not hasattr(LRUCache, "get_output_cache"):
    LRUCache.get_output_cache = _cache_get_output_cache
if not hasattr(NullCache, "get_output_cache"):
    NullCache.get_output_cache = _nullcache_get_output_cache
