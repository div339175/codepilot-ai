import api from "./api";

export async function getFile(
    repository: string,
    path: string
) {

    const response = await api.get(
        `/repositories/${repository}/file`,
        {
            params: {
                path
            }
        }
    );

    return response.data;

}