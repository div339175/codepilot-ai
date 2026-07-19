import api from "./api";

export async function reviewRepository(
    repository: string
) {

    const response = await api.post("/review/", {

        repository,

    });

    return response.data;

}