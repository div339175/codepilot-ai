import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen p-6">
      <h1 className="text-2xl font-bold mb-8">
        CodePilot AI
      </h1>

      <nav className="space-y-3">

        <Link
          to="/"
          className="block p-3 rounded hover:bg-slate-700"
        >
          Dashboard
        </Link>

        <Link
          to="/repositories"
          className="block p-3 rounded hover:bg-slate-700"
        >
          Repositories
        </Link>

        <Link
          to="/search"
          className="block p-3 rounded hover:bg-slate-700"
        >
          Semantic Search
        </Link>

        <Link
          to="/review"
          className="block p-3 rounded hover:bg-slate-700"
        >
          AI Review
        </Link>

        <Link
          to="/chat"
          className="block p-3 rounded hover:bg-slate-700"
        >
          Repository Chat
        </Link>

      </nav>
    </aside>
  );
}

export default Sidebar;