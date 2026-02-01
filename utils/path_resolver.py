from pathlib import Path

def root_path()-> Path:
    """
    root_path is designemed to get the root dirrectory path from the system 
    :return: path object 
    :rtype: Path
    """
    path=Path(__file__).resolve().parents[1]
    return(path)


def resolve_path(relative_path:str)-> Path:
    """
    
    resolve_path is desigened to append the relative path with root path so to get exact location of the path 
    
    :param relative_path: accespts the releative file path to appaned it with rood dir path 
    :type relative_path: str
    :return: Path object
    :rtype: Path
    
    """
    return root_path() / relative_path
