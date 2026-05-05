import os
from pathlib import Path

class WorkspaceManager:
    """Mengelola isolasi direktori kerja untuk setiap klien MAIO."""
    
    BASE_DIR = Path("workspaces")
    
    @classmethod
    def get_client_path(cls, client_id: str, subpath: str = "") -> Path:
        """Mendapatkan path direktori untuk klien tertentu."""
        path = cls.BASE_DIR / client_id.lower().replace(" ", "_")
        if subpath:
            path = path / subpath
            
        # Pastikan direktori ada
        path.mkdir(parents=True, exist_ok=True)
        return path

    @classmethod
    def get_specialist_path(cls, client_id: str, vp_name: str, specialist_name: str) -> Path:
        """Mendapatkan path spesifik untuk spesialis di bawah VP tertentu."""
        subpath = f"{vp_name}/{specialist_name}"
        return cls.get_client_path(client_id, subpath)
