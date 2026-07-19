export interface SearchResult {
    repository: string;
    score: number;
    file: string;
    language: string;
    chunk: string;
}

export interface SearchResponse {
    repository: string;
    query: string;
    results: SearchResult[];
}