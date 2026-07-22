import { Bot } from "lucide-react";
import { useState } from "react";
import { askAgent } from "../../api/agent";
import { useEffect, useRef } from "react";

type Props = {
    repository: string;
    selectedFile: string | null;
    fileContent: string;
};

export default function AIWorkspace({
                repository,
                selectedFile,
                fileContent,
            }: Props) {
                
                const [isThinking, setIsThinking] = useState(false);

                const chatContainerRef = useRef<HTMLDivElement | null>(null);
                interface ChatMessage {
                    role: "user" | "assistant";
                    content: string;
                }
                const [prompt, setPrompt] = useState("");
                const [messages, setMessages] = useState<ChatMessage[]>([]);
                
                useEffect(() => {
                    if (chatContainerRef.current) {
                        chatContainerRef.current.scrollTop =
                            chatContainerRef.current.scrollHeight;
                    }
                }, [messages]);


                async function sendMessage() {

                        if (!prompt.trim()) return;

                        const userMessage = prompt;

                        setMessages((prev) => [
                            ...prev,
                            {
                                role: "user",
                                content: userMessage,
                            },
                        ]);

                        setPrompt("");

                        setIsThinking(true);

                        try {

                            const data = await askAgent(
                                repository,
                                selectedFile,
                                fileContent,
                                userMessage
                            );

                            setMessages((prev) => [
                                ...prev,
                                {
                                    role: "assistant",
                                    content: data.response,
                                },
                            ]);

                        } catch (error) {

                            console.error(error);

                            setMessages((prev) => [
                                ...prev,
                                {
                                    role: "assistant",
                                    content: "Backend connection failed.",
                                },
                            ]);

                        } finally {

                            setIsThinking(false);

                        }

                    }

    return (
        <div className="bg-white rounded-xl shadow border h-full min-h-0 flex flex-col">

            {/* Header */}
            <div className="border-b px-5 py-4 flex items-center gap-3">

                <Bot className="text-blue-600" size={28} />

                <div>

                   <h2 className="text-2xl font-bold whitespace-nowrap">
                        CodePilot AI
                    </h2>

                    <p className="text-sm text-gray-500 truncate">
                        Your AI Software Engineer
                    </p>

                </div>

            </div>

            {/* Context */}

           

            {/* Conversation */}

                <div
                    ref={chatContainerRef}
                    className="flex-1 min-h-0 overflow-y-auto bg-gray-50"
                >
                    <div className="p-4 space-y-4">

                {messages.length === 0 ? (

                    <div className="text-gray-400 text-center mt-10">

                        👋

                        <br /><br />

                        Ask me anything about this repository.

                    </div>

                ) : (

                    messages.map((message, index) => (

                        <div
                            key={index}
                            className={
                                message.role === "user"
                                    ? "flex justify-end"
                                    : "flex justify-start"
                            }
                        >

                            <div
                                className={
                                    message.role === "user"
                                        ? "bg-blue-600 text-white rounded-xl px-4 py-3 max-w-[90%]"
                                        : "bg-white border rounded-xl px-4 py-3 max-w-[90%]"
                                }
                            >

                                {message.content}

                            </div>

                        </div>

                    ))
                )}
                {isThinking && (

                        <div className="flex justify-start">

                            <div className="bg-gray-100 border rounded-xl px-4 py-3 text-gray-500 animate-pulse">

                                🤖 Thinking...

                            </div>

                        </div>

                    )}
            </div>

            </div>

            {/* Prompt */}

            <div className="border-t p-4 bg-white flex-shrink-0">

                <textarea
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Describe what to build..."
                    rows={3}
                    className="w-full rounded-lg border p-3 resize-none"
                    onKeyDown={(e) => {

                        if (e.key === "Enter" && !e.shiftKey) {

                            e.preventDefault();

                            sendMessage();

                        }

                    }}
                />

                <div className="flex items-center justify-between gap-3 mt-3">

                    <div className="flex items-center gap-2 flex-wrap">

                            <span className="px-3 py-1 rounded-full bg-gray-100 text-sm">
                                Auto
                            </span>

                            <span className="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-sm max-w-[120px] truncate">
                                {repository}
                            </span>

                            <span className="px-3 py-1 rounded-full bg-gray-100 text-gray-700 text-sm max-w-[170px] truncate">
                                {selectedFile ?? "No File"}
                            </span>

                        </div>

                        <button
                            onClick={sendMessage}
                            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
                        >
                            Send
                        </button>

                </div>

            </div>

        </div>
    );
}