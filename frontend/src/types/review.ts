export interface Review {

    repository: string;

    overall_score: number;

    bugs: string[];

    security_issues: string[];

    code_smells: string[];

    performance_suggestions: string[];

    best_practices: string[];

}