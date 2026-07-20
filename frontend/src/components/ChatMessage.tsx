import MarkdownRenderer from "./MarkdownRenderer";
import toast from "react-hot-toast";

interface Source {
    file: string;
    score: number;
}

interface Props {
    question: string;
    answer: string;
    sources?: Source[];
    timestamp?: string;
}

function copyAnswer(text: string) {
    navigator.clipboard.writeText(text);
    toast.success("Answer copied");
}

function ChatMessage({
    question,
    answer,
    sources,
    timestamp,
}: Props) {
    return (
        <div className="space-y-6">

            {/* User */}

                <div className="flex justify-end">

                    <div className="bg-blue-600 text-white rounded-2xl p-5 max-w-xl">

                        <div className="flex justify-between items-center mb-3">

                            <h3 className="font-bold">

                                🙂 You

                            </h3>

                            <span className="text-xs opacity-70">

                                {timestamp}

                            </span>

                        </div>

                        <p>

                            {question}

                        </p>

                    </div>

                </div>

        {/* AI */}

            <div className="flex justify-start">

                <div className="bg-white rounded-2xl shadow-lg p-6 max-w-4xl w-full">

                    {/* Header */}

                    <div className="flex justify-between items-start mb-5">

                        <div className="flex items-center gap-3">

                            <div className="w-10 h-10 rounded-full bg-green-600 flex items-center justify-center text-white">

                                🤖

                            </div>

                            <div>

                                <h3 className="font-bold text-lg">

                                    CodePilot AI

                                </h3>

                                <p className="text-sm text-gray-500">

                                    AI Repository Assistant

                                </p>

                                <p className="text-xs text-gray-400">

                                    {timestamp}

                                </p>

                            </div>

                        </div>

                        <button
                            onClick={() => copyAnswer(answer)}
                            className="px-3 py-2 text-sm rounded-lg bg-gray-100 hover:bg-gray-200 transition"
                        >
                            📋 Copy Answer
                        </button>

                    </div>

                    {/* AI Answer */}

                    <div className="
                        prose
                        max-w-none
                        prose-headings:font-bold
                        prose-h1:text-3xl
                        prose-h2:text-2xl
                        prose-h3:text-xl
                        prose-p:text-gray-700
                        prose-li:text-gray-700
                    ">

                        <MarkdownRenderer content={answer} />

                    </div>

                    {/* Sources */}

                    {sources && sources.length > 0 && (

                        <div className="mt-8">

                            <hr className="mb-5" />

                            <h4 className="font-bold text-lg mb-4">

                                📂 Sources

                            </h4>

                            <div className="space-y-3">

                                {sources.map((item, index) => (

                                    <div
                                        key={index}
                                        className="border rounded-xl p-4 hover:bg-gray-50 transition"
                                    >

                                        <div className="font-medium">

                                            📄 {item.file}

                                        </div>

                                        <div className="text-sm text-gray-500 mt-1">

                                            Similarity Score: {item.score.toFixed(2)}

                                        </div>

                                    </div>

                                ))}

                            </div>

                        </div>

                    )}

                </div>

            </div>
        </div>
    );
}

export default ChatMessage;