export interface Source {

    file: string;

    score: number;

}

export interface ChatResponse {

    repository: string;

    question: string;

    answer: string;

    sources?: Source[];

    timestamp?: string;

}