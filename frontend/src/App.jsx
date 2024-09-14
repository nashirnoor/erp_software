import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from "react-redux";
import { store } from "./features/store";
import Layout from "./components/layout/Layout";
import Branch from "./Branch";
import Store from "./Store";
import LoginPage from "./pages/generals/LoginPage";
import NotFound404 from "./components/layout/NotFound404";
import { BranchProtectedRoute } from "./components/layout/BranchProtectedRoute";
import {
  AuthenticatedRoute,
  StoreProtectedRoute,
} from "./components/layout/StoreProtectedRoute";
import Unauthorized from "./components/layout/Unauthorized";
import ErrorBoundary from "./components/layout/ErrorBoundary";
import TokenExpirationModal from "./components/modals/TokenExpirationModal";

function App() {
  return (
    <Provider store={store}>
      <ErrorBoundary>
        <Router>
          <TokenExpirationModal />
          <Routes>
            <Route
              path="/"
              element={
                <AuthenticatedRoute>
                  <LoginPage />
                </AuthenticatedRoute>
              }
            />
            <Route
              path="/branch/*"
              element={
                <BranchProtectedRoute allowedRoles={["branch_manager"]}>
                  <Layout>
                    <Branch />
                  </Layout>
                </BranchProtectedRoute>
              }
            />
            <Route
              path="/store/*"
              element={
                <StoreProtectedRoute allowedRoles={["admin","staff"]}>
                  <Layout>
                    <Store />
                  </Layout>
                </StoreProtectedRoute>
              }
            />
            <Route path="/unauthorized" element={<Unauthorized />} />
            <Route path="*" element={<NotFound404 />} />
          </Routes>
        </Router>
      </ErrorBoundary>
    </Provider>
  );
}

export default App;
