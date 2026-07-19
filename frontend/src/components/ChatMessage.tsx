import ReactMarkdown from "react-markdown";

interface Source {
    file: string;
    score: number;
}

interface Props {
    question: string;
    answer: string;
    sources?: Source[];
}

function ChatMessage({
    question,
    answer,
    sources,
}: Props) {
    return (
        <div className="space-y-6">

            {/* User */}

            <div className="flex justify-end">

                <div className="bg-blue-600 text-white rounded-xl p-4 max-w-2xl">

                    <h3 className="font-bold mb-2">
                        🙂 You
                    </h3>

                    {question}

                </div>

            </div>

            {/* AI */}

            <div className="flex justify-start">

                <div className="bg-white rounded-xl shadow p-5 max-w-3xl">

                    <h3 className="font-bold mb-4">
                        🤖 CodePilot AI
                    </h3>

                    <div className="prose max-w-none">

                        <ReactMarkdown>

                            {answer}

                        </ReactMarkdown>

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