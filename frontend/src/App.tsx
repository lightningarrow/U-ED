import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TestPage from "./pages/TestPage";
import ResultsPage from "./pages/ResultsPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/test/:videoId" element={<TestPage />} />
        <Route path="/results/:videoId" element={<ResultsPage />} />
      </Routes>
    </Router>
  );
}

export default App;
