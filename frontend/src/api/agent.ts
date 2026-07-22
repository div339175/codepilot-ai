import api from "./api";

export async function askAgent(
    repository: string,
    currentFile: string | null,
    currentContent: string,
    message: string
) {

    const response = await api.post("/chat/agent", {
        repository,
        current_file: currentFile,
        current_content: currentContent,
        message,
    });

    return response.data;
}