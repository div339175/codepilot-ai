import api from "./api";

export async function getDashboard() {
  const response = await api.get("/dashboard/overview");
  console.log(response);
  return response.data;
}