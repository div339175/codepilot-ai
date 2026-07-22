import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Allotment } from "allotment";
import "allotment/dist/style.css";
import PageContainer from "../components/PageContainer";
import FileExplorer from "../components/workspace/FileExplorer";
import CodeViewer from "../components/workspace/CodeViewer";
import AIWorkspace from "../components/workspace/AIWorkspace";
import { getFile } from "../api/file";
import { ArrowLeft } from "lucide-react";
import { useNavigate } from "react-router-dom";


export default function RepositoryDetails() {

    const { repository } = useParams();
    const navigate = useNavigate();
    const [selectedFile, setSelectedFile] = useState<string | null>(null);
    const [fileContent, setFileContent] = useState("");

    useEffect(() => {

        if (!repository || !selectedFile) return;

        // Create local constants after the guard
        const repo = repository;
        const file = selectedFile;

        async function loadFile() {

            try {

                const data = await getFile(
                    repo,
                    file
                );

                setFileContent(data.content);

            } catch (err) {

                console.error(err);

            }

        }

        loadFile();

    }, [repository, selectedFile]);

    return (
            <PageContainer
                title="Repository Workspace"
                action={
                <button
                    onClick={() => navigate("/repositories")}
                    className="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium transition"
                >
                    <ArrowLeft size={18} />
                    Back to Repositories
                </button>
              }
           >

        <div className="h-[88vh]">

            <Allotment>

                {/* Explorer */}

                <Allotment.Pane
                    preferredSize={280}
                    minSize={220}
                >

                    <FileExplorer
                        onSelectFile={setSelectedFile}
                    />

                </Allotment.Pane>

                {/* Code */}

                <Allotment.Pane
                    preferredSize={700}
                    minSize={350}
                >

                    <CodeViewer
                        filePath={selectedFile}
                        content={fileContent}
                    />

                </Allotment.Pane>

                {/* AI */}

                <Allotment.Pane
                    preferredSize={500}
                    minSize={320}
                >

                    <AIWorkspace
                        repository={repository ?? ""}
                        selectedFile={selectedFile}
                        fileContent={fileContent}
                    />

                </Allotment.Pane>

            </Allotment>

        </div>

    </PageContainer>
);

}