import { useState } from "react";
import { Oval } from "react-loader-spinner";
import { askRepository } from "../api/chat";
import type { ChatResponse } from "../types/chat";
import RepositorySelector from "../components/RepositorySelector";
import ChatMessage from "../components/ChatMessage";
import toast from "react-hot-toast";
import Loader from "../components/Loader";
import { useEffect, useRef } from "react";
import { useSearchParams } from "react-router-dom";
import PageContainer from "../components/PageContainer";

function Chat() {

    const [searchParams] = useSearchParams();
    const repositoryFromUrl = searchParams.get("repo");
    const [repository, setRepository] = useState(
        repositoryFromUrl ?? ""
    );

    const [question, setQuestion] = useState("");

    const [conversation, setConversation] = useState<ChatResponse[]>([]);

    const [loading, setLoading] = useState(false);
    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [conversation]);

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
                {
                    ...response,
                    timestamp: new Date().toLocaleTimeString([], {
                        hour: "2-digit",
                        minute: "2-digit",
                    }),
                },
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

        <PageContainer title="Chat">

            <div className="bg-white rounded-2xl shadow-lg p-6 border">

                <RepositorySelector
                    value={repository}
                    onChange={setRepository}
                />

                <textarea

                    className="border rounded-xl w-full p-4 mt-4 resize-none"

                    rows={4}

                    placeholder="Ask anything..."

                    value={question}

                    onChange={(e)=>setQuestion(e.target.value)}

                />

                    <button
                        onClick={sendMessage}
                        disabled={loading}
                        className="mt-4 px-6 py-3 rounded-xl bg-blue-600 text-white hover:bg-blue-700 transition disabled:opacity-50"
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
                {loading && (

                <div className="flex items-center gap-3">

                    <div className="bg-white rounded-xl shadow px-5 py-4">

                        🤖 CodePilot AI is typing...

                    </div>

                </div>

            )}

                {conversation.map((chat,index)=>(
            
                    <ChatMessage
                        key={index}
                        question={chat.question}
                        answer={chat.answer}
                        sources={chat.sources}
                        timestamp={chat.timestamp}
                    />
                    

                ))}
                <div ref={bottomRef} />

            </div>

        </PageContainer>

    );

}

export default Chat;