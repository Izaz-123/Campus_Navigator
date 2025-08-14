# navigator/utils.py
from collections import deque
import re

# ---- Campus graph ----
BLOCKS = [
    "Block 25", "Block 26", "Block 27", "Block 28", "Block 29", "Block 30",
    "Block 31", "Block 32", "Block 33", "Block 34", "Block 35", "Block 36",
    "Block 37", "Block 38"
]

GRAPH = {b: [] for b in BLOCKS}

def _add_undirected(a, b):
    GRAPH[a].append(b)
    GRAPH[b].append(a)

_add_undirected("Block 25", "Block 26")
_add_undirected("Block 26", "Block 27")
_add_undirected("Block 27", "Block 28")
_add_undirected("Block 28", "Block 29")
_add_undirected("Block 29", "Block 30")
_add_undirected("Block 30", "Block 31")
_add_undirected("Block 31", "Block 32")
_add_undirected("Block 32", "Block 33")
_add_undirected("Block 33", "Block 34")
_add_undirected("Block 35", "Block 36")
_add_undirected("Block 36", "Block 37")
_add_undirected("Block 37", "Block 38")
_add_undirected("Block 38", "Block 26")
_add_undirected("Block 35", "Block 33")

# ---- Helpers ----
def normalize_block(s: str) -> str | None:
    """Normalize input to 'Block XX' format."""
    if not s:
        return None
    s = s.strip()
    m = re.search(r'(\d+)$', s)
    if not m:
        return None
    num = m.group(1)
    candidate = f"Block {num}"
    return candidate if candidate in GRAPH else None

# ---- BFS shortest path ----
def shortest_path(start_raw: str, end_raw: str) -> list[str]:
    start = normalize_block(start_raw)
    end = normalize_block(end_raw)
    if not start or not end:
        return []

    visited = {node: False for node in GRAPH}
    parent = {}

    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        current = q.popleft()
        for neighbor in GRAPH[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                q.append(neighbor)

                if neighbor == end:  # Found destination
                    # Reconstruct path
                    path = []
                    step = end
                    while step != start:
                        path.append(step)
                        step = parent[step]
                    path.append(start)
                    path.reverse()
                    return path

    return []
