from app.core.search import semantic_search
from app.core.repository_registry import RepositoryRegistry


class MultiRepositoryService:

    def __init__(self):

        self.registry = RepositoryRegistry()

    def search_all(
        self,
        query: str,
        top_k: int = 5
    ):

        repositories = self.registry.list_repositories()

        all_results = []

        for repository in repositories:

            print(f"\nSearching repository: {repository}")

            try:

                results = semantic_search(
                    repository=repository,
                    query=query,
                    top_k=top_k
                )
                print(f"Found {len(results)} results")
                all_results.extend(results)

            except Exception as e:
                print(f"Error in {repository}: {e}")

        all_results.sort(
            key=lambda x: x["score"]
        )

        return all_results[:top_k]