export default function AIWorkspace() {
    return (

        <div className="bg-white rounded-xl shadow border h-full">

            <div className="border-b px-5 py-4 font-semibold">
                🤖 AI Workspace
            </div>

            <div className="p-4 space-y-3">

                <button className="w-full bg-blue-600 text-white rounded-lg py-3">
                    💬 Chat
                </button>

                <button className="w-full bg-purple-600 text-white rounded-lg py-3">
                    🔍 Search Repository
                </button>

                <button className="w-full bg-green-600 text-white rounded-lg py-3">
                    📝 Create File
                </button>

                <button className="w-full bg-orange-600 text-white rounded-lg py-3">
                    ✏ Edit File
                </button>

                <button className="w-full bg-gray-800 text-white rounded-lg py-3">
                    🤖 AI Agent
                </button>

            </div>

        </div>

    );
}