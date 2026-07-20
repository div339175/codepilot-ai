import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import PageContainer from "../components/PageContainer";

import {
    getRepositories,
    cloneRepository,
    deleteRepository,
    buildIndex,
    analyzeRepository,
    reviewRepository,
} from "../api/repository";

    function Repositories() {

        type Repository = {
            name: string;
            indexed: boolean;
        };

        const [repositories, setRepositories] = useState<Repository[]>([]);
        const [url, setUrl] = useState("");
        const [loading, setLoading] = useState(false);

    async function loadRepositories() {

        try {

            const data = await getRepositories();

            setRepositories(data.repositories);

        } catch (err) {
            console.error(err);
        }

    }

    useEffect(() => {
        loadRepositories();
    }, []);

    async function handleClone() {

        if (!url.trim()) return;

        setLoading(true);

        try {

            await cloneRepository(url);

            setUrl("");

            await loadRepositories();

        } catch (err) {

            console.error(err);

            toast.error("Clone Failed");

        }

        setLoading(false);

    }

    async function handleDelete(repository: string) {

        if (!confirm(`Delete ${repository}?`)) return;

        await deleteRepository(repository);

        loadRepositories();

    }

    async function handleIndex(repository: string) {

        try {

            await buildIndex(repository);
            await loadRepositories();
           toast.success("Index Built Successfully");

        } catch (err) {

            console.error(err);

            toast.error("Index Failed");

        }

    }

    async function handleAnalysis(repository: string) {

        try {

            await analyzeRepository(repository);

            toast.success("Analysis Completed");

        } catch (err) {

            console.error(err);

            toast.error("Analysis Failed");

        }

    }

    async function handleReview(repository: string) {

        try {

            await reviewRepository(repository);

            toast.success("Review Generated");

        } catch (err) {

            console.error(err);

            alert("Review Failed");

        }

    }

    return (

        <PageContainer title="Repositories">

            <div className="bg-white rounded-xl shadow p-6 mb-8">

                <input

                    className="border rounded-lg w-full p-3"

                    placeholder="GitHub Repository URL"

                    value={url}

                    onChange={(e) => setUrl(e.target.value)}

                />

                <button

                    onClick={handleClone}

                    disabled={loading}

                    className="mt-4 bg-blue-600 text-white px-5 py-2 rounded"

                >
                    

                    {loading ? "Cloning..." : "Clone Repository"}

                </button>

            </div>

            <div className="space-y-5">

                {repositories.map((repo) => (

                    <div

                        key={repo.name}

                        className="bg-white rounded-xl shadow p-6"

                    >

                        <h2 className="text-xl font-bold">
                            📁 {repo.name}
                        </h2>

                        <p
                            className={
                                repo.indexed
                                    ? "text-green-600 font-semibold mt-2"
                                    : "text-red-600 font-semibold mt-2"
                            }
                        >
                            {repo.indexed
                                ? "✅ Index Ready"
                                : "❌ Index Not Built"}
                        </p>

                        <div className="flex gap-3 mt-5 flex-wrap">

                            <button

                                onClick={() => handleIndex(repo.name)}

                                className="bg-green-600 text-white px-4 py-2 rounded"

                            >

                                Build Index

                            </button>

                            <button
                                disabled={!repo.indexed}
                                title={!repo.indexed ? "Build the index first" : ""}
                                onClick={() => handleAnalysis(repo.name)}
                                className={`px-4 py-2 rounded text-white ${
                                    repo.indexed
                                        ? "bg-blue-600 hover:bg-blue-700"
                                        : "bg-gray-400 cursor-not-allowed"
                                }`}
                            >
                                Analyze
                            </button>

                            <button
                                disabled={!repo.indexed}
                                title={!repo.indexed ? "Build the index first" : ""}
                                onClick={() => handleReview(repo.name)}
                                className={`px-4 py-2 rounded text-white ${
                                    repo.indexed
                                        ? "bg-purple-600 hover:bg-purple-700"
                                        : "bg-gray-400 cursor-not-allowed"
                                }`}
                            >
                                Review
                            </button>

                            <button
                                disabled={!repo.indexed}
                                title={!repo.indexed ? "Build the index first" : ""}
                                className={`px-4 py-2 rounded text-white ${
                                    repo.indexed
                                        ? "bg-orange-600 hover:bg-orange-700"
                                        : "bg-gray-400 cursor-not-allowed"
                                }`}
                            >
                                Chat
                            </button>

                            <button

                                onClick={() => handleDelete(repo.name)}

                                className="bg-red-600 text-white px-4 py-2 rounded"

                            >

                                Delete

                            </button>

                        </div>

                    </div>

                ))}

            </div>

        </PageContainer>

    );

}

export default Repositories;