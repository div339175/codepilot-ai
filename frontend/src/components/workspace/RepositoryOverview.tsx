import {
    BarChart3,
    FileText,
    Box,
    GitBranch
} from "lucide-react";

export default function RepositoryOverview() {

    return (

        <div className="bg-white rounded-xl shadow border h-full">

            <div className="border-b px-5 py-4 font-semibold text-lg">
                Repository Overview
            </div>

            <div className="grid grid-cols-2 gap-4 p-6">

                <div className="border rounded-lg p-5">

                    <BarChart3 className="text-blue-600 mb-3"/>

                    <h3 className="font-semibold">
                        Statistics
                    </h3>

                    <p className="text-gray-500 text-sm">
                        Files, folders and languages
                    </p>

                </div>

                <div className="border rounded-lg p-5">

                    <FileText className="text-green-600 mb-3"/>

                    <h3 className="font-semibold">
                        README
                    </h3>

                    <p className="text-gray-500 text-sm">
                        Documentation preview
                    </p>

                </div>

                <div className="border rounded-lg p-5">

                    <Box className="text-purple-600 mb-3"/>

                    <h3 className="font-semibold">
                        Dependencies
                    </h3>

                    <p className="text-gray-500 text-sm">
                        package.json & requirements.txt
                    </p>

                </div>

                <div className="border rounded-lg p-5">

                    <GitBranch className="text-orange-600 mb-3"/>

                    <h3 className="font-semibold">
                        Structure
                    </h3>

                    <p className="text-gray-500 text-sm">
                        Project architecture
                    </p>

                </div>

            </div>

        </div>

    );

}