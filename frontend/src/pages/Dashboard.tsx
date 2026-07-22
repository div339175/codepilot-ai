import { useEffect, useState } from "react";
import { getDashboard } from "../api/dashboard";
import type { DashboardResponse } from "../types/dashboard";
import PageContainer from "../components/PageContainer";

import {
    FaFolder,
    FaSearch,
    FaRobot,
    FaComments,
} from "react-icons/fa";

import StatCard from "../components/StatCard";
import RepositoryCard from "../components/RepositoryCard";

function Dashboard() {

    const [dashboard, setDashboard] = useState<DashboardResponse | null>(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function loadDashboard() {

            try {

                const data = await getDashboard();
                console.log("Dashboard Response:", data);
                console.log("Repositories:", data.repositories);
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

        <PageContainer title="Dashboard">

            {/* Statistics */}

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

                <StatCard
                    title="Repositories"
                    value={dashboard.total_repositories}
                    icon={FaFolder}
                />

                <StatCard
                    title="Languages"
                    value={dashboard.total_languages}
                    icon={FaSearch}
                />

                <StatCard
                    title="Frameworks"
                    value={dashboard.total_frameworks}
                    icon={FaRobot}
                />

                <StatCard
                    title="Analyzed"
                    value={dashboard.analyzed_repositories}
                    icon={FaComments}
                />

            </div>

            {/* Repository Overview */}

            <div className="mt-10">

                <h2 className="text-2xl font-bold mb-5">

                    Repository Overview

                </h2>

                <div className="space-y-5">

                    {dashboard.repositories.map((repo) => (

                        <RepositoryCard
                            key={repo.repository}
                            repository={repo}
                        />

                    ))}

                </div>

            </div>

        </PageContainer>

    );

}

export default Dashboard;