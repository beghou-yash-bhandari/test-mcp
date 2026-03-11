from fastmcp import FastMCP
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

load_dotenv()

mcp = FastMCP(name = "Notes App")

@mcp.tool()
def get_my_notes() -> str:
    """Get all notes for a user"""
    return "no notes yet"

@mcp.tool()
def add_note(content: str) -> str:
    """Add a note for a user"""
    return f"Added note: {content}"

if __name__ == "__main__":
    mcp.run(
        transport = "http", #stdio.h or sse
        host = "127.0.0.1",
        port = 8000,
        middleware = [
            Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)
        ]
    )