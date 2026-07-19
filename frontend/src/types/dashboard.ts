export interface Repository {
  repository: string;
  generated_at: string | null;
  languages: string[];
  frameworks: string[];
  summary_length: number;
  architecture_length: number;
}

export interface DashboardResponse {
  total_repositories: number;
  analyzed_repositories: number;
  total_languages: number;
  total_frameworks: number;
  repositories: Repository[];
}