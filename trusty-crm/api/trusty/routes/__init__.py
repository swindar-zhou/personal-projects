from fastapi import APIRouter

from . import health, companies, contacts, applications, tasks

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"]) 
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
api_router.include_router(applications.router, prefix="/applications", tags=["applications"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
