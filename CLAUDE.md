# Project: IF0100-POO-II

## Commands
- Build: `[fill in]`
- Test: `pytest`
- Lint: `ruff check .`
- Dev: `uvicorn app.main:app --reload`

## Stack
Python / FastAPI

## Entry Points
- [fill in your entry points]

## Optimization Rules
- Use Pydantic v2 models for all request/response schemas
- Use async def for IO-bound routes, def for CPU-bound
- Use dependency injection for database sessions and auth
- Use Alembic for all schema migrations — never raw SQL DDL
- Add OpenAPI tags and descriptions to all endpoints
- Use HTTPException with proper status codes — never return raw dicts

## Key Decisions
- [fill in: Why X not Y → reason]

## Things That Look Wrong But Aren't
- [fill in: file/pattern → why it's intentional]

## Conventions
- [fill in your naming convention]
- [fill in your file organization rule]

## Workflow
- New feature → /plan first, then /smart-edit to implement
- Bug fix → /debug-error or /fix-issue [number]
- Before editing unfamiliar code → /explore-area [dir]
- After all changes → /review then /commit
- Ready to merge → /create-pr
- New developer → /onboard
