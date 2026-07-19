import { useEffect, useState } from "react";
import { getDashboard } from "../api/dashboard";
import type { DashboardResponse} from "../types/dashboard";

function Dashboard() {
  const [dashboard, setDashboard] = useState<DashboardResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const data = await getDashboard();
        setDashboard(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (!dashboard) {
    return <h2>Failed to load dashboard.</h2>;
  }

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">
        Dashboard
      </h1>

      <div className="grid grid-cols-3 gap-6 mb-8">

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Repositories</h2>
          <p className="text-4xl font-bold">
            {dashboard.total_repositories}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Languages</h2>
          <p className="text-4xl font-bold">
            {dashboard.total_languages}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Frameworks</h2>
          <p className="text-4xl font-bold">
            {dashboard.total_frameworks}
          </p>
        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-xl font-semibold mb-4">
          Repositories
        </h2>

        {dashboard.repositories.map((repo) => (

          <div
            key={repo.repository}
            className="border rounded-lg p-4 mb-4"
          >
            <h3 className="font-bold">
              {repo.repository}
            </h3>

            <p>
              Languages: {repo.languages.join(", ")}
            </p>

            <p>
              Frameworks: {repo.frameworks.join(", ")}
            </p>

          </div>

        ))}

      </div>
    </div>
  );
}

export default Dashboard;