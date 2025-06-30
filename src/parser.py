from mcp.server.fastmcp import FastMCP
import re
from datetime import datetime

mcp = FastMCP(name="Parser", stateless_http=True)

def parse_log_line(line):
    match = re.match(
        r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (\d{3}) (/[^ ]+) (.+)", line
    )
    if not match:
        return None
    date_str, time_str, level, status, url, message = match.groups()
    timestamp = f"{date_str}T{time_str}"
    return {
        "timestamp": timestamp,
        "level": level,
        "status": int(status),
        "url": url,
        "message": message
    }


@mcp.tool(description="A simple parser tool")
def parse_logs(log_text: str) -> list[dict]:
    """
    Parse a text containing log lines into a list of dictionaries.

    Args:
        log_text (str): The text containing log lines.

    Returns:
        list[dict]: A list of dictionaries, each containing the parsed log line data.
    """
    lines = log_text.strip().splitlines()
    parsed = [parse_log_line(line) for line in lines]
    return [entry for entry in parsed if entry]