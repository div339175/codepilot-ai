import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Allotment } from "allotment";
import "allotment/dist/style.css";
import PageContainer from "../components/PageContainer";
import FileExplorer from "../components/workspace/FileExplorer";
import CodeViewer from "../components/workspace/CodeViewer";
import AIWorkspace from "../components/workspace/AIWorkspace";

import { getFile } from "../api/file";

export default function RepositoryDetails() {

    const { repository } = useParams();

    const [selectedFile, setSelectedFile] = useState<string | null>(null);
    const [fileContent, setFileContent] = useState("");

    useEffect(() => {

        if (!repository || !selectedFile) return;

        async function loadFile() {

            try {

                const data = await getFile(
                    repository,
                    selectedFile
                );

                setFileContent(data.content);

            } catch (err) {

                console.error(err);

            }

        }

        loadFile();

    }, [repository, selectedFile]);

    return (
    <PageContainer title="Repository WorkSpace">

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