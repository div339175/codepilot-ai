import { useEffect, useState } from "react";

import {
    getRepositories,
    cloneRepository,
    deleteRepository,
    buildIndex,
    analyzeRepository,
    reviewRepository,
} from "../api/repository";

function Repositories() {

    const [repositories, setRepositories] = useState<string[]>([]);
    const [url, setUrl] = useState("");
    const [loading, setLoading] = useState(false);

    async function loadRepositories() {

        try {

            const data = await getRepositories();

            // 🔄 UPDATE THIS IF YOUR BACKEND RETURNS A DIFFERENT SHAPE
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

            alert("Clone failed.");

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

            alert("Index Built Successfully");

        } catch (err) {

            console.error(err);

            alert("Index Failed");

        }

    }

    async function handleAnalysis(repository: string) {

        try {

            await analyzeRepository(repository);

            alert("Analysis Completed");

        } catch (err) {

            console.error(err);

            alert("Analysis Failed");

        }

    }

    async function handleReview(repository: string) {

        try {

            await reviewRepository(repository);

            alert("Review Generated");

        } catch (err) {

            console.error(err);

            alert("Review Failed");

        }

    }

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">

                Repositories

            </h1>

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

                        key={repo}

                        className="bg-white rounded-xl shadow p-6"

                    >

                        <h2 className="text-xl font-bold">

                            📁 {repo}

                        </h2>

                        <div className="flex gap-3 mt-5 flex-wrap">

                            <button

                                onClick={() => handleIndex(repo)}

                                className="bg-green-600 text-white px-4 py-2 rounded"

                            >

                                Build Index

                            </button>

                            <button

                                onClick={() => handleAnalysis(repo)}

                                className="bg-blue-600 text-white px-4 py-2 rounded"

                            >

                                Analyze

                            </button>

                            <button

                                onClick={() => handleReview(repo)}

                                className="bg-purple-600 text-white px-4 py-2 rounded"

                            >

                                Review

                            </button>

                            {/* 🚀 We'll connect this in the next milestone */}

                            <button

                                className="bg-orange-600 text-white px-4 py-2 rounded"

                            >

                                Chat

                            </button>

                            <button

                                onClick={() => handleDelete(repo)}

                                className="bg-red-600 text-white px-4 py-2 rounded"

                            >

                                Delete

                            </button>

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default Repositories;