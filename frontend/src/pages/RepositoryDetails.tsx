import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

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

        <PageContainer title="Repository Workspace">

            <div className="grid grid-cols-12 gap-6 h-[75vh]">

                <div className="col-span-3">

                    <FileExplorer
                        onSelectFile={setSelectedFile}
                    />

                </div>

                <div className="col-span-6">

                    <CodeViewer
                        filePath={selectedFile}
                        content={fileContent}
                    />

                </div>

                <div className="col-span-3">

                    <AIWorkspace />

                </div>

            </div>

        </PageContainer>

    );

}