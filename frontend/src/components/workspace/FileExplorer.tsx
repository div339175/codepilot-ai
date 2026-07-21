import { useEffect, useState } from "react";
import { Folder, FileText } from "lucide-react";
import { useParams } from "react-router-dom";
import { getRepositoryTree } from "../../api/explore"; 
import type { TreeNode } from "../../api/explore";


export default function FileExplorer({
        onSelectFile,
    }: {
        onSelectFile: (path: string) => void;
    }) {
        
    const { repository } = useParams();

    const [tree, setTree] = useState<TreeNode[]>([]);

    useEffect(() => {
        if (repository) {
            loadTree();
        }
    }, [repository]);

    async function loadTree() {
        try {
            const data = await getRepositoryTree(repository!);
            setTree(data.children || []);
        } catch (err) {
            console.error(err);
        }
    }

    return (
        <div className="bg-white rounded-xl shadow border h-full overflow-auto">

            <div className="border-b px-5 py-4 font-semibold">
                📁 Explorer
            </div>

            <div className="p-3">

                {tree.map((item) => (
                    <TreeItem
                        key={item.path}
                        node={item}
                        level={0}
                        onSelectFile={onSelectFile}
                    />
                ))}

            </div>

        </div>
    );
}

function TreeItem({
    node,
    level,
    onSelectFile,
}: {
    node: TreeNode;
    level: number;
    onSelectFile: (path: string) => void;
}) {
    const [open, setOpen] = useState(false);

    return (
        <div>
            <div
                onClick={() => {
                    if (node.type === "folder") {
                        setOpen(!open);
                    } else {
                        onSelectFile(node.path);
                    }
                }}
                className="flex items-center gap-2 cursor-pointer rounded hover:bg-gray-100 py-2 px-2"
                style={{ paddingLeft: `${level * 18}px` }}
            >
                {node.type === "folder" ? (
                    <Folder size={18} className="text-yellow-500" />
                ) : (
                    <FileText size={18} className="text-blue-500" />
                )}

                <span>{node.name}</span>
            </div>

            {open &&
                node.children?.map((child) => (
                    <TreeItem
                        key={child.path}
                        node={child}
                        level={level + 1}
                        onSelectFile={onSelectFile}
                    />
                ))}
        </div>
    );
}