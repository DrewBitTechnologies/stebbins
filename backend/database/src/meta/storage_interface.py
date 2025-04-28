import os

class FileStorageInterface:
    def save_file(self, file_data, file_path):
        """Save file data to the specified path"""
        pass
    
    def get_file_url(self, file_path):
        """Get URL for accessing the file"""
        pass
    
    def get_file_bytes(self, file_path):
        """Get raw bytes of the file"""
        pass
    
    def delete_file(self, file_path):
        """Delete the file at specified path"""
        pass

class LocalFileStorage(FileStorageInterface):
    def __init__(self, base_dir="/app/app_data/images"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
    
    def save_file(self, file_data, file_path):
        full_path = os.path.join(self.base_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(file_data)
        return file_path
    
    def get_file_url(self, file_path):
        # Return a URL that your FastAPI app can serve
        return f"/images/{file_path}"
    
    def get_file_bytes(self, file_path):
        full_path = os.path.join(self.base_dir, file_path)
        with open(full_path, "rb") as f:
            return f.read()
    
    def delete_file(self, file_path):
        full_path = os.path.join(self.base_dir, file_path)
        if os.path.exists(full_path):
            os.remove(full_path)