from typing import Any, Callable, Generic, TypeVar
from .async_task import AsyncTask

_CT = TypeVar('_CT', bound=Callable[..., Any])
_T = TypeVar('_T')
_ReturnT = TypeVar('_ReturnT')

class _AsyncDecoratorFunction(Generic[_ReturnT]):
    def __call__(self, *args: Any, **kwargs: Any) -> _ReturnT: ...
    def asynq(self, *args: Any, **kwargs: Any) -> AsyncTask[_ReturnT]: ...

class _AsyncDecoratorBinder:
    def __call__(self, fn: Callable[..., _ReturnT]) -> _AsyncDecoratorFunction[_ReturnT]: ...

def asynq(*args: Any) -> _AsyncDecoratorBinder: ...
