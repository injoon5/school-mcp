#!/usr/bin/env python3
import os
from fastmcp import FastMCP
import httpx

mcp = FastMCP("School API Server")
BASE_URL = "https://school-api-1i8w.onrender.com"


@mcp.tool
def search_school(school_name: str) -> list:
    """Search for a school by its name."""
    response = httpx.get(f"{BASE_URL}/school", params={"schoolname": school_name})
    response.raise_for_status()
    return response.json()


@mcp.tool
def get_classes(grade: int, school_code: str) -> list:
    """Get the list of classes for a specific grade in a school."""
    params = {"grade": grade, "schoolcode": school_code}
    response = httpx.get(f"{BASE_URL}/classes", params=params)
    response.raise_for_status()
    return response.json()


@mcp.tool
def get_timetable(grade: int, class_number: int, week: int, school_code: str) -> dict:
    """
    Get the timetable for a specific grade and class for a given week.
    'week' parameter should be 0 for the current week and 1 for the next week.
    """
    params = {
        "grade": grade,
        "classno": class_number,
        "week": week,
        "schoolcode": school_code,
    }
    response = httpx.get(f"{BASE_URL}/timetable", params=params)
    response.raise_for_status()
    return response.json()


@mcp.tool
def get_lunch_menu(start_date: str, end_date: str, school_code: str) -> list:
    """
    Get the lunch menu for a school for a given date range.
    Dates should be in 'YYYYMMDD' format.
    """
    params = {
        "startdate": start_date,
        "enddate": end_date,
        "schoolcode": school_code,
    }
    response = httpx.get(f"{BASE_URL}/lunch", params=params)
    response.raise_for_status()
    return response.json()


@mcp.tool
def get_school_events(start_date: str, end_date: str, school_code: str) -> list:
    """
    Get the school events for a given date range.
    Dates should be in 'YYYYMMDD' format.
    """
    params = {
        "startdate": start_date,
        "enddate": end_date,
        "schoolcode": school_code,
    }
    response = httpx.get(f"{BASE_URL}/schedule", params=params)
    response.raise_for_status()
    return response.json()


@mcp.tool
def get_server_info() -> dict:
    """
    Get information about the MCP server including name, version, environment,
    and Python version.
    """
    return {
        "server_name": "School API Server",
        "version": "1.0.0",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "python_version": os.sys.version.split()[0],
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"

    print(f"Starting FastMCP server on {host}:{port}")

    mcp.run(transport="http", host=host, port=port, stateless_http=True)
