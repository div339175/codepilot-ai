import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

import toast from "react-hot-toast";

interface Props {
    content: string;
}

function MarkdownRenderer({ content }: Props) {
    return (
        <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
                code({ className, children, ...props }) {

                    const match = /language-(\w+)/.exec(className || "");

                    if (match) {
                        return (
                            <div className="border rounded-lg overflow-hidden">

                            <div className="flex justify-between items-center bg-gray-800 text-white px-3 py-2">

                                <span>{match[1]}</span>

                                <button
                                    onClick={() => {
                                        navigator.clipboard.writeText(String(children).replace(/\n$/, ""));
                                        toast.success("Code copied");
                                    }}
                                    className="text-sm hover:underline"
                                >
                                    Copy
                                </button>

                            </div>

                            <SyntaxHighlighter
                                language={match[1]}
                                style={oneDark}
                                PreTag="div"
                            >
                                {String(children).replace(/\n$/, "")}
                            </SyntaxHighlighter>

                        </div>
                        );
                    }

                    return (
                        <code
                            className="bg-gray-200 px-1 rounded"
                            {...props}
                        >
                            {children}
                        </code>
                    );
                },
            }}
        >
            {content}
        </ReactMarkdown>
    );
}

export default MarkdownRenderer;