import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import Dashboard from "./pages/Dashboard";
import Repositories from "./pages/Repositories";
import Search from "./pages/Search";
import Review from "./pages/Review";
import Chat from "./pages/Chat";
import NotFound from "./pages/NotFound";
import RepositoryDetails from "./pages/RepositoryDetails";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route element={<MainLayout />}>

          <Route path="/" element={<Dashboard />} />

          <Route
            path="/repositories"
            element={<Repositories />}
          />

          <Route
            path="/search"
            element={<Search />}
          />

          <Route
            path="/review"
            element={<Review />}
          />

          <Route
            path="/chat"
            element={<Chat />}
          />

        </Route>

        <Route
          path="*"
          element={<NotFound />}
        />

        <Route
            path="/repository/:repository"
            element={<RepositoryDetails />}
         />

      </Routes>

    </BrowserRouter>
  );
}

export default App;