import { useState } from "react";

import { reviewRepository } from "../api/review";

import type { Review } from "../types/review";

function ReviewPage() {

    const [repository, setRepository] = useState("");

    const [review, setReview] = useState<Review | null>(null);

    const [loading, setLoading] = useState(false);

    async function generateReview() {

        if (!repository) return;

        setLoading(true);

        try {

            const data = await reviewRepository(repository);

            setReview(data);

        } catch (err) {

            console.error(err);

            alert("Review Failed");

        }

        setLoading(false);

    }

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">

                AI Review

            </h1>

            <div className="bg-white rounded-xl shadow p-6 mb-8">

                <input

                    className="border rounded w-full p-3"

                    placeholder="Repository"

                    value={repository}

                    onChange={(e)=>setRepository(e.target.value)}

                />

                <button

                    onClick={generateReview}

                    className="bg-blue-600 text-white px-6 py-2 rounded mt-4"

                >

                    {loading ? "Generating..." : "Generate Review"}

                </button>

            </div>

            {review && (

                <div className="space-y-6">

                    {/* Score */}

                    <div className="bg-white rounded-xl shadow p-6">

                        <h2 className="text-2xl font-bold">

                            Overall Score

                        </h2>

                        <p className="text-5xl mt-3 text-green-600">

                            {review.overall_score}/10

                        </p>

                    </div>

                    {/* Bugs */}

                    <Section
                        title="🐞 Bugs"
                        items={review.bugs}
                    />

                    {/* Security */}

                    <Section
                        title="🔒 Security Issues"
                        items={review.security_issues}
                    />

                    {/* Code Smells */}

                    <Section
                        title="🧹 Code Smells"
                        items={review.code_smells}
                    />

                    {/* Performance */}

                    <Section
                        title="⚡ Performance"
                        items={review.performance_suggestions}
                    />

                    {/* Best Practices */}

                    <Section
                        title="✅ Best Practices"
                        items={review.best_practices}
                    />

                </div>

            )}

        </div>

    );

}

interface Props {

    title: string;

    items: string[];

}

function Section({

    title,

    items

}: Props) {

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-bold mb-4">

                {title}

            </h2>

            <ul className="list-disc pl-6 space-y-2">

                {items.length === 0 ? (

                    <li>No issues found.</li>

                ) : (

                    items.map((item,index)=>(

                        <li key={index}>

                            {item}

                        </li>

                    ))

                )}

            </ul>

        </div>

    );

}

export default ReviewPage;