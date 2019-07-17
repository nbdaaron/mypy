from typing import Generic, TypeVar

_T = TypeVar('_T')

class AsyncTask(Generic[_T]):
    def value(self) -> _T: ...