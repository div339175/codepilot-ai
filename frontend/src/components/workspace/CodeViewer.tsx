import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

type Props = {
    filePath: string | null;
    content: string;
};

function getLanguage(file: string | null) {
    if (!file) return "text";

    if (file.endsWith(".py")) return "python";
    if (file.endsWith(".ts")) return "typescript";
    if (file.endsWith(".tsx")) return "tsx";
    if (file.endsWith(".js")) return "javascript";
    if (file.endsWith(".jsx")) return "jsx";
    if (file.endsWith(".json")) return "json";
    if (file.endsWith(".html")) return "html";
    if (file.endsWith(".css")) return "css";
    if (file.endsWith(".md")) return "markdown";
    if(file.endsWith(".ipynb"))return "ipynb"

    return "text";
}

export default function CodeViewer({
    filePath,
    content,
}: Props) {
    return (
        <div className="bg-white rounded-xl shadow border h-full flex flex-col">

            <div className="border-b px-5 py-4 font-semibold text-lg">
                {filePath ?? "Code Viewer"}
            </div>

            <div className="flex-1 overflow-auto bg-gray-900 text-gray-100 p-5 font-mono text-sm">

                {filePath ? (
                    <SyntaxHighlighter
                        language={getLanguage(filePath)}
                        style={oneDark}
                        showLineNumbers
                        wrapLongLines
                    >
                        {content}
                    </SyntaxHighlighter>
                ) : (
                    <div className="text-gray-400">
                        Select a file from the Explorer.
                    </div>
                )}

            </div>

        </div>
    );
}