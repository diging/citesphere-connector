CITESPHERE_API_URL = "https://diging-dev.asu.edu/citesphere-review/api"
MAX_SIZE = 50

def get_file(file_id:str)-> str:
    return f"https://diging.asu.edu/geco-giles-staging/api/v2/resources/files/{file_id}/content"