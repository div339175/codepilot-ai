import api from "./api";

export interface TreeNode {
    name: string;
    path: string;
    type: "file" | "folder";
    children?: TreeNode[];
}

export async function getRepositoryTree(repository: string) {
    const response = await api.get(`/repositories/${repository}/tree`);
    return response.data;
}