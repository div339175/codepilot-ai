import { useState } from "react";
import { semanticSearch } from "../api/search";
import type { SearchResult } from "../types/search";
import RepositorySelector from "../components/RepositorySelector";
import toast from "react-hot-toast";
import { Oval } from "react-loader-spinner";
import { useSearchParams } from "react-router-dom";
import PageContainer from "../components/PageContainer";

function Search() {

    const [searchParams] = useSearchParams();

    const repositoryFromUrl = searchParams.get("repo");
    const [repository, setRepository] = useState(
        repositoryFromUrl ?? ""
    );

    const [query, setQuery] = useState("");

    const [results, setResults] = useState<SearchResult[]>([]);

    const [loading, setLoading] = useState(false);

    async function handleSearch() {

        if (!repository || !query) return;

        setLoading(true);

        try {

            const data = await semanticSearch(
                repository,
                query
            );

            setResults(data.results);
            toast.success("Search Complete");

        } catch (err) {

            console.error(err);

            toast.error("Search Failed");

        }

        setLoading(false);

    }

    return (

        <PageContainer title="Search">

            <div className="bg-white rounded-xl shadow p-6">

                <RepositorySelector
                    value={repository}
                    onChange={setRepository}
                />

                <input
                    className="border rounded w-full p-3"
                    placeholder="Search Query"
                    value={query}
                    onChange={(e)=>setQuery(e.target.value)}
                />

                <button
                    onClick={handleSearch}
                    disabled={loading}
                    className="bg-blue-600 text-white px-6 py-2 rounded mt-4 flex items-center gap-2 disabled:opacity-50"
                >
                    {loading && (
                        <Oval
                            height={18}
                            width={18}
                            strokeWidth={4}
                            visible={true}
                        />
                    )}

                    {loading ? "Searching..." : "Search"}
                </button>

            </div>

            <div className="space-y-6 mt-8">

                {results.map((item,index)=>(

                    <div
                        key={index}
                        className="bg-white rounded-xl shadow p-5"
                    >

                        <div className="flex justify-between">

                            <h2 className="font-bold">

                                📄 {item.file}

                            </h2>

                            <span>

                                Similarity : {item.score.toFixed(3)}

                            </span>

                        </div>

                        <p className="mt-2">

                            Language : {item.language}

                        </p>

                        <pre className="bg-gray-100 mt-4 p-4 rounded overflow-auto whitespace-pre-wrap">

{item.chunk}

                        </pre>

                    </div>

                ))}

            </div>

        </PageContainer>

    );

}

export default Search;