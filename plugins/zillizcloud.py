import milvus
from milvus import Milvus, connections, Collection
from typing import List, Dict, Any

class ZillizRetrievalAgent:
    def __init__(self, host: str, port: str, collection_name: str):
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self.collection = None
        self.connect()

    def connect(self):
        connections.connect("default", host=self.host, port=self.port)
        self.collection = Collection(name=self.collection_name)

    def search(self, vectors: List[List[float]], top_k: int, params: Dict[str, Any]):
        """
        Search the Milvus collection for similar vectors.
        Args:
            vectors (List[List[float]]): The query vectors.
            top_k (int): Number of top similar results to retrieve.
            params (Dict[str, Any]): Additional search parameters.
        Returns:
            List of search results.
        """
        search_params = {
            "metric_type": "L2",
            "params": params
        }
        results = self.collection.search(vectors, "embedding", search_params, top_k)
        return results
