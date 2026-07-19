import api from "./api";

export async function askRepository(
    repository: string,
    question: string
) {

    const response = await api.post("/chat/", {

        
        repository,
        question,

    });

    return response.data;

}