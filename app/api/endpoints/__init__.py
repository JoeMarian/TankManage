from .auth import router as auth_router
from .users import router as users_router
from .dashboards import router as dashboards_router
from .data import router as data_router

__all__ = ['auth_router', 'users_router', 'dashboards_router', 'data_router']
