import api from "./api";
import type { Repository } from "../types/repository";

interface RepositoryListResponse {
    repositories: Repository[];
}

export async function getRepositories(): Promise<RepositoryListResponse> {
    const response = await api.get("/repositories/");
    return response.data;
}

export async function cloneRepository(repoUrl: string) {
    const response = await api.post("/clone", {
        repo_url: repoUrl,
    });

    return response.data;
}

export async function deleteRepository(repository: string) {
  const response = await api.delete(`/repositories/${repository}`);
  return response.data;
}

export async function buildIndex(repository: string) {
    const response = await api.post("/index/", {

        repository,

    });

    return response.data;
}

export async function analyzeRepository(repository: string) {
    const response = await api.post("/analysis/cache/", {

        repository,

    });

    return response.data;
}

export async function reviewRepository(repository: string) {
    const response = await api.post("/review/", {

        repository,

    });

    return response.data;
}