import MarkdownRenderer from "./MarkdownRenderer";

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

                <div className="bg-blue-600 text-white rounded-xl p-4 max-w-2xl">

                    <h3 className="font-bold mb-2">
                        🙂 You
                    </h3>
                    <p className="text-xs opacity-70 mt-1">

                    {timestamp}

                    </p>

                    {question}

                </div>

            </div>

            {/* AI */}

            <div className="flex justify-start">

                <div className="bg-white rounded-xl shadow p-5 max-w-3xl">

                    <h3 className="font-bold mb-4">
                        🤖 CodePilot AI
                    </h3>
                    <p className="text-xs opacity-70 mt-1">

                        {timestamp}

                    </p>

                    <div className="prose max-w-none">

                        <MarkdownRenderer
                            content={answer}
                        />

                    </div>

                    {sources && sources.length > 0 && (

                        <>

                            <hr className="my-4"/>

                            <h4 className="font-semibold">

                                📂 Sources

                            </h4>

                            <ul className="list-disc pl-6 mt-2">

                                {sources.map((item,index)=>(

                                    <li key={index}>

                                        {item.file}

                                    </li>

                                ))}

                            </ul>

                        </>

                    )}

                </div>

            </div>

        </div>
    );
}

export default ChatMessage;