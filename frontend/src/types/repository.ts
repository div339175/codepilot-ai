export type RepositoryStatus =
    | "Not Indexed"
    | "Indexed"
    | "Indexing"
    | "Analyzing"
    | "Ready"
    | "Failed";

export interface Repository {
    name: string;
    indexed: boolean;
    status: RepositoryStatus;
}