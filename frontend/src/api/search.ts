import api from "./api";

export async function semanticSearch(
    repository: string,
    query: string,
    top_k: number = 5
) {

    const response = await api.post("/search/", {

        repository,
        query,
        top_k,

    });

    return response.data;
}