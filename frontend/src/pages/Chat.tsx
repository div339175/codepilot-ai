import { useState } from "react";

import { askRepository } from "../api/chat";

import type { ChatResponse } from "../types/chat";

function Chat() {

    const [repository, setRepository] = useState("");

    const [question, setQuestion] = useState("");

    const [conversation, setConversation] = useState<ChatResponse[]>([]);

    const [loading, setLoading] = useState(false);

    async function sendMessage() {

        if (!repository || !question) return;

        setLoading(true);

        try {

            const response = await askRepository(
                repository,
                question
            );

            setConversation(prev => [
                ...prev,
                response
            ]);

            setQuestion("");

        } catch (err) {

            console.error(err);

            alert("Chat Failed");

        }

        setLoading(false);

    }

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">

                Repository Chat

            </h1>

            <div className="bg-white rounded-xl shadow p-6">

                <input

                    className="border rounded w-full p-3 mb-4"

                    placeholder="Repository"

                    value={repository}

                    onChange={(e)=>setRepository(e.target.value)}

                />

                <textarea

                    className="border rounded w-full p-3"

                    rows={4}

                    placeholder="Ask anything..."

                    value={question}

                    onChange={(e)=>setQuestion(e.target.value)}

                />

                <button

                    onClick={sendMessage}

                    className="bg-blue-600 text-white px-5 py-2 rounded mt-4"

                >

                    {loading ? "Thinking..." : "Send"}

                </button>

            </div>

            <div className="space-y-6 mt-8">

                {conversation.map((chat,index)=>(

                    <div

                        key={index}

                        className="bg-white rounded-xl shadow p-5"

                    >

                        <h2 className="font-bold">

                            ❓ {chat.question}

                        </h2>

                        <div className="mt-4 whitespace-pre-wrap">

                            🤖 {chat.answer}

                        </div>

                        {chat.sources && (

                            <div className="mt-5">

                                <h3 className="font-semibold">

                                    Sources

                                </h3>

                                <ul className="list-disc pl-6">

                                    {chat.sources.map((item,i)=>(

                                        <li key={i}>

                                            {item.file}

                                        </li>

                                    ))}

                                </ul>

                            </div>

                        )}

                    </div>

                ))}

            </div>

        </div>

    );

}

export default Chat;