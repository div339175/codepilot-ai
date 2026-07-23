export type RepositoryStatus =
    | "Not Indexed"
    | "Indexing"
    | "Indexed"
    | "Analyzing"
    | "Ready"
    | "Failed";

export interface Repository {
    repository: string;

    status: RepositoryStatus;

    indexed: boolean;
    analyzed: boolean;

    generated_at: string | null;

    languages: string[];
    frameworks: string[];

    file_count: number;
    repository_size: string;

    analysis_ready: boolean;
}

export interface DashboardResponse {
    total_repositories: number;
    analyzed_repositories: number;
    total_languages: number;
    total_frameworks: number;
    repositories: Repository[];
}