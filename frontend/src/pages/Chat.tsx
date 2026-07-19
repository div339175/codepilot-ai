import { useState } from "react";
import { Oval } from "react-loader-spinner";

import { askRepository } from "../api/chat";

import type { ChatResponse } from "../types/chat";
import RepositorySelector from "../components/RepositorySelector";
import ChatMessage from "../components/ChatMessage";
import toast from "react-hot-toast";
import Loader from "../components/Loader";

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
            toast.success("Response Generated");

        } catch (err) {

            console.error(err);

            toast.error("Chat Failed");

        }finally{
        setLoading(false);
        }
    }

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">

                Repository Chat

            </h1>

            <div className="bg-white rounded-xl shadow p-6">

                <RepositorySelector
                    value={repository}
                    onChange={setRepository}
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
                        disabled={loading}
                        className="bg-blue-600 text-white px-5 py-2 rounded mt-4 disabled:opacity-50 flex items-center gap-2"
                    >
                        {loading && (
                            <Oval
                                height={18}
                                width={18}
                                strokeWidth={4}
                                visible={true}
                            />
                        )}

                        {loading ? "Thinking..." : "Send"}
                    </button>

            </div>

            <div className="space-y-6 mt-8">

                {loading && <Loader />}

                {conversation.map((chat,index)=>(

                    <ChatMessage
                        key={index}
                        question={chat.question}
                        answer={chat.answer}
                        sources={chat.sources}
                    />

                ))}

            </div>

        </div>

    );

}

export default Chat;