import type { Repository } from "../types/dashboard";
import { useNavigate } from "react-router-dom";


interface Props {
    repository: Repository;
}

function RepositoryCard({ repository }: Props) {
    const navigate = useNavigate();
    return (
        <div className="bg-white rounded-2xl shadow p-6">

            <div className="flex justify-between items-start">

                <div>

                    <h2 className="text-xl font-bold">

                        📁 {repository.repository}

                    </h2>

                    <p className="text-gray-500 mt-2">

                        Generated:{" "}
                        {repository.generated_at
                            ? new Date(repository.generated_at).toLocaleString()
                            : "Not Available"}

                    </p>

                </div>

                <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">

                    Ready

                </span>

            </div>

            {/* Languages */}

            <div className="mt-4">

                <h4 className="font-semibold mb-2">

                    Languages

                </h4>

                {repository.languages.length > 0 ? (

                    <div className="flex flex-wrap gap-2">

                        {repository.languages.map((language) => (

                            <span
                                key={language}
                                className="bg-blue-100 text-blue-700 px-2 py-1 rounded-full text-sm"
                            >
                                {language}
                            </span>

                        ))}

                    </div>

                ) : (

                    <p className="text-gray-500 text-sm">

                        No languages detected

                    </p>

                )}

            </div>

            {/* Frameworks */}

            <div className="mt-4">

                <h4 className="font-semibold mb-2">

                    Frameworks

                </h4>

                {repository.frameworks.length > 0 ? (

                    <div className="flex flex-wrap gap-2">

                        {repository.frameworks.map((framework) => (

                            <span
                                key={framework}
                                className="bg-purple-100 text-purple-700 px-2 py-1 rounded-full text-sm"
                            >
                                {framework}
                            </span>

                        ))}

                    </div>

                ) : (

                    <p className="text-gray-500 text-sm">

                        No frameworks detected

                    </p>

                )}

            </div>

            {/* Quick Stats */}

            <div className="grid grid-cols-3 gap-4 mt-6">

                <div className="bg-gray-50 rounded-lg p-3">

                    <p className="text-sm text-gray-500">

                        📄 Files

                    </p>

                    <p className="font-bold text-lg">

                        {repository.file_count}

                    </p>

                </div>

                <div className="bg-gray-50 rounded-lg p-3">

                    <p className="text-sm text-gray-500">

                        📦 Size

                    </p>

                    <p className="font-bold text-lg">

                        {repository.repository_size}

                    </p>

                </div>

                <div className="bg-gray-50 rounded-lg p-3">

                    <p className="text-sm text-gray-500">

                        🤖 AI Status

                    </p>

                    <p
                        className={`font-bold text-lg ${
                            repository.analysis_ready
                                ? "text-green-600"
                                : "text-yellow-600"
                        }`}
                    >

                        {repository.analysis_ready ? "Ready" : "Pending"}

                    </p>

                </div>

            </div>

            {/* Actions */}

            <div className="flex gap-3 mt-6">

                <button
                    onClick={() =>
                        navigate(`/search?repo=${repository.repository}`)
                    }
                    className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                >
                    Search
                </button>

                <button
                    onClick={() =>
                        navigate(`/chat?repo=${repository.repository}`)
                    }
                    className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
                >
                    Chat
                </button>

                <button
                    onClick={() =>
                        navigate(`/review?repo=${repository.repository}`)
                    }
                    className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700"
                >
                    Review
                </button>

            </div>

        </div>
    );
}

export default RepositoryCard;